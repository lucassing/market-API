from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
import os
from shop import models as modelShop

User = get_user_model()

Users = [
    {"username": "test1", "password": "123456", 'email': 'test4@gmail.com', },
    {"username": "test2", "password": "abcdef", 'email': 'test2@gmail.com', },
    {"username": "test3", "password": "ABCDEF", 'email': 'test3@gmail.com', }, ]
Categories = [{"name": "cellphones"}, {"name": "computer"}, {"name": "TV"}, ]


class Command(BaseCommand):
    help = 'Populate the database with some data'

    def handle(self, *args, **options):
        for user in Users:
            get_user_model().objects.get_or_create(**user)
        for category in Categories:
            modelShop.Category.objects.get_or_create(**category)


