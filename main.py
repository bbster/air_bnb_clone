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
    def woof(self):
        print("woofwoof")


class Beagle(Dog):
    def woof(self):
        super().woof()
        print("jump")

beagle = Beagle()
beagle.woof()
