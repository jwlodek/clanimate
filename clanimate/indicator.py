"""
The base class for all loading bars and indicators supported by clanimate.

@author: Jakub Wlodek
"""

import threading
import sys
import itertools
import time
import datetime


class Indicator:

    def __init__(self, num_elems, name='', color='None'):
        self.name = name
        self.color = color
        self.animation_thread = threading.Thread(target=self.start, name='Animation Thread')
        self.is_running = False
        self.item_counter = 0
        self.num_elems = num_elems


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


    def write(self, new_indicator_state):
        """
        Function writes the indicator to stdout

        Parameters
        ----------
        new_indicator_state : str
            the new indicator state that will be displayed (ex. new frame in animation)
        """

        new_indicator_state = '\r{}   {}'.format(self.name, new_indicator_state)
        sys.stdout.write(new_indicator_state)
        sys.stdout.flush()


    def increment_counter(self):
        """
        Function that increments the processed item counter. Used by the progress bar.
        """

        self.item_counter = self.item_counter + 1
