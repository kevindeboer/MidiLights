class Note:
    HiHatStop = 44
    HiHat = 46
    HiHatFootTap = 30
    Crash1 = 49
    Crash1Stop = 34
    Crash2 = 60
    Kick = 36
    RideBell = 53
    RideBow = 51
    RideRim = 25
    SnareHead = 38
    SnareRim = 40
    Tom1Head = 47
    Tom1Rim = 50
    Tom2Head = 45
    Tom2Rim = 48
    Tom3Head = 43
    Tom3Rim = 41
    Tom4Head = 63

    ALL = [44,46,30,49,34,60,36,53,51,25,38,40,47,50,45,48,43,41,63] #just for choice

class Instrument:

	def __init__(self, *notes):
		self.notes = notes

class Instruments:

	HIHAT = Instrument(Note.HiHatStop, Note.HiHat, Note.HiHatFootTap)
	CRASH1 = Instrument(Note.Crash1, Note.Crash1Stop)
	CRASH2 = Instrument(Note.Crash2)
	KICK = Instrument(Note.Kick)
	RIDE = Instrument(Note.RideBell, Note.RideBow, Note.RideRim)
	SNARE = Instrument(Note.SnareHead, Note.SnareRim)
	TOM1 = Instrument(Note.Tom1Head, Note.Tom1Rim)
	TOM2 = Instrument(Note.Tom2Head, Note.Tom2Rim)
	TOM3 = Instrument(Note.Tom3Head, Note.Tom3Rim)
	TOM4 = Instrument(Note.Tom4Head)
