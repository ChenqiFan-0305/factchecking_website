import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scientific_rating.settings")

import django
django.setup()

from django.core.management import call_command

import pandas as pd
import numpy as np
from sim_rating.models import Link, Topic, Source, Article



def link():
    link_data = pd.read_csv("link.csv")
    for row in range(len(link_data)):
        uniqno = link_data["UniqNO"][row]
        articleurl = link_data["articleurl"][row]
        status = link_data["status"][row]
        Link.objects.get_or_create(external_url=articleurl,status=status)

def topic():
    topic_data = pd.read_csv("topic.csv")
    for row in range(len(topic_data)):
        temp = topic_data["0"][row]
        Topic.objects.get_or_create(topic=temp)

def source():
    source_data = pd.read_csv("source.csv")
    for row in range(len(source_data)):
        temp = source_data["0"][row]
        Source.objects.get_or_create(source=temp)

def article():
    article_data=pd.read_csv("article.csv")
    for row in range(len(article_data)):
        link = Link.objects.get(external_url=article_data["articleurl"][row])
        title = article_data["title, original source"][row]
        topic = Topic.objects.get(topic=article_data["topic"][row])
        text = article_data["text"][row]
        display = article_data["html_text"][row]
        source = article_data["source"]
        #date_published = article_data["date"][row]
        Article.objects.get_or_create(link=link,title=title,topic=topic,text=text,display=display,source=source)#,date_published=date_published)

if __name__ == "__main__":
    link()
    print("Link Done!")
    topic()
    print("Topic Done!")
    source()
    print("Source Done!")
    article()
    print("Article Done!")                 