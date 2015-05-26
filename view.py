from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
import models
import tweepy

from category import ReviewCategories

from settings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, URL, LINKEDIN_API_KEY, LINKEDIN_SECRET_KEY, TWITTER_KEY, TWITTER_SECRET


from google.appengine.api import memcache
from google.appengine.api import urlfetch
from google.appengine.api import mail
from urlparse import urlparse
from urllib import urlencode
from random import randint


import json
import datetime
import re

# for displaying debug messages in GAE log.  Use logging.error()
import logging




###############################################################################
# Notes
###############################################################################

# USER is used for the person, network id's are for permission
# memcache needs to be updated when USER and ACCOUNT are changed or set
# 





###############################################################################
# Controllers for each page of the site
###############################################################################


# High hits
def homepage(request):
    
    # Check if the user is already logged in, if so send them to the searchpage
    if (request.user.is_authenticated() ):
        return redirect("/home")
    
    else:
        # Pass redirect string if needed
        return render(request, 'hopku.html', {"querystring": ( request.get_full_path() )[1:] })



# High hits
def signup(request):

    # Only show if they aren't already logged in
    if ( not request.user.is_authenticated() ):
        return render(request, "signup.html")
    
    else:
        return redirect("/")



# privacy policy
def privacy(request):
    return render(request, "privacy.html")



# sample review
def sample(request):
    return render(request, "sample.html")



#tos
def tos(request):
    return render(request, "tos.html")



def contact(request):
    
    # Only display the page if the user is logged in
    if ( request.user.is_authenticated() ) :
        return render(request, "contact.html")
    
    # If not, redirect to the homepage to log in
    else:
        return redirect("/#NotAuthenticated")



# High hits
def searchpage(request):
    
    # Only display the page if the user is logged in
    if ( request.user.is_authenticated() ):
        return render(request, "home.html", {"products": ReviewCategories.products, "services": ReviewCategories.services, "events": ReviewCategories.events})

    # If not, redirect them to the homepage to login 
    else:
        return redirect("/#NotAuthenticated")




def learnmore(request):
    # Check if the user is already logged in
    isloggedin = request.user.is_authenticated()
    
    # Only display certain links on the page if they're logged in
    return render(request, "learnmore.html", {"loggedin": isloggedin})



def biz(request):
    # Check if the user is already logged in
    isloggedin = request.user.is_authenticated()
    
    # Only display certain links on the page if they're logged in
    return render(request, "biz.html", {"loggedin": isloggedin})





# High hits
def account(request):

    # Only display the page if the user is logged in
    if ( request.user.is_authenticated() ): 
        
        currentuser = getcurrentuser(request)
        accountinfo = getuseraccount(currentuser)

        hopkufriends = ""

        
        if accountinfo.hopkufriends:    
            hopkufriends = str(",".join( eval(accountinfo.hopkufriends) ) )
       
        
        
        return render(request, "account.html", {"username": currentuser.username, "email": currentuser.email, "mycsrf": accountinfo.mycsrf, "facebookchecked": accountinfo.facebookid, "linkedchecked": accountinfo.linkedinid, "twitterchecked": accountinfo.twitterid, "hopkufriends": hopkufriends})
    
    
    # If not, redirect to the homepage to login
    else:
        return redirect("/#NotAuthenticated")





# High hits
def write(request):
    
    # Only display the page if the user is logged in
    if ( request.user.is_authenticated() ) :

        currentuser = getcurrentuser(request)
        accountinfo = getuseraccount(currentuser)

        noaccounts = False

        if (not accountinfo.facebookid) and (not accountinfo.linkedinid) and (not accountinfo.twitterid) and (not accountinfo.hopkufriends):
            noaccounts = True
        
        
        return render(request, "write.html", {"products": ReviewCategories.products, "services": ReviewCategories.services, "events": ReviewCategories.events, "noaccounts": noaccounts})
    
    # If not, redirect to the homepage to log in
    else:
        return redirect("/#NotAuthenticated")



