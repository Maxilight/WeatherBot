class Parrot:

    def fly(self):
        print("Попугай умеет летать")

    def swim(self):
        print("Попугай не умеет плавать")


class Penguin:

    def fly(self):
        print("Пингвин не умеет летать")

    def swim(self):
        print("Пингвин умеет плавать")
def flying_test(bird):
    bird.swim()
kesha = Parrot()
peggy = Penguin()
flying_test(kesha)
flying_test(peggy)