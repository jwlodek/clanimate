import clanimate
import time

animator = clanimate.Animator('wheel', 10, name='Loading')
animator.start_animation()
time.sleep(3)
animator.end_animation()