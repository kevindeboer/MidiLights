"""Test receiving midi signals"""
import mido

print(mido.get_input_names())

inport = mido.open_input('USB2MIDI:USB2MIDI MIDI 1 20:0')

while True:
    midi = inport.receive()
    print(midi)
    # import pdb;pdb.set_trace()
