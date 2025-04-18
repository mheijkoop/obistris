from foconutil import FoconFrame, FoconSerialTransport, FoconBus, FoconMessageBus, FoconDisplay
from foconutil.devices.display import *
from foconutil.devices.device import FoconDevice
from pprint import pprint
from functools import reduce
import logging
from time import sleep

class ObisTrisRenderer():

    def __init__(self, com_port = "/dev/tty.usbserial-211310", device_id = 0, source_id = 14, baud_rate = 56700, crystal = 1.8432):
        self.com_port = com_port
        self.device_id = device_id
        self.source_id = source_id

        debug = False
        transport = FoconSerialTransport(self.com_port, baudrate=baud_rate, xtal=crystal, debug = debug)
        bus = FoconBus(transport, self.source_id, debug = debug)
        msg_bus = FoconMessageBus(bus, self.source_id, debug = debug)
        self.device = FoconDevice(msg_bus, self.device_id)
        self.display = FoconDisplay(self.device)
        
        self.logger = logging.getLogger()
        self.logger.addHandler(logging.StreamHandler())
        self.logger.setLevel(logging.ERROR)

        self.config = self.display.get_current_config()
        self.display.use_config(self.config) # shouldnt be needed but solved a weird problem :)
        self.state_spec = False



    def render_state(self, state):

        if not self.state_spec:
            self.state_spec = FoconDisplayDrawSpec(
                object_id = 1,
                output_id = 1,
                composition = FoconDisplayDrawComposition.Replace,
                transition = FoconDisplayDrawTransition.Appear,
                x_start = 0,
                y_start = 0,
                x_end = state.height*2,
                y_end = state.width*2,
                count = 1,
                duration = 10
            )
            
        # TODO show score
        self.logger.debug(self.display.draw(self.get_pixels(state.get_board_map()), state.width*2, self.state_spec))
        self.render_score(state)


    def render_score(self, state):
       # TODO - render score as pixel art above the board
       return


    def get_pixels(self, boardmap):
        
        # we need to double every pixel in both X and Y to make it look nice on the display
        # and we need to reverse the Y direction because what makes sense for us and for the display errrm differs

        rows = [list(reduce(list.__add__, [[1,1] if cell else [0,0] for cell in row])) for row in reversed(boardmap)]

        double_rows = []
        for row in rows:
            double_rows.append(row)
            double_rows.append(row)

        return double_rows