# clanimate

A python library for adding CLI loading bars and animations to your python scripts.

### Installation

Install with pip. Note that this library is still in an "alpha" state and is not guaranteed to be bug free in any way

```
pip install clanimate
```

### Usage

The basic usage of clanimate uses the `Animator` object. Then, simply call `start_animation()` to start the animation, and `end_animation()` once it is done.

```
import clanimate

animator = clanimate.Animator('wheel', 10, name='Loading')
animator.start_animation()
time.sleep(3)
animator.end_animation()
```
would be the most basic use case. The supported animator types are the `wheel` indicator, which shows a spinning character, the `bar` indicator which shows a progress bar, and the `scroll_text` indicator, which iterates through a string in a loop.
