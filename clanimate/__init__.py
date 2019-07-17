import signal
import sys
from clanimate import progressindicator
from clanimate import wheel

class Animator:

    def __init__(self, indicator_type, name='', color='None', num_items=10, todo_char='-', done_char='#', showcounter=True, animation_frames='|/-\\', sleep_time=0.1):
        self.indicator = None

        if indicator_type == 'wheel':
            self.indicator = wheel.WheelIndicator(name=name, color=color, sleep_time=sleep_time, animation_frames=animation_frames)

        signal.signal(signal.SIGINT, self.sigint_handler)

    def sigint_handler(self, signal, frame):
        self.end_animation()
        sys.exit()


    def start_animation(self):
        if self.indicator is not None:
            self.indicator.animation_thread.start()


    def end_animation(self):
        if self.indicator is not None:
            self.indicator.stop()
