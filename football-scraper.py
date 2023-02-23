# Imports
# -----------------------------------
import requests
import pandas as pd
from fuzzywuzzy import process
# ---------------------------------------------
# Setting up connection to the football API
url = 'http://api.football-data.org/v4/competitions/PL/teams' # gathers teams from the prem
# Headers to access the API
headers = {'X-Auth-Token': 'Add-API-key-here'}
# Grabbing the response from the API
response = requests.get(url, headers=headers)
# ----------------------------------------------------------------------
# Setting up variables to store team data
team_dict = {}
team_id = 0

# Collecting the teams are assinging IDs
for i in range(len(response.json()['teams'])):
    team_dict[response.json()['teams'][i]['name']] = team_id
    team_id += 1
# ----------------------------------------------------------------------
# Asking the user to input thier premier league team
team_input = input('Input your Premier League football team here: ')

# Using fuzzy match to deal with any inaccuracies when inputting
best_match, score = process.extractOne(team_input, [tup for tup in team_dict.keys()])
# ----------------------------------------------------------------------
# Ensure the team inputted is somewhat valid 
if score < 50:
    print('\nTeam you inputted has not been found.')
else:
    # Preparing data to be store in a data frame
    player_names = []
    position_list = []
    nationality_list = []

    for j in range(len(response.json()['teams'][team_dict[best_match]]['squad'])):
        player_names.append(response.json()['teams'][team_dict[best_match]]['squad'][j]['name'])
        position_list.append(response.json()['teams'][team_dict[best_match]]['squad'][j]['position'])
        nationality_list.append(response.json()['teams'][team_dict[best_match]]['squad'][j]['nationality'])
    # ----------------------------------------------------------------------
    # Creating the dataframe
    team_df = pd.DataFrame({'Player Name':player_names, 'Position':position_list,'Nationality':nationality_list})
    # Printing the dataframe
    print(f"\nYou have chosen the team {best_match} here is the squad list:\n\n",team_df)

