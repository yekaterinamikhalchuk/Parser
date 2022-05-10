import requests
from bs4 import BeautifulSoup
import json

from celery import shared_task
from .models import News


@shared_task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            print(article)
            print(type(article))
            News.objects.create(
                link=article['link'],
                domain=article['domain'],
                create_date=article['create_date'],
                update_date=article['update_date'],
                country=article['country'],
                is_dead=article['is_dead'],
                a=article['a'],
                ns=article['ns'],
                cname=article['cname'],
                mx=article['mx'],
                txt=article['txt']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')


@shared_task
def hackernews_rss(url):
    article_list = []
    try:
        
        print('Starting the Scrapping tool')
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='lxml')
        container = soup.select('a')
        url_storage = []
        for block in container:
            try:
                print(5)
                url1 = block.get('href')
                print(url1)
                print(6)
                if url1.startswith('http'):
                    url_storage.append(url1)
            except:
                continue
        for link in url_storage:
            print(7)
            r = requests.get(f'https://api.domainsdb.info/v1/domains/search?domain={link}')
            print(8)
            data = r.text
            print(9)
            parse_json = json.loads(data)
            print(10)
            for block in parse_json['domains']:
                domain = block['domain']
                create_date = block['create_date']
                update_date = block['update_date']
                country = block['country']
                is_dead = block['isDead']
                a = block['A']
                ns = block['NS']
                cname = block['CNAME']
                mx = block['MX']
                txt = block['TXT']
                article = {
                    'domain': domain,
                    'link': link,
                    'create_date': create_date,
                    'update_date': update_date,
                    'country': country,
                    'is_dead': is_dead,
                    'a': a,
                    'ns': ns,
                    'cname': cname,
                    'mx': mx,
                    'txt': txt
                }
                print(article)
                article_list.append(article)
            print('Finished scraping the articles')
            return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)