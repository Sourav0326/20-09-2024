def list_sports():
    return "Football", "Cricket", "Tennis", "Basketball"


def famous_player(sport):
    players = {
        "Football": "Lionel Messi",
        "Cricket": "MS Dhoni",
        "Tennis": "Serena Williams",
        "Basketball": "Lebron James"

    }
    return players.get(sport, "unknown player")

sports = list_sports()
for sport in sports:
    player = famous_player(sport)
    print(f"{player} is a famous {sport} player")