# High Hits
def readreview(request, reviewtype, number):

        number = int(number)

        rev = re.sub(r'[^a-zA-Z]', '', reviewtype).lower()


        reviewtype = ReviewCategories.hashmapper[rev]

        
        try:
            # The review itself
            review = reviewtype.objects.get(id=number)
            revaccount = getuseraccount(review.user) 
        
        except ObjectDoesNotExist:
            raise Http404

        

        location = str(review.zipcode)

        if location == "0":
            location = False
        

        refferer = str(request.META.get("HTTP_REFERER", "")).startswith("https://www.facebook.com")
        refferer = refferer or str(request.META.get("HTTP_REFERER", "")).startswith("https://t.co/") 
        

        
        if ( refferer and ( len(review.stars) > 3 ) ):


            logging.error("Someone read a review")
            
            return render(request, "readreview.html", {"name": review.name, "author": (review.user.first_name +" "+review.user.last_name), "location": location, "description": review.description, "stars": review.stars, "reviewtext": review.reviewtext, "date": review.date, "url": review.url, "reff": True, "media": review.mediaurls, "auth": request.user.is_authenticated()})



        # First we need to check that the user is allowed to read the review, then we present the review

        if request.user.is_authenticated():
            
            # Get users list of friends and contacts credentials for social networks
            currentuser = getcurrentuser(request)
            useraccount = getuseraccount(currentuser) 
        
            fbfriends = getfriends(useraccount, "facebookfriends")        
            infriends = getfriends(useraccount, "linkedinfriends")
            twfriends = getfriends(useraccount, "twitterfriends")
            hpfriends = getfriends(useraccount, "hopkufriends")



            # Check if the reviewer is in the list of people the user is friends with

            facebookid = review.facebookid
            linkedid = review.linkedinid
            twitterid = review.twitterid
            hpname = review.username

        
            # a friend or from facebook, twitter, linkedin or hopku
            if (facebookid in fbfriends) or (twitterid in twfriends) or ( (hpname in hpfriends) and (currentuser.username in revaccount.hopkufriends) ) or (linkedid in infriends) :

                
                logging.error("Someone read a review")

            
                return render(request, "readreview.html", {"name": review.name, "author": (review.user.first_name +" "+review.user.last_name), "location": location, "description": review.description, "stars": review.stars, "reviewtext": review.reviewtext, "date": review.date, "url": review.url,"reff": False, "media": review.mediaurls, "auth": True})
        
        
            
            # if the current user wrote the review, they may edit it
            elif ( currentuser.id == review.user.id ):
            
                return render(request, "readreview.html", {"name": review.name, "author": (review.user.first_name +" "+review.user.last_name), "location": location, "description": review.description, "stars": review.stars, "reviewtext": review.reviewtext, "date": review.date, "url": review.url, "reff": False, "edit": True, "id": review.id, "media": review.mediaurls, "rev": rev, "auth": True})


            # otherwise the requester is not allowed to view this review
            else:
                raise PermissionDenied
        
        
        
        else:
            return redirect("/")
            
    
    



###############################################################################
# Controllers for form submissions
###############################################################################



# High Hits
# When the user tries to login from the home page
def hopkulogin(request):

    # Get username and password from Http request
    if (request.method == "POST") and (not request.user.is_authenticated() ) :

        username = request.POST.get("username", "")
        password = request.POST.get("password", "")


        # If one of the fields is empty, reject the login
        if (not username) or (not password):
            raise Exception
        
        
        user = authenticate(username=username, password=password)


        # An error occured
        if user is None:
            return redirect("/#Error")
        
        
        # the user is now added to the session backend
        login(request, user)


        
        # See if there's a redirect url in the query string
        goto = request.get_full_path()[ (request.get_full_path().find("redirect=") + 9) : ]

                
        if not goto:
            return redirect("/home")
        
        
        return redirect(goto)





# Handle the users logout 
def hopkulogout(request):

    if ( request.user.is_authenticated() ): 
        
        logout(request)
        
        # Update memcache for this user
        memcache.delete("u"+str(request.user.id) )
        memcache.delete("a"+str(request.user.id) )


    return redirect("/")






# delete the users account and associated reviews
def deleteaccount(request):
    
    if ( request.user.is_authenticated() ):

        
        currentuser = getcurrentuser(request)

        # Update memcache for this user
        memcache.delete("u"+str(request.user.id) )
        memcache.delete("a"+str(request.user.id) )

        
        # delete all reviews they wrote
        for revtype, reviewtype in ReviewCategories.hashmapper.items():
            reviewtype.objects.filter(user=currentuser).delete()
        
        

        # delete the account
        models.Accounts.objects.filter(user=currentuser).delete()
        

        # delete the user account
        User.objects.filter(pk=request.user.pk).delete()
        


        return redirect("/#DeletionSuccessful")
        
    
    
    else:
        return redirect("/#NotAuthenticated")       








# If csrf mechanism fails
def csrf_failure(request, reason=""):
    
    logging.error("Someone's csrf failed: "+reason)
    return render(request, "403.html")





# When the user wants to change their account info
def updateaccount(request):
    
    # The user must be logged in in order to do this
    if ( request.user.is_authenticated() ) and (request.method == "POST"):

        facebook = request.POST.get("facebook", "")
        linkedin = request.POST.get("linkedin", "")
        hopkufriends = request.POST.get("hopkufriends", "")
        twitter = request.POST.get("twitter", "")
        email = request.POST.get("emailaddress", "")
        oldpass = request.POST.get("oldpassword", "")
        newpass = request.POST.get("newpassword", "")
        newpass2 = request.POST.get("newpassword2", "")
        

        currentuser = getcurrentuser(request)
        account = getuseraccount(currentuser)


        # No matter what, update
        account.hopkufriends = hopkufriends.split(",")

        
        
        # If a text field is blank, do nothing.  If a text field has content, update it
        # If a checkbox is unchecked, delete everything for that network for the user (id, token, friends)

        if email:
            currentuser.email = email
        
               
        if oldpass:
            # test that oldpass is correct, if so set password as new one
            if currentuser.check_password(oldpass):
                currentuser.set_password(newpass)
            
            else:
                return redirect("/account#Wrongpassword")
        
        
        if not facebook:
            account.facebookid = ""
            account.facebooktoken = ""
            account.facebookfriends = ""
        
        
        
        if not linkedin:
            account.linkedinid = ""
            account.linkedintoken = ""
            account.linkedinfriends = ""
        
        
        if not twitter:
            account.twitterid = ""
            account.twitterkey = ""
            account.twittersecret = ""
            account.twitterfriends = ""
        
        
        currentuser.save()
        account.save()

        # Update memcache for this user
        memcache.delete("u"+str(currentuser.id) )
        memcache.delete("a"+str(currentuser.id) )

        

        return redirect("/#Accountupdated")
   
    
    else:
        return redirect("/#NotAuthenticated")


    

