import requests
import json
url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = ""
headers = {
    "authority" : "api.sofascore.com"
}

response = requests.request("GET", url, data=payload, headers=headers)
jsondata = json.loads(response.text)



league = jsondata['events'][0]['tournament']['name']
hometeam = jsondata['events'][0]['homeTeam']['name']
awayteam = jsondata['events'][0]['awayTeam']['name']
hometeamscore = jsondata['events'][0]['homeScore']['current']
awayteamscore = jsondata['events'][0]['awayScore']['current']


for matches in jsondata['events']:
    league = matches['tournament']['name']
    hometeam = matches['homeTeam']['name']
    awayteam = matches['awayTeam']['name']
    hometeamscore = matches['homeScore']['current']
    awayteamscore = matches['awayScore']['current']
    print(league, "|", hometeam, hometeamscore,"-",awayteamscore, awayteam)
