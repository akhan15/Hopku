from django.conf.urls import patterns, include, url
from view import *



urlpatterns = patterns('',


###############################################################################
# Mappers for each page of the app 
###############################################################################

    url(r'^$', homepage),

    url(r'^signup$', signup),

    url(r'^home$', searchpage),
    
    url(r'^learnmore$', learnmore),

    url(r'^businesses$', biz),    

    url(r'^privacy$', privacy),

    url(r'^tos$', tos),

    url(r'^account$', account),

    url(r'^sample$', sample),
      
    url(r'^write$', write),

    url(r'^contact$', contact),

    # show the users reviews
    url(r'^myreviews$', myreviews),


    # more pages of users reviews
    url(r'^myreviews/(?P<page>\d+)$', myreviews),

    
    # Handle reviews
    url(r'^review/(?P<reviewtype>\w+)/(?P<number>\d+)$', readreview),




   

###############################################################################
# Mappers for actions and dynamic content 
############################################################################### 
    

    # When the user tries to login from the homepage
    url(r'^login$', hopkulogin),


    # When the user wants to update their account info
    url(r'^updateaccount$', updateaccount),


    # When the user wants to register for the app
    url(r'^register$', register),


    # When the user submits a review
    url(r'^submitreview$', review),


    # Handle facebook login
    url(r'^facebookhandler$', facebooklogin),


    
    # Handle linkedin login
    url(r'^linkedinhandler$', linkedinlogin),


    # Handler twitter start
    url(r'^twitterstart$', twitterlogin),

    
    # Handle twitter process
    url(r'^twitterlogin$', twitterhandler),


    # Handle search query
    url(r'^search$', search),


    # Handle more pages of search
    url(r'^search/(?P<page>\d+)$', search),


  
    # Handle logout
    url(r'^logout$', hopkulogout),


    # update a review
    url(r'^updatereview/(?P<reviewtype>\w+)/(?P<number>\d+)$', updatereview),


    # user contacts us
    url(r'^contactemail', usercontact),


    # delete the users account
    url(r'^deleteaccount', deleteaccount),





    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