# High Hits
# When the user is signing up for the service
def register(request):
    
    if (request.method == "POST") and (not request.user.is_authenticated() ):
        
        # Get fields from registration form
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        tos = request.POST.get("tosagree", "")

        #recaptchachallenge = request.POST.get("recaptcha_challenge_field", "")
        #recaptchatext = request.POST.get("recaptcha_response_field", "")

        captchavalue = request.POST.get("captcha", "")

        # if recaptcha was ignored
        #if (not recaptchachallenge) or (not recaptchatext):
        #    return redirect("/signup#captcha")

        
        captchavalue = captchavalue.lower()
        
        if not ( (captchavalue == "4") or (captchavalue == "four") ):
            return redirect("/signup#captcha")
        
        

        # if any aren't filled out send them back
        if (not username) or (not password) or (not tos):
            return redirect("/signup#fillout")
        
        
            
        # check that the username isn't already taken. if it is, abort and alert
        sameusernames = User.objects.filter(username__exact=username)
        
        if sameusernames.exists():
            return redirect("/signup#Error")
        
        
        #ipaddr = request.META["REMOTE_ADDR"] 
        

        
        # reCaptcha check
        #formfields = urlencode( {"privatekey": "6LcZuOoSAAAAAA9GzeAWGE_p7E9H9Wio8wR06c6n", "remoteip": ipaddr, "challenge": recaptchachallenge, "response": recaptchatext} )

        #result = urlfetch.fetch(url="https://www.google.com/recaptcha/api/verify", payload=formfields, method=urlfetch.POST, validate_certificate=True).content.split("\n")[0]


       
        #if not (result == "true"):
        #    return redirect("/signup#captcha")    

        
        import random
        import string
        
        
        # Create and save the newly registered user to the system
        newuser = User.objects.create_user(username, "", password)

       
        # set a name to show up on reviews
        newuser.first_name = username
        newuser.save() 
        
       
        # generate a random string for csrf
        csrf = str( "".join([random.choice(string.ascii_letters + string.digits) for n in range(40)]) )
        
        # Create and save an associated accounts table to the system
        models.Accounts(user=newuser, mycsrf=csrf).save()



        
        # login will be forced to change last login so it won't throw an error
        newuser.last_login = newuser.last_login - datetime.timedelta(seconds=60)
        newuser.save()

        

        # Authenticate the new user
        newuser = authenticate(username=username, password=password)

        
        # if that odd login exception happens, just chalk it up as the username already existing
        try:
            login(request, newuser)
        
        except:
            logging.error("Login Exception Occurred")
            return redirect("/signup#Error")
            



        # email me about new user
        emailcontent = "Username: "+username+"\n"
        subject = "Hopku: New User"

        mail.send_mail("Arash.Khan.01@gmail.com", "Arash.Khan.01@gmail.com", subject, emailcontent)
        

        
        return redirect("/account#GettingStarted")




