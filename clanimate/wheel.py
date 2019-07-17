"""
Class for the simplest implementation of the Indicator class,
a spinning wheel animation.

@author: Jakub Wlodek
"""

from clanimate import progressindicator
import time

class WheelIndicator(progressindicator.Indicator):

    def __init__(self, name='', color='None', sleep_time=0.1, animation_frames='|/-//'):
        super().__init__(name=name, color=color)
        self.sleep_time = sleep_time
        self.animation_frames = animation_frames


    def animate(self):
        self.is_running = True
        counter = 0
        while self.is_running:
            time.sleep(self.sleep_time)
            self.write(self.animation_frames[counter])
            counter = counter + 1
            if counter == len(self.animation_frames):
                counter = 0

