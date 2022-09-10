class Human:
    def __init__(self, name):
        print("huma initialized")
        self.name = name

    def say_hello(self):
        print(f"hello my name is {self.name}")


class Player(Human):
    def __init__(self, name, xp): # self는 class의 인스턴스
        self.name = name


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team

nico = Fan("nico", "blue")
