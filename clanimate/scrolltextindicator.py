"""
Class for the simplest implementation of the Indicator class,
a spinning wheel animation.

@author: Jakub Wlodek
"""

from clanimate import indicator
import time

class ScrollTextIndicator(indicator.Indicator):

    def __init__(self, num_elems, name='', color='None', sleep_time=0.1, animation_frames='...'):
        super().__init__(num_elems, name=name, color=color)
        self.sleep_time = sleep_time
        self.animation_text = animation_frames
        self.frame_counter = 0

    def animate(self):
        time.sleep(self.sleep_time)
        current_text = self.animation_text[0:self.frame_counter]
        self.write(current_text)
        self.frame_counter = self.frame_counter + 1
        if self.frame_counter > len(self.animation_text):
            self.frame_counter = 0