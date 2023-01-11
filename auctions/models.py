from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category

class Bids(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="userbid")
    bid = models.FloatField(default=0)

class auction_listings(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.CharField(max_length=65, null=False)
    description = models.CharField(max_length=150, null=False)
    price = models.ForeignKey(Bids, on_delete=models.CASCADE, blank=True, null=True, related_name="bids")
    url= models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="cat" )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user" )
    Active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, null=True, blank=True, related_name="watchlist")

    def __str__(self):
        return self.item

class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="usercomment")
    item = models.ForeignKey(auction_listings, on_delete=models.CASCADE, blank=True, null=True, related_name="listing")
    comment = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user_id} comment on {self.item}"