# High Hits
# When the user submits a review
def review(request):

    # The user must be logged in to perform this action
    if ( request.user.is_authenticated() ) and ( request.method == "POST" ):
        
        # Get fields from the form
        category = request.POST.get("category", "")
        name = request.POST.get("name", "")
        period = request.POST.get("periodofuse", "")
        zipcode = request.POST.get("zipcode", "")
        description = request.POST.get("description", "")
        rating = request.POST.get("rating", "")
        review = request.POST.get("review", "")
        url = request.POST.get("url", "")
        media = request.POST.get("media", "") 
        

        # Check if a required field is empty, if so send them back
        if (not name) or (not category) or  (not description) or (not rating) or (not review):
            raise Exception
        
        
        # Remove non-alpha numeric from name and description (easier on searches)
        name = re.sub('[^0-9a-zA-Z]+', " ", name)
        description = re.sub('[^0-9a-zA-Z]+', " ", description) 
        
               
        # Remove text from rating
        rating = rating.split(" ")[0]

        currentuser = getcurrentuser(request)
        useraccount = getuseraccount(currentuser)


        catname = re.sub(r'[^a-zA-Z]', '', category).lower()
        category = ReviewCategories.hashmapper[catname]

        period = durationtonumber(period)
       

        if not zipcode:
            zipcode = 0
        
        
        # Create a review instance and save it
        submittedrev = category(user=currentuser, username=currentuser.username, facebookid=useraccount.facebookid, twitterid=useraccount.twitterid, linkedinid=useraccount.linkedinid, name=name, zipcode=int(zipcode), description=description, duration=period, stars=rating, reviewtext=review, url=url, mediaurls=media)

        submittedrev.save()
        

        # Check if the rating is high, if so post it to Facebook and Twitter

        if (len(rating) > 3) and useraccount.facebookid:

            fakenum = ''.join(["%s" % randint(0,9) for num in range(0, 10)])

            snippet = " ".join( review.split()[0:35] ) + " ..."
       
            
            # Post to Facebook (this should be async)
            postfields = urlencode( {"access_token": useraccount.facebooktoken, "message": "Reviewed "+name, "name": name, "caption": description, "description": snippet, "link": URL+"/review/"+catname+"/"+str(submittedrev.id)+"?fbauth="+str(fakenum), "privacy": "{'value':'ALL_FRIENDS'}"} )
       

            # async
            rpc = urlfetch.create_rpc()
            
            urlfetch.make_fetch_call(rpc=rpc, url="https://graph.facebook.com/"+ useraccount.facebookid +"/feed", payload=postfields, method=urlfetch.POST, validate_certificate=True)

        
        
        # post to twitter
        if (len(rating) > 3) and useraccount.twitterid:

            fakenum = ''.join(["%s" % randint(0,9) for num in range(0, 10)])

            auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
            auth.set_access_token(useraccount.twitterkey, useraccount.twittersecret)
            
            api = tweepy.API(auth)

            api.update_status("Reviewed "+name+ ".  " + str(len(rating)) + " stars. "+URL+"/review/"+catname+"/"+str(submittedrev.id)+"?twauth="+str(fakenum))
        
        
        # email me about new reviews
        emailcontent = "New Hopku Review: "+currentuser.username+"\n"+name+"\n"
        subject = "Hopku: New Review"

        mail.send_mail("Arash.Khan.01@gmail.com", "Arash.Khan.01@gmail.com", subject, emailcontent)

            
            

        # Send them back home
        return redirect("/home#SuccessfulReview")




# returns a page (or pages) showing all the users reviews 
def myreviews(request, page="1"):

    page = int(page)
   
    resultsperpage = 10


    # The user must be logged in to do this
    if ( request.user.is_authenticated() ) : 

        currentuser = getcurrentuser(request)
        useraccount = getuseraccount(currentuser)

        allreviews = []


        
        for revtype, reviewtype in ReviewCategories.hashmapper.items():


            values = reviewtype.objects.filter(user=currentuser).values("name", "stars", "description", "id")

            
            # may not have written a review in this category
            if values:
            
                # could be many per category
                for review in values:
                
                    review["rev"] = revtype
                    
                allreviews.extend( values )
            
        
        
        allreviews = allreviews[( (page-1)*resultsperpage ) : (page*resultsperpage)]


        return render(request, "searchmore.html", {"reviews": allreviews, "extra": True, "page": {"prev": page -1, "next": page + 1}, "url": "myreviews"}) 


    else:

        raise Exception


    



