import requests
def obtener_datos_nba():
    url = "https://www.kaggle.com/datasets/nathanlauga/nba-games"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener los datos de la NBA.")
        return []
def bubble_sort(arr, key): #por favor funciona
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][key] < arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
sample = obtener_datos_nba()
sorted_games = bubble_sort(sample, 'TOTAL_POINTS')
for g in sorted_games[:10]:
    print(f"{g['GAME_DATE']}: {g['HOME_TEAM']} {g['HOME_PTS']} -"
          f" {g['AWAY_TEAM']} {g['AWAY_PTS']}"
          f" (Total: {g['TOTAL_POINTS']})")

