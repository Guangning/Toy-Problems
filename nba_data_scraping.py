#!/usr/bin/python

import os
import requests
from datetime import datetime, date
from bs4 import BeautifulSoup

def get_the_teams():

    print "> Get the teams..."

    url = 'http://espn.go.com/nba/teams'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    team_list = []
    regions = soup.find_all('ul', class_='medium-logos')
    for region in regions:
        teams = region.find_all('li')
        for team in teams:
            info = team.h5.a
            team_name = info.text
            team_url = info['href']
            team_short_name1 = info['href'].split('/')[-2]
            team_short_name2 = info['href'].split('/')[-1]
            team_list.append([team_name, team_short_name1, team_short_name2, team_url])

    with open(TEAM_LIST, 'w') as output_file:
        for team in team_list:
            output_file.write(','.join(team) + '\n')


def get_the_games():

    print "> Get the games..."

    BASE_URL = 'http://espn.go.com/nba/team/schedule/_/name/{0}/year/{1}/{2}'

    year = 2015

    match_list = []
    with open(TEAM_LIST, 'rb') as team_list:
        for rec in team_list:
            team = rec.strip().split(',')
            this_team = team[1]
            team_game_url = BASE_URL.format(team[1],year,team[2])
            # Get the first table
            table = BeautifulSoup(requests.get(team_game_url).text, "lxml").table
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                try:
                    is_home = True if columns[1].find_all('li')[0].text == 'vs' else False
                    is_won = True if columns[2].find_all('li')[0].text == 'W' else False
                    other_team = columns[1].find_all('a')[0]['href'].split('/')[-2]
                    match_date = datetime.strptime(columns[0].text, '%a, %b %d')
                    score = columns[2].find_all('li')[1].text.split(' ')[0].split('-')
                    ot = columns[2].find_all('li')[1].text.split(' ')[1] if len(columns[2].find_all('li')[1].text.split(' ')) > 1 else ''
                    match_id = columns[2].find_all('li')[1].find_all('a')[0]['href'].split('?id=')[1]

                    home_team = this_team if is_home else other_team
                    visit_team = other_team if is_home else this_team

                    if is_home:
                        if is_won:
                            home_score = score[0]
                            visit_score = score[1]
                        else:
                            home_score = score[1]
                            visit_score = score[0]
                    else:
                        if is_won:
                            home_score = score[1]
                            visit_score = score[0]
                        else:
                            home_score = score[0]
                            visit_score = score[1]

                    if match_date.month >= 9:
                        match_dt = date(year-1, match_date.month, match_date.day)
                    else:
                        match_dt = date(year, match_date.month, match_date.day)

                    match_list.append([match_id, str(match_dt), home_team, visit_team, home_score, visit_score, ot])

                except Exception as e:
                    pass

    with open(MATCH_LIST, 'w') as output_file:
        for match in match_list:
            output_file.write(','.join(match) + '\n')


def get_the_boxscore(match_id):

    print "> Get the boxscore of game %s..." % match_id

    BASE_URL = 'http://espn.go.com/nba/boxscore?gameId={0}'
    url = BASE_URL.format(match_id)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    tables = soup.find_all('table', class_='mod-data')
    away_table = tables[0]
    home_table = tables[1]

    rows = away_table.find_all('tr')
    for row in rows:
        try:
            th = row.find_all('th')
            is_starter = True if th[0].text == 'starters' else False
        except Exception:
            pass

        try:
            td = row.find_all('td')
            player_name = td[0].find_all('a')[0].text
            player_id = td[0].find_all('a')[0]['href'].split('/')[-1]
            position = td[0].find_all('span')[0].text
            starter_ind = 'Y' if is_starter else 'N'
            min = td[1].text
            fg = td[2].text
            _3pt = td[3].text
            ft = td[4].text
            #td[5].text
            #td[6].text
            #td[7].text
            #td[8].text
            #td[9].text
            #td[10].text
            #td[11].text
            #td[12].text
            #td[13].text
            #td[14].text

            print player_id, player_name, position, starter_ind, min, fg, _3pt, ft

        except Exception:
            pass


if __name__ == '__main__':

    TEAM_LIST = '/home/devuser/Documents/scraper/team.csv'
    MATCH_LIST = '/home/devuser/Documents/scraper/match.csv'

    get_the_teams()
    get_the_games()
    get_the_boxscore('400578910','ny','no')
