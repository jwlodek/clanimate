import signal
import sys
from clanimate import indicator
from clanimate import animationindicator

supported_indicators = ['wheel']

class StdOutHook:
    def __init__(self):
        self.original_stdout = None

    def process_hook(self, text):
        self.original_stdout.flush()
        self.original_stdout.write(text)

    def start_hook(self, func = None):
        sys.stdout = self
        self.original_stdout = sys.stdout


    def write(self, text):
        self.process_hook(text)

class Animator:

    def __init__(self, indicator_type, name='', color='None', num_items=10, todo_char='-', done_char='#', showcounter=True, animation_frames='|/-\\', sleep_time=0.1):
        self.indicator = None

        if indicator_type == 'wheel':
            self.indicator = animationindicator.AnimationIndicator(name=name, color=color, sleep_time=sleep_time, animation_frames=animation_frames)

        elif indicator_type not in supported_indicators:
            pass

        hook = StdOutHook()
        hook.start_hook()
        # Proper signal handling here
        signal.signal(signal.SIGINT, self.sigint_handler)


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
