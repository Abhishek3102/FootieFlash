# from flask import Flask, jsonify, render_template, request
# import requests

# app = Flask(__name__)

# def fetch_live_scores():
#     url = "https://api.sofascore.com/api/v1/sport/football/events/live"
#     headers = {
#         "authority": "api.sofascore.com"
#     }
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     matches = []

#     for match in data.get('events', []):
#         matches.append({
#             "league": match['tournament']['name'],
#             "homeTeam": match['homeTeam']['name'],
#             "awayTeam": match['awayTeam']['name'],
#             "homeScore": match['homeScore']['current'],
#             "awayScore": match['awayScore']['current']
#         })

#     return matches

# @app.route('/api/live-scores', methods=['GET'])
# def live_scores_api():
#     matches = fetch_live_scores()
#     return jsonify({"matches": matches})

# @app.route('/')
# def live_scores_page():
#     matches = fetch_live_scores()
#     return render_template('scores.html', matches=matches)

# @app.route('/match/<match_id>', methods=['GET'])
# def get_match_details(match_id):
#     url = f"https://api.sofascore.com/api/v1/event/{match_id}/lineups"  # Example endpoint
#     response = requests.get(url)
#     if response.status_code == 200:
#         return jsonify(response.json())
#     return jsonify({"error": "Match details not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

def fetch_live_scores():
    url = "https://api.sofascore.com/api/v1/sport/football/events/live"
    headers = {
        "authority": "api.sofascore.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = []

    for match in data.get('events', []):
        matches.append({
            "match_id": match['id'],  # Store match ID to use later for detailed info
            "league": match['tournament']['name'],
            "homeTeam": match['homeTeam']['name'],
            "awayTeam": match['awayTeam']['name'],
            "homeScore": match['homeScore']['current'],
            "awayScore": match['awayScore']['current']
        })

    return matches

@app.route('/api/live-scores', methods=['GET'])
def live_scores_api():
    matches = fetch_live_scores()
    return jsonify({"matches": matches})

@app.route('/')
def live_scores_page():
    matches = fetch_live_scores()
    return render_template('scores.html', matches=matches)

@app.route('/match/<match_id>', methods=['GET'])
def get_match_details(match_id):
    url = f"https://api.sofascore.com/api/v1/event/{match_id}/lineups"  # Sofascore lineups API
    response = requests.get(url)
    if response.status_code == 200:
        match_data = response.json()
        # Extract home and away player lineups
        home_players = match_data.get('home', {}).get('players', [])
        away_players = match_data.get('away', {}).get('players', [])
        
        match_details = {
            'home': {
                'team': match_data.get('home', {}).get('team', {}).get('name', 'Unknown'),
                'players': [{'name': player['name'], 'position': player['position']} for player in home_players]
            },
            'away': {
                'team': match_data.get('away', {}).get('team', {}).get('name', 'Unknown'),
                'players': [{'name': player['name'], 'position': player['position']} for player in away_players]
            }
        }
        return jsonify(match_details)
    return jsonify({"error": "Match details not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
