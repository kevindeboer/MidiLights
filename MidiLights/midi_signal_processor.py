from messages import LedOnMessage, LedOffMessage
from instruments import Instruments


class MidiSignalProcessor:

    ignore_notes = [64]

    """Control the leds on the strip based on a midi signal."""
    def __init__(self, strip, color_profile):
        self.strip = strip
        self.instrument_led_mapping = {
            Instruments.HIHAT: range(6,12),
            Instruments.CRASH1: range(20,26),
            Instruments.CRASH2: range(56, 62),
            Instruments.KICK: range(38,44),
            Instruments.RIDE: range(50,56), 
            Instruments.SNARE: range(12,20),
            Instruments.TOM1: range(26,32),
            Instruments.TOM2: range(32,38),
            Instruments.TOM3: range(44,50),
            Instruments.TOM4: range(0,6),
        }
        self.color_profile = color_profile
        self.hi_hat_open = True

    def _get_leds_for_note(self, note):
        for instrument, leds in self.instrument_led_mapping.items():
            if note in instrument.notes:
                return leds
        raise ValueError("No instrument found for note {0}".format(note))


    def process(self, midi_signal):
        """Find the leds and color for the given signal, and turn them on."""
        midi_signal_type = midi_signal.type
        if midi_signal_type == 'note_on':
            note = midi_signal.note
            if note in self.ignore_notes:
                return
            print('PROCESSING NOTE: {0}'.format(note))
            LedOnMessage(
                self.strip, 
                self._get_leds_for_note(note), 
                self.color_profile.get_rgb_fade_for_note(note, self.hi_hat_open),
            ).start()
        if midi_signal_type == 'control_change':
            self.hi_hat_open = midi_signal.value != 127
