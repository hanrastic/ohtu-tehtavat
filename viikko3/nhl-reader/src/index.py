import requests
from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"

    players = PlayerReader.get_players(url)

    stats = PlayerStats.top_scorers_by_nationality(players)


    for x in stats:
        print(x)

main()