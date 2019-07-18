

class BarIndicator(Indicator):


    def __init__(self, name='', color='None', todo_char='-', done_char='#', showcounter=False):
        super().__init__(name=name, color=color)
        self.todo_char = todo_char
        self.done_char = done_char
        self.showcounter = showcounter