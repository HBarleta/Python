class Player:
    team_list = []
    def __init__(self,dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position = dict['position']
        self.team = dict['team']
        Player.team_list.append(self)


players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

kevin_durant = Player(players[0])
jason_tatum = Player(players[1])
kyrie_irving = Player(players[2])
print(kevin_durant.age)
print(kevin_durant.position)
print(jason_tatum.team)
print(kyrie_irving.name)
print(kyrie_irving.team)
print(Player.team_list)
