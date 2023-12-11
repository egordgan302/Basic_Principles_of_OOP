class RoboCat:
    def __init__(self, speed, sound, color):
        self.ears = 2
        self.hp = 9
        self.speed = speed
        self.sound = sound
        self.color = color

    def play_sounde(self):
        print(f'My robocat say {self.sound}')

class angryrobocat(RoboCat):
    def __init__(self, speed, hp, color):
        super().__init__(speed, hp, color)
        self.superpower = 'стрелять лазерами'
    def damage(self, damage):
        self.hp -= damage
        print(f'осталось {self.hp}')

my_robocat = RoboCat(10, 'meow', 'black')
print (my_robocat.color)

my_robocat.play_sounde()

angry = angryrobocat(100, 9, 'red')
angry.damage(2)
