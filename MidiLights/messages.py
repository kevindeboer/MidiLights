import time
from collections import namedtuple
from threading import Thread
from neopixel import Color

class LedLocker:
    """Class to keep track which led strip has been locked by which message."""
    locks = {}

    @classmethod
    def set_message_for_leds(cls, leds, message):
        for led in leds:
            cls.locks[led] = message

    @classmethod
    def get_message_for_led(cls, led):
        return cls.locks[led]


class LedMessage(Thread):
    """A message (or event) to control the colors of some leds."""
    def __init__(self, strip, leds):
        Thread.__init__(self)
        self.strip = strip
        self.leds = leds

    def _take_control_of_leds(self):
        LedLocker.set_message_for_leds(self.leds, self)

    def _has_control_of_led(self, led):
        return LedLocker.get_message_for_led(led) is self


class LedOnMessage(LedMessage):
    """Turn the leds on and fade out."""
    def __init__(self, strip, leds, rgb_fade):
        LedMessage.__init__(self, strip, leds)
        self.rgb_fade = rgb_fade
        self.set_color_interval = 30

    def run(self):
        red_decrement = float(self.rgb_fade.red) / float(self.set_color_interval)
        green_decrement = float(self.rgb_fade.green) / float(self.set_color_interval)
        blue_decrement = float(self.rgb_fade.blue) / float(self.set_color_interval)
        sleep_time = float(self.rgb_fade.fade_time) / float(self.set_color_interval)
        self._take_control_of_leds()
        for i in range(self.set_color_interval+1):
            red = self.rgb_fade.red - red_decrement*i
            green = self.rgb_fade.green - green_decrement*i
            blue = self.rgb_fade.blue - blue_decrement*i
            for led in self.leds:
                if not self._has_control_of_led(led):
                    continue
                self.strip.setPixelColor(led, Color(int(blue), int(red), int(green)))
            self.strip.show()
            time.sleep(sleep_time)

class LedOffMessage(LedMessage):
    """Turn all leds off."""
    def __init__(self, strip, leds):
        LedMessage.__init__(self, strip, leds)

    def run(self):
        self._take_control_of_leds()
        for led in self.leds:
            self.strip.setPixelColor(led, Color(0,0,0))
        self.strip.show()




