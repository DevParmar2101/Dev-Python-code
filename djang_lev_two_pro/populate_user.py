import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','djang_lev_two_pro.settings')

import django
django.setup()

import random
from djan_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_First_name = fake_name[0]
        fake_Second_name = fake_name[0]
        fake_email = fakegen.email()

        # New ENTRY
        user = User.objects.get_or_create(First_Name=fake_First_name,
                                          Second_Name=fake_Second_name,
                                          E_mail=fake_email)

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(50)
    print("COMPLETE")
