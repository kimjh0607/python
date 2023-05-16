class Char:
    def __init__(self,name):
        self.name=name
    def do(self):
        print("do")

class Fighter(Char):
    def do(self):
        print("fighting")
class Healer(Char):
    def do(self):
        print("healing")
class Wizard(Char):
    def do(self):
        print("magic")

fighter1 = Fighter('tom')
healer1 = Healer("Andy")
wizard1 = Wizard('Emily')

for x in (fighter1, healer1, wizard1):
    print(x.name, end=' ')
    x.do

