import requests
from bs4 import BeautifulSoup
import itertools

import praw
import pandas as pd

def get_stories(folder,url):
    url = url
    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.content)
        title = soup.find('title').text.replace('– ','').replace(' ', '_')
        headers = list(soup.find_all('strong'))
        head_list = [item.get_text(strip = True) for item in headers]
        head_list = [item.replace(':', '') for item in head_list]
        story_list = [''.join(item.get_text().split(':')[1:]).replace('\xa0', '') for item in soup.find_all('p')]
        story_list = [item for item in story_list if item]
        story_tuple = list(zip(head_list, story_list))
        full_story_string = ' '.join(list(itertools.chain(*story_tuple)))
        if title.startswith('My') or title.startswith('Our'):
            with open("{}/{}.txt".format(folder,title), 'a') as write_file:
                write_file.write(full_story_string)
        if soup.findChild(class_="nav-previous") is not None:
            url = soup.findChild(class_="nav-previous").a.get('href')
        else:
            break


def reddit_scrape(folder,client_id, client_secret, user_agent):
    reddit = praw.Reddit(client_id=client_id, 
                         client_secret=client_secret, 
                         user_agent=user_agent)

    mt_sub = reddit.subreddit('MeToo')

    posts = []
    for post in mt_sub.search('flair_name:"Personal"', limit = None):
        if post.selftext is not '':
            posts.append([post.id, post.title, post.selftext])

    df_posts = pd.DataFrame(posts, columns = ['id', 'title', 'body'])

    sp_posts = []
    for post in mt_sub.search('flair_name:"Serious/Personal"', limit = None):
        if post.selftext is not '':
            sp_posts.append([post.id, post.title, post.selftext])

    df_sp_posts = pd.DataFrame(sp_posts, columns = ['id', 'title', 'body'])

    df_personal = pd.concat([df_posts, df_sp_posts], ignore_index=True)

    df_personal = df_personal.drop_duplicates(subset='id')

    for ind in list(range(0,len(df_personal))):
        with open("{}/{}.txt".format(folder,df_personal.id[ind]), 'a') as write_file:
            write_file.write("{} {}".format(str(df_personal.title[ind]), str(df_personal.body[ind])))