import requests
from bs4 import BeautifulSoup
import itertools


def get_stories():
    url = "https://metoostem.com/2019/05/22/my-name-is-ana/"
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
            with open("{}.txt".format(title), 'a') as write_file:
                write_file.write(full_story_string)
        if soup.findChild(class_="nav-previous") is not None:
            url = soup.findChild(class_="nav-previous").a.get('href')
        else:
            break