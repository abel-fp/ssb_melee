#!/usr/bin/env python3

import requests
import os

# create the folder for the html source code
folder_path = 'html_source_files'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

urls = ['https://www.esportsearnings.com/games/204-super-smash-bros-melee/top-players',
        'https://smashboards.com/rankings/melee.2',
        'https://liquipedia.net/smash/SSBMRank',
        'https://www.ssbwiki.com/List_of_national_tournaments']

# create the html files from the urls
for url in urls:
    response = requests.get(url)
    with open(os.path.join(folder_path, url.split('/')[-1]) + '.html', mode='wb') as file:
        file.write(response.content)

# check that we got the files we wanted in the folder we created
print(os.listdir(folder_path))
