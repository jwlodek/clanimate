"""
Class for the simplest implementation of the Indicator class,
a spinning wheel animation.

@author: Jakub Wlodek
"""

# clanimate import + time
from clanimate import indicator
import time

class WheelIndicator(indicator.Indicator):
    """
    Class for Wheel indicator - a basic animation that cycles through characters.
    Extends the Indicator base class

    Attributes
    ----------
    sleep_time : float
        time to wait between refreshing animation frame
    animation_frames : str
        a string of characters to cycle through
    frame_counter : int
        counter representing which char in the animation_frames str we are on

    Methods
    -------
    animate()
        implements the base class animate function
    """


    def __init__(self, num_elems, name='', color='None', sleep_time=0.1, animation_frames='|/-//'):
        """
        Constructor for the WheelIndicator class. First calls superclass constructor, and then inits
        some attributes
        """

        super().__init__(num_elems, name=name, color=color)
        self.sleep_time = sleep_time
        self.animation_frames = animation_frames
        self.frame_counter = 0


    def animate(self):
        """
        Animation function. Overrides base class. Simply writes name + char at frame counter
        """

        time.sleep(self.sleep_time)
        self.write(self.animation_frames[self.frame_counter])
        self.frame_counter = self.frame_counter + 1
        if self.frame_counter == len(self.animation_frames):
            self.frame_counter = 0

