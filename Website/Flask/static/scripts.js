function fetchMatchDetails(matchId) {
    fetch(`/match/${matchId}`)
        .then(response => response.json())
        .then(data => {
            const detailsElement = document.getElementById(`details-${matchId}`);
            detailsElement.style.display = detailsElement.style.display === "none" || detailsElement.style.display === "" ? "block" : "none";

            const homePlayersList = document.getElementById(`home-players-${matchId}`);
            const awayPlayersList = document.getElementById(`away-players-${matchId}`);

            homePlayersList.innerHTML = "";
            awayPlayersList.innerHTML = "";

            if (data.home && data.home.players) {
                data.home.players.forEach(player => {
                    homePlayersList.innerHTML += `<li>${player.name} - ${player.position}</li>`;
                });
            } else {
                homePlayersList.innerHTML = "<li>No players found</li>";
            }

            if (data.away && data.away.players) {
                data.away.players.forEach(player => {
                    awayPlayersList.innerHTML += `<li>${player.name} - ${player.position}</li>`;
                });
            } else {
                awayPlayersList.innerHTML = "<li>No players found</li>";
            }
        })
        .catch(error => console.error('Error fetching match details:', error));
}
