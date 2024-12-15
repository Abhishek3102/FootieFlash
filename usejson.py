import json
with open('scores.json', encoding='utf-8') as f:
    jsondata = json.load(f)

league = jsondata['featuredEvents'][0]['tournament']['name']
hometeam = jsondata['featuredEvents'][0]['homeTeam']['name']
awayteam = jsondata['featuredEvents'][0]['awayTeam']['name']
hometeamscore = jsondata['featuredEvents'][0]['homeScore']['current']
awayteamscore = jsondata['featuredEvents'][0]['awayScore']['current']

# print(league, hometeam, awayteam, hometeamscore, awayteamscore)
# print(league, "|", hometeam, hometeamscore,"-",awayteamscore, awayteam)

for matches in jsondata['featuredEvents']:
    league = matches['tournament']['name']
    hometeam = matches['homeTeam']['name']
    awayteam = matches['awayTeam']['name']
    hometeamscore = matches['homeScore']['current']
    awayteamscore = matches['awayScore']['current']
    print(league, "|", hometeam, hometeamscore,"-",awayteamscore, awayteam)