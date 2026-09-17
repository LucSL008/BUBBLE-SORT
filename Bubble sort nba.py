import pandas as pd

df = pd.read_csv("games.csv")
df2 = pd.read_csv("teams.csv")
season = df[df['SEASON'] == 2022].copy()
season['TOTAL_POINTS'] = season['PTS_home'] + season['PTS_away']
sample = season[['GAME_DATE_EST', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'TOTAL_POINTS']].head(500).to_dict(orient='records')
#buscar en el archivo teams el equipo en funcion de su id del archivo games


def bubble_sort(arr, key): #por favor funciona
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] < arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

puntos_sorteados = bubble_sort(sample, "TOTAL_POINTS")
df['HOME_TEAM_ID'] = df2['TEAM_ID']
df['VISITOR_TEAM_ID'] = df2['TEAM_ID']
name = df2[df2['NICKNAME']]
for g in puntos_sorteados[:10]:
    print(f"{g['GAME_DATE_EST']}: {g['HOME_TEAM_ID']} vs {g['VISITOR_TEAM_ID']}  Total: {g['TOTAL_POINTS']}")

print("Top 10 juegos:")
for g in puntos_sorteados[:10]:
    print(g)