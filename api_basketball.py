import pandas as pd
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def equipos():
    url = "https://api-basketball.p.rapidapi.com/teams"

    querystring = {"league":"12","season":"2022-2023"}

    headers = {
        "X-RapidAPI-Key": "4261bdd672msha1cdce9d40cda4cp19be08jsndc19601c3046",
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }
    id = {}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()["response"]
    string = ""
    for i in range(len(data)):
        string += "\t- "
        string += data[i]["name"] + "\n"
        id[data[i]["name"]] = data[i]["id"]
    print(string)
    return id


def get_stats(id: int):
    url = "https://api-basketball.p.rapidapi.com/statistics"

    querystring = {"season": "2022-2023", "league": "12", "team": str(id)}

    headers = {
        "X-RapidAPI-Key": "4261bdd672msha1cdce9d40cda4cp19be08jsndc19601c3046",
        "X-RapidAPI-Host": "api-basketball.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    teamstats_json = response.json()["response"]
    dict_games = {"Place": ["Home", "Away"], "draws": [0, 0], "loses": [0, 0], "wins": [0, 0]}
    dict_points = {"Place": ["Home", "Away"], "Average For": [0, 0], "Average Against": [0, 0]}
    games, points = teamstats_json["games"], teamstats_json["points"]
    for kind in games:
        if kind != "played":
            for place in games[kind]:
                if place == "away":
                    dict_games[kind][1] = games[kind][place]["percentage"]
                elif place == "home":
                    dict_games[kind][0] = games[kind][place]["percentage"]

    for place in points:
        for kind in points[place]["average"]:
            if kind == "home":
                if place == "against":
                    dict_points["Average Against"][0] = points[place]["average"][kind]
                elif place == "for":
                    dict_points["Average For"][0] = points[place]["average"][kind]
            elif kind == "away":
                if place == "against":
                    dict_points["Average Against"][1] = points[place]["average"][kind]
                elif place == "for":
                    dict_points["Average For"][1] = points[place]["average"][kind]

    df_games = pd.DataFrame.from_dict(dict_games)
    df_games.rename(columns={"draws": "% Draws", "loses": "% Loses", "wins": "% Wins"}, inplace=True)
    df_points = pd.DataFrame.from_dict(dict_points)
    return df_games, df_points

if __name__ == "__main__":
    pass
