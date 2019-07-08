from neopixel import *
from random import choice
from color_profile import default, vaporwave
from midi_signal_processor import MidiSignalProcessor
import time
import mido

# LED strip configuration:
LED_COUNT      = 62     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

inport = mido.open_input('USB2MIDI:USB2MIDI MIDI 1 20:0')

def reset_pins(strip):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()

def init_signal_processor():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    reset_pins(strip)
    midi_signal_processor = MidiSignalProcessor(strip, vaporwave)
    return midi_signal_processor

def main():
    midi_signal_processor = init_signal_processor()
    while True:
        midi_signal_processor.process(inport.receive())
        

def test():
    """A simple test function that mocks actual midi signals."""
    from instruments import Note

    class Midi:

        def __init__(self):
            self.type = 'note_on'
            self.note = choice(Note.ALL)

    midi_signal_processor = init_signal_processor()
    while True:
        midi_signal_processor.process(Midi())
        time.sleep(0.2)


if __name__ == '__main__':
    main()





