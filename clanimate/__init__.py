import signal
import sys
from clanimate import indicator
from clanimate import wheelindicator
from clanimate import barindicator

supported_indicators = ['wheel']

class ClanimateError(Exception):
    pass

class Animator:

    def __init__(self, indicator_type, num_elems, name='', color='None', num_items=10, todo_char='-', done_char='#', showcounter=True, animation_frames='|/-\\', sleep_time=0.1):
        self.indicator = None

        if indicator_type == 'wheel':
            self.indicator = wheelindicator.WheelIndicator(num_elems, name=name, color=color, sleep_time=sleep_time, animation_frames=animation_frames)
        elif indicator_type == 'progress_bar':
            self.indicator = barindicator.BarIndicator(num_elems, name=name, color = color, todo_char=todo_char, done_char=done_char, showcounter=True)

        elif indicator_type not in supported_indicators:
            raise ClanimateError('Selected animated indicator type is not supported')


    def sigint_handler(self, signal, frame):
        """
        Function that handles interrupt signals - stops animation and exits.
        """

        self.end_animation()
        sys.exit()


    def start_animation(self):
        """
        Function that starts animation - just calls the animation_thread.start()
        """

        if self.indicator is not None:
            self.indicator.animation_thread.start()


    def end_animation(self):
        if self.indicator is not None:
            self.indicator.stop()


    def increment(self):
        if self.indicator.num_elems is not None:
            self.indicator.increment_counter()
            if self.indicator.item_counter == self.indicator.num_elems:
                self.end_animation()
        else:
            raise ClanimateError('Current animation does not support incrementing item counter')