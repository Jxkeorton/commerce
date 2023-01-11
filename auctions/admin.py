from django.contrib import admin
from .models import auction_listings, User, Bids, Comments, Category

# Register your models here.
admin.site.register(auction_listings)
admin.site.register(User)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Category)