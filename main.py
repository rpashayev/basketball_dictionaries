class Player:
    all_teams = []
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']
    
    @classmethod
    def get_team(cls, team_list):
        for team in team_list:
            cls.all_teams.append(cls(team))
        return cls.all_teams
    
    
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

players = [
    {
    'name': 'Kevin Durant', 
    'age':34, 
    'position': 'small forward', 
    'team': 'Brooklyn Nets'
    },
    {
    'name': 'Jason Tatum', 
    'age':24, 
    'position': 'small forward', 
    'team': 'Boston Celtics'
    },
    {
    'name': 'Kyrie Irving', 
    'age':32,
    'position': 'Point Guard', 
    'team': 'Brooklyn Nets'
    },
    {
    'name': 'Damian Lillard', 
    'age':33,
    'position': 'Point Guard', 
    'team': 'Portland Trailblazers'
    },
    {
    'name': 'Joel Embiid', 
    'age':32,
    'position': 'Power Foward', 
    'team': 'Philidelphia 76ers'
    },
    {
    'name': '', 
    'age':16, 
    'position': 'P', 
    'team': 'en'
    }
]

new_team = []
for player in players:
    new_team.append(Player(player))

lst = Player.get_team(players)
print(lst)

for p in lst: 
    print(f'Player: {p.name}, age is {p.age}, position is{p.position} and the current team is {p.team}')
