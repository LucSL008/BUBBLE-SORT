import pandas as pd
df = pd.read_csv("games.csv")
df2 = pd.read_csv("teams.csv")
season = df[df['SEASON'] == 2022]
season['TOTAL_POINTS'] = season['PTS_home'] + season['PTS_away']
sample = season[['GAME_DATE_EST', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'TOTAL_POINTS']].head(500)
sorted_games = sample.sort_values(by='TOTAL_POINTS', ascending=False)
print(sorted_games.head())