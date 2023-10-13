__all__ = ['core', 'figure', 'semantics', 'html', 'utils', '__main__']

__version_info__ = (0, 4, 1)
__release__ = False
__version__ = ".".join(str(i) for i in __version_info__)
if not __release__:
    __version__ = __version__ + "-a1"

import svgling.core

draw_tree = svgling.core.draw_tree
tree2svg = svgling.core.tree2svg

disable_nltk_png = svgling.core.disable_nltk_png
