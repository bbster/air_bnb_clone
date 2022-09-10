# class Human:
#     def __init__(self, name):
#         print("huma initialized")
#         self.name = name
#
#     def say_hello(self):
#         print(f"hello my name is {self.name}")
#
#
# class Player(Human):
#     def __init__(self, name, xp): # self는 class의 인스턴스
#         super().__init__(name)
#         self.name = name
#
#
# class Fan(Human):
#     def __init__(self, name, fav_team):
#         super().__init__(name)
#         self.fav_team = fav_team
#
# nico = Player("nico", 10)
# nico.say_hello()
#
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(super().__str__())
        return f"dog: {self.name}"

    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "😂"


jia = Dog("jia")
print(jia)
paul = Dog("Paul")
print(paul)
print(dir(jia))
print(jia.name)