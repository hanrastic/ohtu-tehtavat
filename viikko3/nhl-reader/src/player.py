class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    def __str__(self):
        yht = self.goals + self.assists
        return f"{self.name:25}{self.team:25}{str(self.goals):5} + {str(self.assists):5} = {str(yht):5}"


def nationalityCheck(self):
    if self.nationality == "FIN":
        return True
    else:
        return False
        