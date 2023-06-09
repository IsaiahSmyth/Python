
# Set up a new file and add the Player class with the given constructor

# Challenge 1: Update the constructor to accept a dictionary (player) as an argument and set the attributes using the dictionary

# Complete challenge 2: Create 3 instances of the Player class using the given dictionaries

# Complete challenge 3: Populate a new list with Player instances from the list of players.

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.


class Player:
    def __init__(self, player):
        self.name = player['name']
        self.team = player['team']
        self.poition = player['position']
    def __str__ (self):
        return f'{self.name} play for {self.team} and is a {self.position}'

    @classmethod
    def get_team(cls, team_list):
        team_list = []
        player_list = []
        for player in team_list:
            player_list.append(cls(player))
            return player_list
