#!/usr/bin/env python3
import sys
sys.path.append("./src")

from gamestate import ObisTrisGameState
from renderer import ObisTrisRenderer
from keyboardthread import KeyboardThread
from renderthread import RenderThread
from pprint import pprint
from time import sleep
from argparse import ArgumentParser



parser = ArgumentParser( 
            description='Play tetris on your ICMm display, use the arrow keys (up is rotate, down is accelerated drop)',
            epilog='Dont forget to rotate your display :)'
)

parser.add_argument(
    "-p",
    "--port",
    default="/dev/tty.usbserial-211310",
    help="path to serial port to which the display is connected"
)

parser.add_argument(
    "-d",
    "--device-id",
    default=0,
    help="target device ID"
)

arguments = parser.parse_args()

state = ObisTrisGameState()
renderer = ObisTrisRenderer(com_port=arguments.port, device_id=arguments.device_id)

def render():
    renderer.render_state(state)
    state.print() # show game in cli for testing/debugging


def play(state):
    while not state.is_game_over:
        sleep(state.get_interval())
        state.advance()
    print("\n\nGame over! You scored", state.score)
    exit()

keyboard_thread = KeyboardThread(state)
render_thread = RenderThread(render)
keyboard_thread.start()
render_thread.start()

play(state)