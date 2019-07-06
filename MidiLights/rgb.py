class RGBFade(object):
    """Represents a color, combined with how quickly it should fade out."""
    def __init__(self, red, green, blue, fade_time):
        self.red = red
        self.green = green
        self.blue = blue
        self.fade_time = fade_time


class Red(RGBFade):

    def __init__(self, fade_time):
        super(Red, self).__init__(255, 0, 0, fade_time)

class Green(RGBFade):

    def __init__(self, fade_time):
        super(Green, self).__init__(0, 255, 0, fade_time)

class Blue(RGBFade):

    def __init__(self, fade_time):
        super(Blue, self).__init__(0, 0, 255, fade_time)

class Yellow(RGBFade):

    def __init__(self, fade_time):
        super(Yellow, self).__init__(255, 255, 0, fade_time)

class Pink(RGBFade):

    def __init__(self, fade_time):
        super(Pink, self).__init__(255, 0, 255, fade_time)

class LightBlue(RGBFade):

    def __init__(self, fade_time):
        super(LightBlue, self).__init__(0, 255, 255, fade_time)

class White(RGBFade):

    def __init__(self, fade_time):
        super(White, self).__init__(255, 255, 255, fade_time)

class Random(RGBFade):

    def __init__(self):
        from random import choice
        red = choice([0,255]) 
        green = choice([0,255]) 
        blue = choice([0,255]) 
        fade = choice(range(3,10))/10.0
        super(Random, self).__init__(red, green, blue, fade)