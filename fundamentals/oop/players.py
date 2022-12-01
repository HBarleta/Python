class Player:

    def __init__(self, dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position =dict['position']
        self.team = dict['team'] 

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
KD = Player(kevin)
print(KD.position)