# High Hits
# When the user submits a search query (meat and potatoes of the app)
# Note that everything returned from this view is rendered inpage using AJAX
def search(request, page="1"):

    page = int(page)

    resultsperpage = 10

    
    # The user must be logged in to do this
    if ( request.user.is_authenticated() ) :
        
        # Get search queries from request (database stores strings as unicode)
        query = unicode( request.GET.get("query", "") )
        category = unicode( request.GET.get("category", "") )


        # No query provided
        if not category:
            raise Exception
        
        
        # Log the query so that we can see how users are using Hopku
        # DO NOT REMOVE
        logging.info("Search Query: "+category+": "+query)


        category = re.sub(r'[^a-zA-Z]', '', category).lower()
        query = re.sub('[^0-9a-zA-Z]+', " ", query)
        
        revtype = category
        

        category = ReviewCategories.hashmapper[category]


        # Get user's credentials for social networks
        currentuser = getcurrentuser(request)
        useraccount = getuseraccount(currentuser)
        
        facebookid = useraccount.facebookid 
        facebooktoken = useraccount.facebooktoken
       
        linkedintoken = useraccount.linkedintoken
        
        twitterkey = useraccount.twitterkey
        twittersecret = useraccount.twittersecret
       

        # last time networks were updated
        lastupdate = useraccount.netupdate
        fivedays = datetime.timedelta(days=10)
        
        # Once a week, update the friends lists
        if (not lastupdate) or ( datetime.datetime( int(lastupdate.split("-")[0]), int(lastupdate.split("-")[1]), int(lastupdate.split("-")[2]) ) + fivedays < datetime.datetime.now() ):
        
            
            useraccount.netupdate = str(datetime.datetime.now()).split()[0]
            useraccount.save()
            memcache.delete("a"+str(currentuser.id) )
            
            
            
            if facebookid:
                # Update facebook friends (the token will expire after 60 days, after which we need to go through the authorization process again)

                # If a failure occurs, just let it pass
                try:
                   
                    facebookfriendidlist = fetchfacebookfriends(facebooktoken, useraccount.mycsrf, request)

                    # it's the reauthorize prompt
                    if not (type(facebookfriendidlist) is list ):
                        return facebookfriendidlist

                    
                    updateaccountmodel(request, facebookfriends=str(facebookfriendidlist) )

                except Exception as e:
                    logging.error("Facebook Friend Update Failed" + str(e) )
                
                

            if linkedintoken:
            
                # Update Linkedin Friends (the token will expire after 60 days, after which we need to go through the authorization process again)
                # If call fails, let it pass
                try:
                    
                    linkedinfriendslist = fetchlinkedinfriends(linkedintoken, useraccount.mycsrf, request)

                    # it's the reauthorize prompt
                    if not (type(linkedinfriendslist) is list ):
                        return linkedinfriendslist

                    
                    updateaccountmodel(request, linkedinfriends=str( linkedinfriendslist ) )

                except Exception as e:
                    logging.error("Linkedin Friend Update failed " + str(e) )


            
            # Update Twitter Friends (note that Twitter token never expires)
            if twitterkey:
               
                try:
                    
                    twitterfriendslist = fetchtwitterfriends(twitterkey, twittersecret)  

                    # it's the reauthorize prompt
                    if not (type(twitterfriendslist) is list ):
                        return twitterfriendslist

                    
                    updateaccountmodel(request, twitterfriends=str(twitterfriendslist) )
 
                except Exception as e:
                    logging.error("Twitter friend update failed" + str(e) )
    


       
        # Get list of friends, connections and followings (unicode strings)
        facebookfriendidlist = getfriends(useraccount, "facebookfriends")       
        linkedinfriendidlist = getfriends(useraccount, "linkedinfriends")       
        twitterfriendidlist = getfriends(useraccount, "twitterfriends")       
        hopkufriendslist = getfriends(useraccount, "hopkufriends")


        # Make sure everyone in Hopku ID list also has them in theirs
        twowayhopku = []
        hopkufriends = models.Accounts.objects.filter(user__username__in=hopkufriendslist).values("user__username", "hopkufriends")

        
        for friend in hopkufriends:

            if currentuser.username in friend["hopkufriends"]:
                twowayhopku.append(friend["user__username"])
        

        
        # A queryset of all friends reviews
        facebookfriendsquery = category.objects.filter(facebookid__in=facebookfriendidlist)
        linkedinfriendsquery = category.objects.filter(linkedinid__in=linkedinfriendidlist)
        hopkufriendsquery = category.objects.filter(username__in=twowayhopku)
        twitterfriendsquery = category.objects.filter(twitterid__in=twitterfriendidlist)


        allfriends = facebookfriendsquery | twitterfriendsquery | hopkufriendsquery | linkedinfriendsquery 

       
        reviews = []
        start = (page-1)*resultsperpage 
        end = (page*resultsperpage) 
       
        qnum = True
        
       
        if query:


            qnum = True


            # remove unneccessary words (a, an, the)
            query = query.split()
            query = " ".join([ word for word in query if not word in ('a', 'an', 'the') ])
            
            # Don't look beyond their exact query here (if it's an exact name)
            containsreviewsbyname = allfriends.filter(name__icontains=query)

            nameregex = allfriends.filter(name__iregex=r'heythere')

        
            # If this applies, they didn't give an exact name.  We can modify query to give better results
            # chaining 'exclude' OR's them


            
            # remove certain words and convert to ratings >= 4
            query = query.split()
            ratingflag = False

            if ('good' in query) or ('great' in query) or ('best' in query) or ('nice' in query):
                ratingflag = True
                query = " ".join([ word for word in query if not word in ('good', 'great', 'best', 'nice') ])
           
            else:
                query = " ".join(query)
        
            
            if ratingflag:
                containsreviewsbydescription = allfriends.filter(description__icontains=query, stars__in=[u"\u2605\u2605\u2605\u2605", u"\u2605\u2605\u2605\u2605\u2605", u"\u2605\u2605\u2605\u2605\u2605\u2605"]).exclude(name__icontains=query) 
            
            else:
                containsreviewsbydescription = allfriends.filter(description__icontains=query).exclude(name__icontains=query)

            
            descriptionregex = allfriends.filter(description__iregex=r'heythere')
            
                   

            # merge reviews together
            a = containsreviewsbyname.values("name","user__first_name", "user__last_name", "stars", "description", "id")
            b = containsreviewsbydescription.values("name","user__first_name", "user__last_name", "stars", "description", "id")
            c = nameregex.values("name","user__first_name", "user__last_name", "stars", "description", "id")
            d = descriptionregex.values("name","user__first_name", "user__last_name", "stars", "description", "id")



            count = -1
            for review in generatereviews(first=a, second=b, third=c, fourth=d):

                count = count + 1

                if count < start:
                    continue
                
                if count >= end:
                    break
                
                reviews.append(review)

            
                    
        else:


            qnum = False
            
            a = allfriends.values("name","user__first_name", "user__last_name", "stars", "description", "id")


            count = -1
            for review in generatereviews(first=a):

                count = count + 1

                if count < start:
                    continue
                
                if count >= end:
                    break
                
                reviews.append(review)


       
        extra = True

        
        if len(reviews) < resultsperpage:
            extra = False
        
       
        # Return HTML content to AJAX request
        if page == 1:
            
            return render(request, "searchresults.html", {"reviews": reviews, "extra": extra, "prevpage": False, "page": {"prev": page -1, "next": page + 1}, "query": query, "rev": revtype, "bigquery": qnum}) 

        
        
        if page > 1:

            return render(request, "searchmore.html", {"reviews": reviews, "extra": extra, "prevpage": True, "page": {"prev": page -1, "next": page + 1}, "query": query, "rev": revtype, "url": "search", "bigquery": qnum})
        
        
        else:
            raise Exception
    



