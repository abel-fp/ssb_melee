#!/usr/bin/env python 3

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import requests
import os

html_folder = 'html_source_files'

html_files = ['top-players.html',
              'List_of_national_tournaments.html',
              'melee.2.html',
              'SSBMRank.html']

# I need to change somethings - git commit

def top_players_df():
    # let's create the data for the first item in the above list: top players
    top_players_list = []
    with open(os.path.join(html_folder, html_files[0])) as file:
        soup = BeautifulSoup(file, 'lxml')

        for player in soup.find_all('tr', class_='format_row highlight')[0:100]:
            data_raw = [data for data in player.stripped_strings]

            ranking = int(data_raw[0][0:-1])
            tag = data_raw[1]
            name = data_raw[2]
            country = player.find('img').get('title')
            tot_game = float(data_raw[3][1:].replace(',', ''))
            tot_overall = float(data_raw[5][1:].replace(',', ''))
            percent_of_tot = tot_game / tot_overall * 100

            top_players_list.append({'ranking': ranking,
                                     'tag': tag,
                                     'name': name,
                                     'country': country,
                                     'tot_game': tot_game,
                                     'tot_overall': tot_overall,
                                     'percent_of_tot': percent_of_tot})

    top_players = pd.DataFrame(top_players_list, columns=['ranking', 'tag', 'name', 'country',
                                                          'tot_game', 'tot_overall', 'percent_of_tot'])

    return top_players


def tournaments():
    tourney_list = []
    with open(os.path.join(html_folder, html_files[1])) as file:
        soup = BeautifulSoup(file, 'lxml')


def melee_two_df():
    melee_two_list = []
    with open(os.path.join(html_folder, html_files[2])) as file:
        soup = BeautifulSoup(file, 'lxml')

        for info in soup.find_all('div', class_="torneo-row")[1:51]:
            print([char for char in info.stripped_strings])


if __name__ == '__main__':
    # a = top_players_df()
    # a.country.value_counts().plot.bar(title='Country of Origin of Top 100 Players')
    # plt.show()
    melee_two_df()
