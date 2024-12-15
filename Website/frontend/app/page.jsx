// 'use client';

// import { useEffect, useState } from 'react';
// import axios from 'axios';
// import './styles.css';

// export default function Home() {
//   const [matches, setMatches] = useState([]);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const fetchScores = async () => {
//       try {
//         const response = await axios.get('http://127.0.0.1:5000/api/live-scores');
//         setMatches(response.data.matches);
//       } catch (error) {
//         console.error("Error fetching live scores:", error);
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchScores();
//   }, []);

//   if (loading) {
//     return <div className="loading">Fetching live scores...</div>;
//   }

//   if (matches.length === 0) {
//     return <div className="no-matches">No live matches available right now.</div>;
//   }

//   // Group matches by leagues
//   const groupedByLeague = matches.reduce((acc, match) => {
//     acc[match.league] = acc[match.league] || [];
//     acc[match.league].push(match);
//     return acc;
//   }, {});

//   return (
//     <div className="container">
//       <h1>Live Football Scores</h1>
//       {Object.keys(groupedByLeague).map((league, index) => (
//         <div key={index} className="league-section">
//           <h2 className="league-name">{league}</h2>
//           <div className="cards-container">
//             {groupedByLeague[league].map((match, matchIndex) => (
//               <div key={matchIndex} className="match-card">
//                 <div className="team">
//                   <h3 className="team-name">{match.homeTeam}</h3>
//                   <div className="team-score">{match.homeScore}</div>
//                 </div>
//                 <div className="versus">vs</div>
//                 <div className="team">
//                   <h3 className="team-name">{match.awayTeam}</h3>
//                   <div className="team-score">{match.awayScore}</div>
//                 </div>
//               </div>
//             ))}
//           </div>
//         </div>
//       ))}
//     </div>
//   );
// }


'use client';

import { useEffect, useState } from 'react';
import axios from 'axios';
import './styles.css';

export default function Home() {
  const [matches, setMatches] = useState([]);
  const [matchDetails, setMatchDetails] = useState(null);
  const [selectedMatchId, setSelectedMatchId] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchScores = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/live-scores');
        setMatches(response.data.matches);
      } catch (error) {
        console.error("Error fetching live scores:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchScores();
  }, []);

  const fetchMatchDetails = async (matchId) => {
    setSelectedMatchId(matchId);
    const res = await fetch(`http://localhost:5000/match/${matchId}`);
    if (res.ok) {
      const data = await res.json();
      setMatchDetails(data);
    }
  };

  if (loading) {
    return <div className="loading">Fetching live scores...</div>;
  }

  if (matches.length === 0) {
    return <div className="no-matches">No live matches available right now.</div>;
  }

  const groupedByLeague = matches.reduce((acc, match) => {
    acc[match.league] = acc[match.league] || [];
    acc[match.league].push(match);
    return acc;
  }, {});

  return (
    <div className="container">
      <h1>Live Football Scores</h1>
      {Object.keys(groupedByLeague).map((league, index) => (
        <div key={index} className="league-section">
          <h2 className="league-name">{league}</h2>
          <div className="cards-container">
            {groupedByLeague[league].map((match, matchIndex) => (
              <div
                key={matchIndex}
                onClick={() => fetchMatchDetails(match.id)}
                className="match-card"
              >
                <div className="team">
                  <h3 className="team-name">{match.homeTeam}</h3>
                  <div className="team-score">{match.homeScore}</div>
                </div>
                <div className="versus">vs</div>
                <div className="team">
                  <h3 className="team-name">{match.awayTeam}</h3>
                  <div className="team-score">{match.awayScore}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}

      {matchDetails && selectedMatchId && (
        <div className="mt-8 bg-gray-800 p-4 rounded-lg shadow-lg">
          <h2 className="text-center text-2xl font-bold mb-4">Match Details</h2>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <h3 className="font-bold mb-2">Home Team Players</h3>
              {matchDetails.home.players.map((player, index) => (
                <div key={index} className="mb-1">
                  {player.name} - {player.position}
                </div>
              ))}
            </div>
            <div>
              <h3 className="font-bold mb-2">Away Team Players</h3>
              {matchDetails.away.players.map((player, index) => (
                <div key={index} className="mb-1">
                  {player.name} - {player.position}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
