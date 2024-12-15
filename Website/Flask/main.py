from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

def fetch_live_scores():
    url = "https://api.sofascore.com/api/v1/sport/football/events/live"
    headers = {"authority": "api.sofascore.com"}
    response = requests.get(url, headers=headers)
    data = response.json()
    matches = []

    for match in data.get('events', []):
        matches.append({
            "id": match['id'], 
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
    url = f"https://api.sofascore.com/api/v1/event/{match_id}/lineups"  
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Extract players and positions
        home_team_players = []
        away_team_players = []

        if 'home' in data and 'players' in data['home']:
            home_team_players = [
                {"name": player['player']['name'], "position": player.get('position', 'Unknown')}
                for player in data['home']['players']
            ]
        if 'away' in data and 'players' in data['away']:
            away_team_players = [
                {"name": player['player']['name'], "position": player.get('position', 'Unknown')}
                for player in data['away']['players']
            ]

        return jsonify({
            "home": {"players": home_team_players},
            "away": {"players": away_team_players}
        })

    return jsonify({"error": "Match details not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


