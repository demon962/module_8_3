class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


my_pegasus = Pegasus()


print(my_pegasus.get_pos())  # (0, 0)

my_pegasus.run(10)
my_pegasus.fly(15)
print(my_pegasus.get_pos())

my_pegasus.move(5, 20)
print(my_pegasus.get_pos())

my_pegasus.voice()
