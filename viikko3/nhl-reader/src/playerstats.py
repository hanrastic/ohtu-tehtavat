
from player import Player
from playerreader import PlayerReader

class PlayerStats:

    def top_scorers_by_nationality(players):
        #print(players)

        players.sort(key = lambda player: player.nationality)

        for x in players:
            #print("Pelaajan kansalaisuus: ", x.nationality)
            if x.nationality != "FIN":
                players.remove(x)

        for player in players:
            if player.nationality == "FIN":
                print("Pelaajan kansalaisuus: ", x.nationality)
                #print(player)
                pass
            
        return players
    