import requests
from bs4 import BeautifulSoup
import csv
import os
import logging

ESPN_URL = 'https://www.espncricinfo.com/live-cricket-score'

def fetch_live_score():
    try:
        response = requests.get(ESPN_URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            team1_name = soup.find_all(class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')[0].text.strip()
            team2_name = soup.find_all(class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')[1].text.strip()
            match_date = soup.find(class_='ds-text-tight-xs ds-truncate ds-text-typo-mid3').text.strip()
            match_status = soup.find(class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo').text.strip()
            live_score_info = f"**Team1:** {team1_name}\n"\
                              f"**Team2:** {team2_name}\n" \
                              f"**Details:** {match_date}\n" \
                              f"**Status:** {match_status}"
            append_to_csv([team1_name, team2_name, match_date, match_status])
            return live_score_info
        else:
            return "Failed to fetch live score."
    except Exception as e:
        logging.error(f"Error : {str(e)}")
        return "Failed to fetch live score."

def fetch_match_history():
    try:
        with open('match_history.csv', 'r') as file:
            lines = file.readlines()
        return ''.join(lines)
    except FileNotFoundError:
        with open('match_history.csv', 'w') as file:
            pass
        return "No match history available."

def append_to_csv(data):
    try:
        with open('match_history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    except Exception as e:
        logging.error(f"Error : {str(e)}")
