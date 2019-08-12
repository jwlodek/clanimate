"""
The base class for all loading bars and indicators supported by clanimate.

@author: Jakub Wlodek
"""

# python imports. threading for creating animation thread
# sys for writing, time for waiting
import threading
import sys
import time


class Indicator:
    """
    Base class extended by all supported animated indicators

    Attributes
    ----------
    name : str
        the name of the task covered by the animation
    color : str
        unimplemented - will be the color of the animation
    animation_thread : threading.Thread
        the thread that allows the animation to run even while script processes in the background
    is_running : bool
        boolean saying if animation is running
    item_counter : int
        counter representing which task is being worked on
    num_elems : int
        number of tasks to complete
    chars_written : int
        number of chars written for the animation in the previous line
    writing : bool
        a toggle to see if the indicator is writing or not

    Methods
    -------
    start()
        starts the animation
    animate()
        function that needs to be implemented by each extension of this base class
    stop()
        function that stops the animation
    write()
        function used to actually write the animation to stdout
    increment_counter()
        increments the completed item counter
    """


    def __init__(self, num_elems, name='', color='None'):
        """
        Constructor for the Indicator class.

        Parameters
        ----------
        num_elems : int
            counter of how many tasks need to be completed.
        name='' : str
            name of task - will be added to the start of the animation
        color='None' : str
            unimplemented - will be color of animation
        """

        self.name = name
        self.color = color
        self.animation_thread = threading.Thread(target=self.start, name='Animation Thread')
        self.is_running = False
        self.item_counter = 1
        self.num_elems = num_elems
        self.chars_written = 0


    def start(self):
        """
        Base function that starts the animate function. The animate function will be called until the 
        animation is killed.
        """

        self.is_running = True
        while self.is_running:
            self.animate()


    def animate(self):
        """
        A base class that must be implemented in each child class, with the actual animation.
        """

        pass


    def stop(self):
        """
        Function that stops the animation thread and waits for it to join.
        """

        self.is_running = False
        self.animation_thread.join()
        self.animation_thread = threading.Thread(target=self.animate, name='Animation Thread')
        sys.stdout.write('\n')


    def write(self, new_indicator_state, without_title=False):
        """
        Function writes the indicator to stdout

        Parameters
        ----------
        new_indicator_state : str
            the new indicator state that will be displayed (ex. new frame in animation)
        """

        if not without_title and len(self.name) > 0:
            new_indicator_state = '\r{}   {}'.format(self.name, new_indicator_state)
        else:
            new_indicator_state = '\r{}'.format(new_indicator_state)
        self.chars_written = len(new_indicator_state)
        sys.stdout.write(new_indicator_state)
        sys.stdout.flush()


    def increment_counter(self):
        """
        Function that increments the processed item counter. Used by the progress bar.
        """

        self.item_counter = self.item_counter + 1
