from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta
from django.utils import timezone


class User(AbstractUser):
    pass


class Account(models.Model):
    account_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    barrel_count = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "account_owner_id": self.account_owner.id,
            "account_owner": self.account_owner.username,
            "barrel_count": self.barrel_count,
            "date_joined": self.account_owner.date_joined.strftime("%b %-d %Y"),
            "email": self.account_owner.email
        }

    def __str__(self):
        return f"{self.account_owner}"


class Alert(models.Model):
    alert_user = models.ForeignKey("User", on_delete=models.CASCADE)
    alert_timestamp = models.DateTimeField(
        default=datetime.now)
    alert_message = models.TextField(blank=True)
    alert_barrel = models.ForeignKey("Barrel", on_delete=models.CASCADE)
    alert_read = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "alert_user": self.alert_user.username,
            "alert_timestamp": self.alert_timestamp.strftime("%b %-d, %Y, %-I:%M %p"),
            "alert_message": self.alert_message,
            "alert_read": self.alert_read,
            "alert_barrel": self.alert_barrel.title,
            "alert_barrel_id": self.alert_barrel.id,
        }

    def __str__(self):
        return f"{self.alert_barrel} needs to be pulled soon!"
    # when user logs in, check if any barrels are on or past pull date. then 'send alert'


class Note(models.Model):
    note_author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    note_barrel = models.ForeignKey(
        "Barrel", on_delete=models.CASCADE)
    note_timestamp = models.DateTimeField(default=timezone.now)

    def serialize(self):
        return {
            "id": self.id,
            "note_author": self.note_author.username,
            "content": self.content,
            "note_barrel_title": self.note_barrel.title,
            "note_barrel": self.note_barrel.id,
            "note_timestamp": self.note_timestamp.strftime("%b %-d, %Y")
        }

    def __str__(self):
        return f"{self.note_author}'s note for: {self.note_barrel}"


class Barrel(models.Model):

    RED_WINE = 'Red Wine'
    WHITE_WINE = 'White Wine'
    BOURBON = 'Bourbon'
    RUM = 'Rum'
    GIN = 'Gin'
    WHISKEY = 'Whiskey'
    OTHER = 'Other'
    CATEGORY_CHOICES_BARREL = [
        (RED_WINE, 'Red Wine'),
        (WHITE_WINE, 'White Wine'),
        (BOURBON, 'Bourbon'),
        (RUM, 'Rum'),
        (GIN, 'Gin'),
        (WHISKEY, 'Whiskey'),
        (OTHER, 'Other'),
    ]

    SOUR = 'Sour'
    STOUT_PORTER = 'Stout_Porter'
    LAGER = 'Lager'
    BELGIAN = 'Belgian'
    SPECIALTY = 'Specialty'
    CATEGORY_CHOICES_BEER_STYLES = [
        (SOUR, 'Sour'),
        (STOUT_PORTER, 'Stout_Porter'),
        (LAGER, 'Lager'),
        (BELGIAN, 'Belgian'),
        (SPECIALTY, 'Specialty'),
    ]

    owner = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="barrel_owners")
    title = models.CharField(max_length=64)
    beer_style = models.CharField(
        max_length=16, choices=CATEGORY_CHOICES_BEER_STYLES, default=STOUT_PORTER)
    barrel_category = models.CharField(
        max_length=16, choices=CATEGORY_CHOICES_BARREL, default=BOURBON)
    add_date = models.DateTimeField(
        default=timezone.now)
    fill_date = models.DateTimeField(
        default=timezone.now)
    estimated_ABV = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=256)
    pull_date = models.DateTimeField(
        default=datetime.now()+timedelta(days=180))
    archived = models.BooleanField(default=False)
    bookmarked = models.BooleanField(default=False)
    alert_off = models.BooleanField(default=False)
    # image field of a barrel by default

    def __str__(self):
        return f"{self.title}"

    def get_categories_barrel(self):
        return self.CATEGORY_CHOICES_BARREL

    def get_categories_beer_style(self):
        return self.CATEGORY_CHOICES_BEER_STYLES

    def serialize(self):
        return {
            "id": self.id,
            "barrel_owner": self.owner.username,
            "title": self.title,
            "estimated_ABV": self.estimated_ABV,
            "description": self.description,
            "beer_style": self.beer_style,
            "barrel_category": self.barrel_category,
            "add_date": self.add_date.strftime("%b %-d, %Y"),
            "fill_date": self.fill_date.strftime("%b %-d, %Y"),
            "pull_date": self.pull_date.strftime("%b %-d, %Y"),
            "archived": self.archived,
            "bookmarked": self.bookmarked,
            "alert_off": self.alert_off
        }

    def __str__(self):
        return f"{self.owner}'s Barrel: {self.title}"
