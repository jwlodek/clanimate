"""
File containing some core clanimate classes + data structures. ClanimateError is the Exception raised by clanimate
functions when there is an error, the Animator class is a wrapper that allows the user to call animation functions 
in one call.

@author: Jakub Wlodek
"""


# python imports
import signal
import sys

# clanimate imports
from clanimate import indicator
from clanimate import wheelindicator
from clanimate import barindicator
from clanimate import scrolltextindicator

# list of supported indicators
supported_indicators = ['wheel', 'progress_bar', 'scroll_text']


class ClanimateError(Exception):
    """
    Class representing an error in the clanimate library
    """

    pass


class Animator:
    """
    Top level animator class used by the clanimate library.

    Attributes
    ----------
    indicator : clanimate.indicator.Indicator
        The instance of the indicator type that is wrapped with an Animator object. It contains the animation functions

    Methods
    -------
    sigint_handler(signal : signal.SIGNAL, frame : signal.frame)
        a helper function that kills the animation thread on recieving a SIGINT
    start_animation()
        a function that starts the selected animation
    end_animation()
        a function that ends the animation and joins the animation thread
    increment()
        a function that should be called to tell the animator that an item has been completed
    write()
        a wrapper function around print() that allows print calls to be used while the animator is running.
    """


    def __init__(self, indicator_type, num_elems, name='', color='None', todo_char='-', done_char='#', showcounter=True, animation_frames='|/-\\', sleep_time=0.1):
        """
        Constructor for the Animator class

        Parameters
        ----------
        indicator_type : str
            wheel, progress_bar, scroll_text - a string used to select the animation indicator type
        num_elems : int
            not used by all animations, but a counter of how many tasks must be completed
        name='' : str
            the name of the task - if not empty will be placed in front of animation.
        color='None' : str
            currently unimplemented. Will select color of animated indicator
        todo_char='-' : char
            a character representing a todo task
        done_char='#' : char
            a character representing a finished task
        showcounter : bool
            a toggle to display a done/todo counter with the animation
        animation_frames="|/-\\" : str
            frames or text used by text indicators
        sleep_time=0.1 : float
            time for sleeping between each animation frame
        """

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
        """ Function that handles interrupt signals - stops animation and exits. """

        self.end_animation()
        sys.exit()


    def start_animation(self):
        """ Function that starts animation - just calls the animation_thread.start() """

        if self.indicator is not None:
            self.indicator.animation_thread.start()


    def end_animation(self):
        """ Ends the animation thread """

        if self.indicator is not None:
            self.indicator.stop()


    def increment(self):
        """ Counts up by one counting the item counter """

        if self.indicator.num_elems is not None:
            self.indicator.increment_counter()
        else:
            raise ClanimateError('Current animation does not support incrementing item counter')


    def write(self, text):
        """ Function that should be used to print text to terminal while animation is playing. """

        temp = text
        for i in range(len(text), self.indicator.chars_written):
            temp = temp + ' '
        self.indicator.write(temp + '\n', without_title=True)