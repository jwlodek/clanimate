import clanimate
import time

animator = clanimate.Animator('progress_bar', 10, name='Loading', todo_char='-', done_char='#', showcounter=False)
animator.start_animation()
for i in range(10):
    time.sleep(1)
    animator.increment()
animator.end_animation()