# a generator that will generate the reviews on demand
def generatereviews(first, second=None, third=None, fourth=None):

    for i in first:
        yield i
   
    
    if not (second == None):
        for i in second:
            yield i
    
    if not (third == None):
        for i in third:
            yield i
    
    if not (fourth == None):
        for i in fourth:
            yield i
    
    




# user sends us an email
def usercontact(request):

    if (request.user.is_authenticated()) and (request.method == "POST"): 

        subject = request.POST.get("subject", "") 
        emailcontent = request.POST.get("email", "")

        user = getcurrentuser(request) 
        
        userid = str(user.id)
        username = str(user.username)
        firstname = str(user.first_name)
        emailaddr = str(user.email)

        emailcontent = emailcontent+"\n\n\nUserID: "+userid+"\nUsername: "+username+"\nFirst Name: "+firstname+"\nEmail: "+emailaddr
        subject = "Hopku: "+subject

        
        # Send this email to me
        me = "Arash.Khan.01@gmail.com"

        mail.send_mail(me, me, subject, emailcontent)


        return redirect("/home#GotEmail")
        



# allow user to update their review
def updatereview(request, reviewtype, number):

    # determine user and review.  make sure user wrote that review
    # then append content to review text

    if ( request.user.is_authenticated() ) and ( request.method == "POST" ):
       
        
        reviewid = int(number)

        reviewtype = ReviewCategories.hashmapper[re.sub(r'[^a-zA-Z]', '', reviewtype).lower()]
        
        currentuser = getcurrentuser(request)
        review = reviewtype.objects.get(id=reviewid)

    
        # the viewer is the reviewer 
        if currentuser.id == review.user.id:
        
            update = request.POST.get("update", "")

            fullreview = review.reviewtext + " ... UPDATE ("+ datetime.date.today().strftime("%B %d, %Y") +"): " + update

            review.reviewtext = fullreview

            review.save()
            
            return redirect("/home#SuccessfulReview")
    
    
        else:
            raise PermissionDenied

    



# Handle the facebook login flow
def facebooklogin(request):
    
    # Get the parameters from facebook's redirect
    parameter = urlparse( request.build_absolute_uri() ).query


    # if the user didn't allow FB login
    if "error" in parameter:
        return redirect("/account#FBfailed")
   
    
    
    # removes the 'code=' part
    code = re.search('code=(.*)&state=', parameter).group(1)
    csrftoken = re.search('&state=(.*)', parameter).group(1)


    currentuser = getcurrentuser(request)
    
    # Likely a csrf attack has occured
    if not (csrftoken == models.Accounts.objects.get(user=currentuser).mycsrf):
       raise PermissionDenied
    

    try:
    
        # get access token from facebook
        response = urlfetch.fetch(url="https://graph.facebook.com/oauth/access_token?client_id="+FACEBOOK_APP_ID+"&redirect_uri="+URL+"/facebookhandler"+"&client_secret="+FACEBOOK_APP_SECRET+"&code="+code, deadline=30.0, validate_certificate=True, method=urlfetch.GET)


        # extract access token
        accesstoken = re.search('access_token=(.*)&expires=', response.content).group(1)


        # Security check
        response = urlfetch.fetch(url="https://graph.facebook.com/oauth/access_token?client_id="+FACEBOOK_APP_ID+"&client_secret="+FACEBOOK_APP_SECRET+"&grant_type=client_credentials", deadline=30.0, validate_certificate=True, method=urlfetch.GET)

        apptoken = re.search('access_token=(.*)', response.content).group(1)

        response = urlfetch.fetch(url="https://graph.facebook.com/debug_token?input_token="+accesstoken+"&access_token="+apptoken, deadline=30.0, validate_certificate=True, method=urlfetch.GET)

        data = json.loads(response.content)

    
        if data["data"]["app_id"] == int(FACEBOOK_APP_ID):
            userid = str(data["data"]["user_id"])
    
        else:
            logging.error("Facebook graph debug_token returned a different app id")
            return redirect("/account#FBfailed")
    
    
        # Get an extended token (will last for 60 days)
        response = urlfetch.fetch(url="https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id="+FACEBOOK_APP_ID+"&client_secret="+FACEBOOK_APP_SECRET+"&fb_exchange_token="+accesstoken, deadline=30.0, validate_certificate=True, method=urlfetch.GET) 
    
   
        # get long lived access token
        accesstoken = re.search('access_token=(.*)&expires=', response.content).group(1) 
    
        # Store friendslist
        facebookfriendidlist = fetchfacebookfriends(accesstoken, models.Accounts.objects.get(user=currentuser).mycsrf, request)    


        # Update user's name
    
        if not currentuser.last_name:
            jsondata = json.loads(urlfetch.fetch(url="https://graph.facebook.com/me?access_token="+accesstoken, deadline=30.0, validate_certificate=True, method=urlfetch.GET).content) 
      
            setusersname(currentuser, jsondata["first_name"], jsondata["last_name"])
               
    
    # If anything goes wrong in this block, it's because something went wrong with the FB call
    except Exception as e:
        logging.error("Facebook login failed : %s\n" % e )
        return redirect("/account#FBfailed")
    
    
    # Store user_id, access token and facebook friendslist (find associated user and add token and id to the accounts table)
    updateaccountmodel(request, facebookid=userid, facebooktoken=accesstoken, facebookfriends=str(facebookfriendidlist) )
    

    return redirect("/account")





