# Generated by Django 4.1.4 on 2023-01-10 18:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_auction_listings_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]