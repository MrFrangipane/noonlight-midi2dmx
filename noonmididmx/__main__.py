import sys
from noon_midi_dmx import NoonMidiDmx


if __name__ == '__main__':
    noon_midi_dmx = NoonMidiDmx(midi_device_id=int(sys.argv[1]), enttec_usb_device=sys.argv[2])
    noon_midi_dmx.init()
    noon_midi_dmx.run()
