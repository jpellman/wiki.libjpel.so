 * Gollum/Grit/Rugged uses its own implementation of Git, which only respects Git hooks that are coded into a Ruby config file in some way (see [here](https://github.com/gollum/gollum/issues/69#issuecomment-281501178)).  This necessitates running `gollum --config ./scripts/config.rb`.
 * `build_subpages.py` needs to be run once every time the repo is cloned to install itself as a post-commit hook (or it needs to be added as a post-commit hook manually).
 * `build_subpages.py` requires a Python 3 environment with GitPython installed.

pandoc-bootstrap-template
=========================

Bootstrap template for Pandoc - Converts markdown files into Twitter Bootstrap styled HTML

This version has been modified so that the file fed into `--include-before-body` is placed in a sidebar on the righthand side, and the TOC is placed before the body of the main text.

### Usage example

    pandoc -f markdown -t html -o Charities.html --template=template.html --include-after-body=_Footer.html --include-before-body=_Sidebar.html --toc --toc-depth=2 --metadata title=Charities --css template.css --self-contained Charities.md
