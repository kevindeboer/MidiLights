from instruments import Note
from rgb import *

class ColorProfile:
    """Map notes to colors."""
    def __init__(
        self, hi_hat_closed, hi_hat_open, hi_hat_foot_close, hi_hat_foot_tap,
        crash1, crash1_stop, crash2, kick, snare_head, snare_rim,
        ride_bell, ride_bow, ride_rim, 
        tom1_head, tom1_rim, tom2_head, tom2_rim,
        tom3_head, tom3_rim, tom4_head
    ):
        self.hi_hat_closed = hi_hat_closed
        self.hi_hat_open = hi_hat_open
        self.hi_hat_foot_close = hi_hat_foot_close
        self.hi_hat_foot_tap = hi_hat_foot_tap
        self.crash1 = crash1
        self.crash1_stop = crash1_stop
        self.crash2 = crash2
        self.kick = kick
        self.snare_head = snare_head
        self.snare_rim = snare_rim
        self.ride_bell = ride_bell
        self.ride_bow = ride_bow
        self.ride_rim = ride_rim
        self.tom1_head = tom1_head
        self.tom1_rim = tom1_rim
        self.tom2_head = tom2_head
        self.tom2_rim = tom2_rim
        self.tom3_head = tom3_head
        self.tom3_rim = tom3_rim
        self.tom4_head = tom3_head

    @property
    def _note_mapping(self):
        return {
            Note.HiHatStop: self.hi_hat_foot_close,
            Note.HiHatFootTap: self.hi_hat_foot_close,
            Note.Crash1: self.crash1,
            Note.Crash1Stop: self.crash1_stop,
            Note.Crash2: self.crash2,
            Note.Kick: self.kick,
            Note.RideBell: self.ride_bell,
            Note.RideBow: self.ride_bow,
            Note.RideRim: self.ride_rim,
            Note.SnareHead: self.snare_head,
            Note.SnareRim: self.snare_rim,
            Note.Tom1Head: self.tom1_head,
            Note.Tom1Rim: self.tom1_rim,
            Note.Tom2Head: self.tom2_head,
            Note.Tom2Rim: self.tom2_rim,
            Note.Tom3Head: self.tom3_head,
            Note.Tom3Rim: self.tom3_rim,
            Note.Tom4Head: self.tom4_head
        }

    def get_rgb_fade_for_note(self, note, hi_hat_open=None):
        if note == Note.HiHat:
            if hi_hat_open is None:
                raise ValueError("Please provide hi_hat_open argument for hi hat note")
            else:
                return self.hi_hat_open if hi_hat_open else self.hi_hat_closed
        return self._note_mapping[note]

default = ColorProfile(
    hi_hat_closed=Green(0.3), 
    hi_hat_open=Red(0.6), 
    hi_hat_foot_close=White(0.1), 
    hi_hat_foot_tap=LightBlue(0.3), 
    crash1=Red(0.6), 
    crash1_stop=White(0.1), 
    crash2=Pink(0.4), 
    kick=Blue(0.2), 
    snare_head=Yellow(0.2), 
    snare_rim=White(0.2), 
    ride_bell=Green(0.3), 
    ride_bow=Blue(0.3), 
    ride_rim=Pink(0.3), 
    tom1_head=Yellow(0.3), 
    tom1_rim=LightBlue(0.2), 
    tom2_head=Yellow(0.3), 
    tom2_rim=LightBlue(0.2), 
    tom3_head=Yellow(0.3), 
    tom3_rim=LightBlue(0.3), 
    tom4_head=Yellow(0.3)
)

vaporwave = ColorProfile(
    hi_hat_closed=Pink(0.3), 
    hi_hat_open=White(0.6), 
    hi_hat_foot_close=Red(0.1), 
    hi_hat_foot_tap=Blue(0.3), 
    crash1=Pink(0.6), 
    crash1_stop=White(0.1), 
    crash2=Pink(0.4), 
    kick=Yellow(0.2), 
    snare_head=Yellow(0.2), 
    snare_rim=LightBlue(0.2), 
    ride_bell=Green(0.3), 
    ride_bow=Pink(0.3), 
    ride_rim=White(0.3), 
    tom1_head=LightBlue(0.3), 
    tom1_rim=Green(0.2), 
    tom2_head=LightBlue(0.3), 
    tom2_rim=Green(0.2), 
    tom3_head=LightBlue(0.3), 
    tom3_rim=Green(0.3), 
    tom4_head=LightBlue(0.3)
)