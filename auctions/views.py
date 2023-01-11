from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, auction_listings, Bids, Comments, Category


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        active = auction_listings.objects.filter(Active=True)
        category = Category.objects.all()
        return render(request, "auctions/index.html", {
            "active": active,
            "categories": category
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["Bid"]
        url = request.POST["img"]

        category = request.POST["category"]
        categoryData = Category.objects.get(category=category)

        user = request.user

        bid = Bids(bid=float(price), user_id=user)
        bid.save()

        new = auction_listings(item=title, description=description, price=bid, url=url, category=categoryData, user_id=user)
        new.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        category = Category.objects.all()
        return render(request, "auctions/new.html", {
            "categories": category
        })

def category(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        if request.method == 'POST':
            formCategory = request.POST['category']
            catsearch = Category.objects.get(category=formCategory)
            active = auction_listings.objects.filer(Active=True, category=catsearch)
            category = Category.objects.all()
            return render(request, "auctions/index.html", {
                "active": active,
                "category": category
            })

def listing(request, id):
    listings = auction_listings.objects.get(pk=id)
    InWatchlist = request.user in listings.watchlist.all()
    comments = Comments.objects.filter(item=listings)
    isOwner = request.user.username == listings.user_id.username
    return render(request, "auctions/listing.html", {
        "listing": listings,
        "watchlist": InWatchlist,
        "comments": comments,
        "isOwner": isOwner
    })

def removeWatchlist(request, id):
    listingData = auction_listings.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))      

def addWatchlist(request, id):
    listingData = auction_listings.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id, )))  

def displayWatchlist(request):
    currentUser = request.user
    watchlistData = currentUser.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": watchlistData
    })

def addComment(request, id):
    currentUser = request.user
    listingData = auction_listings.objects.get(pk=id)
    message = request.POST["newComment"]

    newComment = Comments(
        user_id=currentUser,
        item = listingData,
        comment = message
    )

    newComment.save()
    
    return HttpResponseRedirect(reverse("listing", args=(id, )))  

def addBid(request, id):
    newBid = request.POST['newBid']
    listingData = auction_listings.objects.get(pk=id)
    InWatchlist = request.user in listingData.watchlist.all()
    comments = Comments.objects.filter(item=listingData)

    isOwner = request.user.username == listingData.user_id.username

    if int(newBid) > listingData.price.bid:
        updateBid = Bids(user_id=request.user, bid=newBid)
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Bid Updated",
            "update": True,
            "watchlist": InWatchlist,
            "comments": comments,
            "isOwner": isOwner
        })
    else:
        return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Bid Failed",
            "update": False,
            "watchlist": InWatchlist,
            "comments": comments,
            "isOwner": isOwner
        })

def removeAuction(request, id):
    listingData = auction_listings.objects.get(pk=id)
    listingData.Active = False
    listingData.save()

    InWatchlist = request.user in listingData.watchlist.all()
    comments = Comments.objects.filter(item=listingData)

    
    isOwner = request.user.username == listingData.user_id.username

    return render(request, "auctions/listing.html", {
            "listing": listingData,
            "message": "Auction Closed",
            "update": True,
            "watchlist": InWatchlist,
            "comments": comments,
            "isOwner": isOwner
        })