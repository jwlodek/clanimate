import signal
import sys
from clanimate import indicator
from clanimate import wheelindicator
from clanimate import barindicator
from clanimate import scrolltextindicator

supported_indicators = ['wheel', 'progress_bar', 'scroll_text']

class ClanimateError(Exception):
    pass

class Animator:

    def __init__(self, indicator_type, num_elems, name='', color='None', num_items=10, todo_char='-', done_char='#', showcounter=True, animation_frames='|/-\\', sleep_time=0.1):
        self.indicator = None

        signal.signal(signal.SIGINT, self.sigint_handler)

        if indicator_type == 'wheel':
            self.indicator = wheelindicator.WheelIndicator(num_elems, name=name, color=color, sleep_time=sleep_time, animation_frames=animation_frames)
        elif indicator_type == 'progress_bar':
            self.indicator = barindicator.BarIndicator(num_elems, name=name, color = color, todo_char=todo_char, done_char=done_char, showcounter=True)
        elif indicator_type == 'scroll_text':
            self.indicator = scrolltextindicator.ScrollTextIndicator(num_elems, name=name, color=color, sleep_time=sleep_time, animation_frames=animation_frames)

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
        else:
            raise ClanimateError('Current animation does not support incrementing item counter')