"""
Extension of the Indicator class for a scrolledtext indicator.
Used to animate through a series of characters. For example, an
ellipses (...) scrolling through all 3 periods would be a scrolledtext indicator.

@author: Jakub Wlodek
"""

# clanimate + time import
from clanimate import indicator
import time

class ScrollTextIndicator(indicator.Indicator):
    """
    Class for ScrollText indicator - a basic animation that cycles through characters.
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


    def __init__(self, num_elems, name='', color='None', sleep_time=0.1, animation_frames='...'):
        """
        Constructor for the ScrollTextIndicator class. First calls superclass constructor, and then inits
        some attributes
        """

        super().__init__(num_elems, name=name, color=color)
        self.sleep_time = sleep_time
        self.animation_text = animation_frames
        self.frame_counter = 0


    def animate(self):
        """
        Animation function. Overrides base class. Simply writes name + text up to frame counter
        """

        time.sleep(self.sleep_time)
        current_text = self.animation_text[0:self.frame_counter]
        for i in range(self.frame_counter, len(self.animation_text)):
            current_text = current_text + ' '
        self.write(current_text)
        self.frame_counter = self.frame_counter + 1
        if self.frame_counter > len(self.animation_text):
            self.frame_counter = 0