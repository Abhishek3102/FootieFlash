from flask import Flask, jsonify, render_template, request
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def fetch_live_scores():
    url = "https://api.sofascore.com/api/v1/sport/football/events/live"
    headers = {"authority": "api.sofascore.com"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        matches = []
        
        for match in data.get('events', []):
            match_details = {
                "id": match.get('id', 'Unknown'),
                "league": match.get('tournament', {}).get('name', 'Unknown'),
                "homeTeam": match.get('homeTeam', {}).get('name', 'Unknown'),
                "awayTeam": match.get('awayTeam', {}).get('name', 'Unknown'),
                "homeScore": match.get('homeScore', {}).get('current', 'N/A'),
                "awayScore": match.get('awayScore', {}).get('current', 'N/A')
            }
            
            if all(value != 'Unknown' for value in match_details.values()):
                matches.append(match_details)
        
        return matches
    
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON response")
        return []

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
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

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
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request error: {e}"}), 500
    except requests.exceptions.JSONDecodeError:
        return jsonify({"error": "Failed to decode JSON response"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
