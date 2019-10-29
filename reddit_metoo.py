import praw
import pandas as pd

def reddit_scrape(client_id, client_secret, user_agent):
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
        with open("reddit_metoo/{}.txt".format(df_personal.id[ind]), 'a') as write_file:
            write_file.write("{} {}".format(str(df_personal.title[ind]), str(df_personal.body[ind])))