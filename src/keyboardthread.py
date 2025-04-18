from sshkeyboard import listen_keyboard
from threading import Thread

class KeyboardThread(Thread):

    def __init__(self, state):
        self.state = state
        super(__class__, self).__init__(name="KeyboardThread", daemon=True)
    
    def run(self):
        listen_keyboard(
            on_press=self.handle_keypress,
            delay_second_char=0.0
        )

    def handle_keypress(self, key):
        if key == "space" or key == "up":
            self.state.rotate()
        elif key == "right":
            self.state.right()
        elif key == "left":
            self.state.left()
        elif key == "down":
            self.state.down()
        elif key == "s":
            self.state.score += 5 # not for cheating! just for debugging! 
        return True