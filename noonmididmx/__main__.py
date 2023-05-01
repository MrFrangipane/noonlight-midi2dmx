import sys
from noonmididmx.noon_midi_dmx import NoonMidiDmx

import pygame

def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()


def _print_device_info():
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print(
            "%2i: interface :%s:, name :%s:, opened :%s:  %s"
            % (i, interf, name, opened, in_out)
        )


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_device_info()

    noon_midi_dmx = NoonMidiDmx(midi_device_id=int(sys.argv[1]), enttec_usb_device=sys.argv[2])
    noon_midi_dmx.init()
    noon_midi_dmx.run()
