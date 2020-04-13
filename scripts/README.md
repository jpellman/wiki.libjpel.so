 * Gollum/Grit/Rugged uses its own implementation of Git, which only respects Git hooks that are coded into a Ruby config file in some way (see [here](https://github.com/gollum/gollum/issues/69#issuecomment-281501178)).  This necessitates running `gollum --config ./scripts/config.rb`.
 * `build_subpages.py` needs to be run once every time the repo is cloned to install itself as a post-commit hook (or it needs to be added as a post-commit hook manually).
 * `build_subpages.py` requires a Python 3 environment with GitPython installed.
