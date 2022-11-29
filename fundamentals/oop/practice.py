class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
    	print(f"Hello, my name is {self.name}")

harold = User("Harold", "hbf20c@gmail.com")
print(harold.email)
print(harold.greeting())