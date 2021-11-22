import requests
from player import Player

class PlayerReader:

    def get_players(osoite):
        response = requests.get(osoite).json()

        players = []

        for player_dict in response:
            player = Player(player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality'] )
            players.append(player)

        return players
