import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', djangofilter_demo.setting)
import django 
django.setup()

import random

from core.models import Book
from faker import Faker

fakegen = Faker()

def populate(N=5):
    fake = Faker()
    for i in range(50):
        names = [the_fake.unique.name()]
        author = random.randint(1,4)
        title = [the_fake.unique.name()]
        status = random.chioce(['punlished', 'draft'])
