import pygame as pg
import pygame.midi
from DMXEnttecPro import Controller


_MIDI_EVENT_PACK_SIZE = 10


class NoonMidiDmx:
    def __init__(self, midi_device_id, enttec_usb_device):
        self._device_id = midi_device_id
        self._input = None
        self._running = False
        self._dmx_controller = Controller(enttec_usb_device)

    def init(self):
        pg.init()
        pg.fastevent.init()
        pygame.midi.init()
        self._input = pygame.midi.Input(self._device_id)

    def run(self):
        self._running = True
        while self._running:
            self._main_loop()

        self._input = None
        pygame.midi.quit()

    def _main_loop(self):
        for event in pg.fastevent.get():
            if event.type in [pg.QUIT, pg.KEYDOWN]:
                self._running = False

        if self._input.poll():
            midi_events = self._input.read(_MIDI_EVENT_PACK_SIZE)
            for midi_event in midi_events:
                channel = midi_event[0][0] - 175
                cc_number = midi_event[0][1]
                value = midi_event[0][2]

                self._dmx_controller.set_channel(10 * channel + cc_number, value * 2)

            self._dmx_controller.submit()
