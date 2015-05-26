from django.db import models
from django.contrib.auth.models import User


# The models for reviews


# These classes were poorly designed.  Seperate classes should have been made for Products and 
# Services from which all the others would inherit.  All of this duplication and using 'P' and
# 'S' to indicate products and services are textbook design mistakes


class PApparel(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    zipcode = models.PositiveIntegerField(default=None)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]

class PVehicles(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PBaby(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PBeauty(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]

class PElectronics(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PFood(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)

    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PHome(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PMedia(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]



class PNovelty(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class POffice(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PSoftware(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]


class PSports(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]




class POther(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['-duration']

        index_together = [[ "facebookid", "twitterid" ]]




class SBars(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']
    
        index_together = [[ "facebookid", "twitterid" ]]


class SBeauty(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]




class SChild(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SCleaning(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SEducational(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SFinancial(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SFitness(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]



class SHealthcare(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SIT(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]



class SLegal(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]



class SLive(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")

    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SCreative(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SReal(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SRepair(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SRestaurants(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]

class SSports(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SStores(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]



class STravel(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]


class SWeb(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]



class SOther(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    zipcode = models.PositiveIntegerField(default=None)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    class Meta:

        ordering = ['duration']

        index_together = [[ "facebookid", "twitterid" ]]



class EArts(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]




class ECharity(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]




class EEntertainment(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']


        index_together = [[ "facebookid", "twitterid" ]]






class EFood(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]




class EHoliday(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]





class ESocial(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]




class ESports(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]




class EOther(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=100)
    facebookid = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    name = models.CharField(max_length=200)
    duration = models.SmallIntegerField(default=0)
    description = models.CharField(max_length=1000)
    stars = models.CharField(max_length=50)
    reviewtext = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=1500, default="")
    mediaurls = models.TextField(default="")
    zipcode = models.PositiveIntegerField(default=None)
    class Meta:

        ordering = ['date']

        index_together = [[ "facebookid", "twitterid" ]]






# The model for the users accounts
class Accounts(models.Model):
    user = models.OneToOneField(User)
    mycsrf = models.CharField(max_length=50)
    zipcode = models.PositiveIntegerField(default=100000)
    facebookid = models.CharField(max_length=500, default="")
    facebooktoken = models.CharField(max_length=500, default="")
    linkedinid = models.CharField(max_length=500, default="")
    linkedintoken = models.CharField(max_length=500, default="")
    twitterid = models.CharField(max_length=500, default="")
    twitterkey = models.CharField(max_length=500, default="")
    twittersecret = models.CharField(max_length=500, default="")
    facebookfriends = models.TextField(default="")
    linkedinfriends = models.TextField(default="")
    twitterfriends = models.TextField(default="")
    hopkufriends = models.TextField(default="")
    netupdate = models.CharField(max_length=200, default="") 

    class Meta:

        index_together = [["user"]]