# Handle the linkedin login process
def linkedinlogin(request):

    querystrings = urlparse( request.build_absolute_uri() ).query

    if re.search('code=(.*)&', querystrings) == None:
        return redirect("/account")
    
    
    code = re.search('code=(.*)&', querystrings).group(1)
    returnedcsrf = re.search('state=(.*)', querystrings).group(1)


    currentuser = getcurrentuser(request)
    
    if not (returnedcsrf == getuseraccount(currentuser).mycsrf):
        raise PermissionDenied

   
    try:
        response = urlfetch.fetch(url="https://www.linkedin.com/uas/oauth2/accessToken?grant_type=authorization_code&code="+code+"&redirect_uri="+ URL + "/linkedinhandler&client_id="+LINKEDIN_API_KEY+"&client_secret="+LINKEDIN_SECRET_KEY, deadline=30.0, validate_certificate=True, method=urlfetch.GET)

        data = json.loads(response.content)


        linkedintoken = data["access_token"]


        linkedinfriendslist = fetchlinkedinfriends(linkedintoken, getuseraccount(currentuser).mycsrf, request)

    
        linkedinid = json.loads( urlfetch.fetch(url="https://api.linkedin.com/v1/people/~:(id)?oauth2_access_token="+linkedintoken+"&format=json", deadline=30.0, validate_certificate=True, method=urlfetch.GET).content )[u'id']


    # Update user's name
        jsondata = json.loads( urlfetch.fetch(url="https://api.linkedin.com/v1/people/~:(first-name,last-name)?oauth2_access_token="+linkedintoken+"&format=json", deadline=30.0, validate_certificate=True, method=urlfetch.GET).content ) 
   
        setusersname(currentuser, jsondata[u'firstName'], jsondata[u'lastName'])
        
    
    
    # if anything went wrong here, it's due to Linkedin
    except Exception as e:
        logging.error("Linkedin Login Failed: %s\n" % e)
        return redirect("/account#Linkedfailed")
  
    
    # Store linkedintoken in users account db
    updateaccountmodel(request, linkedintoken=linkedintoken, linkedinid=linkedinid, linkedinfriends=str( linkedinfriendslist ) )

 
    
    return redirect("/account")






# Handle twitter login.  A bit more complicated since it uses OAuth 1 (rest use version 2)
def twitterlogin(request):
    
    try:
        auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET, URL+"/twitterlogin")

        redirecturl = auth.get_authorization_url()

        # We need to store the request token in the session so it will be available after the user authorizes Hopku
        request.session["twitter_token"] = (auth.request_token.key, auth.request_token.secret)


    # If anything goes wrong here, it's because of Twitter
    except Exception as e:
        logging.error("Twitter login failed %s\n" % e)
        return redirect("/account#Twitterfail")

    # Redirect user to sign up page which will redirect to twitterhandler
    return redirect(redirecturl)




# Handle the twitter authorization
def twitterhandler(request):

    try:
    
        verifier = request.GET['oauth_verifier']

        auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
        token = request.session['twitter_token']

        del request.session["twitter_token"]

        auth.set_request_token(token[0], token[1])
        auth.get_access_token(verifier)


        api = tweepy.API(auth)
        
        twitterid = api.me().id
        username = api.me().screen_name


        currentuser = getcurrentuser(request)

        if currentuser.username == currentuser.first_name:
            setusersname(currentuser, username, "") 
        

        twitterfriendslist = fetchtwitterfriends(auth.access_token.key, auth.access_token.secret)

    
    except Exception as e:
        logging.error("Twitter login failed %s\n" % e)
        return redirect("/account#Twitterfail")

    
    # Store twitter credentials in database
    updateaccountmodel(request, twitterkey=auth.access_token.key, twittersecret=auth.access_token.secret, twitterid=twitterid, twitterfriends=str(twitterfriendslist) )


    return redirect("/account")





###############################################################################
# Helper functions
###############################################################################

# High Hits
# Returns a user object for the authenticated user (uses memcache)
def getcurrentuser(request):

    # fetch from memcache, if it's not there, pull from DB and then store in memcache

    # try fetching from memcache (letter is a namespace)
    currentuser = memcache.get("u"+str(request.user.pk))

    
    if currentuser is not None:
        return currentuser

        
    else:

        # get from DB and store in memcache
        currentuser = User.objects.get(pk=request.user.pk)
        memcache.set("u"+str(request.user.pk), currentuser)

        return currentuser



