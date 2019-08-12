"""
Class for an extension of the indicator class representing a progress bar indicator.
Draws a series of donechars and todochars to represent a progressbar

@author: Jakub Wlodek
"""

# clanimate + time imports
from clanimate import indicator
import time


class BarIndicator(indicator.Indicator):
    """
    Class for Progress Bar indicator. Extends base Indicator class

    Attributes
    ----------
    todo_char : char
        a character that will represent a task still to be completed
    done_char : char
        a character that will represent a completed task
    showcounter : bool
        Toggle for adding a counter of complete/todo to the progress bar

    Methods
    -------
    animate()
        implements the base class animate function
    """


    def __init__(self, num_elems, name='', color='None', todo_char='-', done_char='#', showcounter=False):
        """
        Constructor for the BarIndicator class. First calls superclass constructor, and then inits
        some attributes
        """

        super().__init__(num_elems, name=name, color=color)
        self.todo_char = todo_char
        self.done_char = done_char
        self.showcounter = showcounter


    def animate(self):
        """
        Animation function. Overrides base class. Writes done_char self.itemcounter times, 
        and then writes todo_char self.num_itmes - self.itemcounter times.
        """

        loading_bar = ''
        for i in range(0, self.item_counter):
            loading_bar = loading_bar + self.done_char
        for j in range(self.item_counter, self.num_elems):
            loading_bar = loading_bar + self.todo_char
        if self.showcounter:
            loading_bar = loading_bar + ' ({}/{})'.format(self.item_counter, self.num_elems)
        self.write(loading_bar)