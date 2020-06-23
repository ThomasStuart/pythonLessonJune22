class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

# END CLASS

# create fist   object call it "user1"  -> {"Tom", "p99"}
user1 = User("tom", "p99")

# create second object call it "user2"  -> {"Donkey", ""}
user2 = User("Donkey", "123")