# High Hits
# Returns an account object for the authenticated user (uses memcache)
def getuseraccount(currentuser):

    # fetch from memcache, if it's not there, pull from DB and then store in memcache

    # try fetching from memcache (letter is a namespace)
    useraccount = memcache.get("a"+str(currentuser.id))


    if useraccount is not None:
        return useraccount
    
    
    else:

        # otherwise, get from DB and store in memcache
        useraccount = models.Accounts.objects.get(user=currentuser)
        memcache.set("a"+str(currentuser.id), useraccount)

        return useraccount





# Helper to modify the users account (model.Account) (must update memcache)
def updateaccountmodel(request, **kwargs):

    models.Accounts.objects.filter(user__pk__exact=request.user.pk).update(**kwargs)
    

    # Update memcache for this user
    memcache.delete("a"+str(request.user.pk))




# High Hits
# gets friend field from account based on field provided
def getfriends(account, field):

    # For some reason, eval is super fast here
    return eval( "list("+ account.__dict__[field] +")" )




# gets facebook friends from FB
def fetchfacebookfriends(accesstoken, mycsrf, request):
    
    response = urlfetch.fetch(url="https://graph.facebook.com/me/friends?access_token="+accesstoken, deadline=5.0, validate_certificate=True, method=urlfetch.GET).content
                            
    # if the response contains an error message, we need to handle it appropriately
    code = 0
    try:
                
        code = int(json.loads(response)["error"]["code"])
        if code == 190:
                            
            csrf = mycsrf 
            return render(request, "reauthorize.html", {"facebook": True, "mycsrf": csrf})
                        
        # an error, but a different kind 
        else:
            raise urlfetch.Error()

    # No error
    except KeyError:
        pass

                
    facebookfriendslist = (json.loads(response))["data"]


    # Check if result is paginated (more info left)
    more = True

    while more:

        more = json.loads(response).get("paging", None).get("next", None)

        if more:
            response = urlfetch.fetch(url=more+"&access_token="+accesstoken, deadline=5.0, validate_certificate=True, method=urlfetch.GET).content 
            data = json.loads(response)["data"] 
            if data:
                facebookfriendslist.extend( data )

            
    # Get a list of their facebook id's
    facebookfriendidlist = []
        
    for friend in facebookfriendslist:
        # Leave as unicode since db strings are in it
        facebookfriendidlist.append(friend[u'id'])

    
    return facebookfriendidlist







# gets linkedin friends from In
def fetchlinkedinfriends(linkedintoken, mycsrf, request):
    
    response = urlfetch.fetch(url="https://api.linkedin.com/v1/people/~/connections:(id)?oauth2_access_token="+linkedintoken+"&format=json", deadline=5.0, validate_certificate=True, method=urlfetch.GET)

            
    # if the response is an error, we need to handle it
    if int(response.status_code) == 401:
                
        csrf = mycsrf 
        return render(request, "reauthorize.html", {"linkedin": True, "mycsrf": csrf})  

            
    connections = json.loads(response.content)

    # We need to use pagination 
    if connections[u'_total'] >= 500:
        count = 1
                    

        while True:

            response = json.loads( urlfetch.fetch(url="https://api.linkedin.com/v1/people/~/connections:(id)?oauth2_access_token="+linkedintoken+"&start="+str(count*500)+"&format=json", deadline=5.0, validate_certificate=True, method=urlfetch.GET).content )

            connections[u'values'].extend(response[u'values'])

            count = count + 1

            if response[u'_total'] < 500:
                break
                        

    linkedinfriendslist = []
    for entry in connections[u"values"]:
        if not (entry[u'id'] == u'private'):
            linkedinfriendslist.append(entry[u'id'])
        
    
    return linkedinfriendslist







# gets twitter friends from twitter
def fetchtwitterfriends(twitterkey, twittersecret):
    
    auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
    auth.set_access_token(twitterkey, twittersecret)
            
    api = tweepy.API(auth)
    
    screenname = api.me().screen_name
    twitterfriendslist = []
    
                
    for friend in tweepy.Cursor( api.friends_ids, screen_name=screenname ).items():
        twitterfriendslist.append(str(friend))

    
    return twitterfriendslist






# set the first and last name of a user
def setusersname(currentuser, first, last):

    currentuser.first_name = first 
    currentuser.last_name = last

    currentuser.save()


    # Update memcache for this user
    memcache.delete("u"+str(currentuser.id) )

    



# convert duration string to a number
def durationtonumber(period):

    durtonumhash = {"Couple of Days": 0, "About a Week": 1, "Couple of Weeks": 2, "About a Month": 3, "Couple of Months": 4, "About a Year": 5, "Couple of Years": 6, "Few Days Ago": 0, "About a Week Ago": 1, "Few Weeks Ago": 2, "About a Month Ago": 3, "Few Months Ago": 4, "About a Year Ago": 5, "Few Years Ago": 6}
    

    return durtonumhash[period]
    


