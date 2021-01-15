import clanimate
import time

animator = clanimate.Animator('scroll_text', 10, name='Loading', sleep_time=0.1, animation_frames='...')
animator.start_animation()
time.sleep(3)
animator.end_animation()
