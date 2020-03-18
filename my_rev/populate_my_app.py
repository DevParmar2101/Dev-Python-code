import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_rev.settings')

import django
django.setup()

##FAKER POP SCRIPT
import random
from my_app.models import AccessRecord,Topic,WebPage
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        print("THIS ARE THE URLS :----------"+fake_url)
        print("THIS ARE THE DATES:----------"+fake_date)
        print("THIS ARE THE NAMES:----------"+fake_name)
        print("=================================================================================")

        #Create a nre WebPage Entry
        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #Create a fake access record for that WebPage
        acc_rec =  AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate(30)
    print("popualting complete !")
