"""
Class for the simplest implementation of the Indicator class,
a spinning wheel animation.

@author: Jakub Wlodek
"""

from clanimate import indicator
import time

class BarIndicator(indicator.Indicator):


    def __init__(self, num_elems, name='', color='None', todo_char='-', done_char='#', showcounter=False):
        super().__init__(num_elems, name=name, color=color)
        self.todo_char = todo_char
        self.done_char = done_char
        self.showcounter = showcounter

    def animate(self):
        loading_bar = ''
        for i in range(0, self.item_counter):
            loading_bar = loading_bar + self.done_char
        for j in range(self.item_counter, self.num_elems):
            loading_bar = loading_bar + self.todo_char
        if self.showcounter:
            loading_bar = loading_bar + '({}/{})'.format(self.item_counter, self.num_elems)
        self.write(loading_bar)