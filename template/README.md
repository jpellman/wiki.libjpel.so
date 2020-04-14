pandoc-bootstrap-template
=========================

Bootstrap template for Pandoc - Converts markdown files into Twitter Bootstrap styled HTML

This version has been modified so that the file fed into `--include-before-body` is placed in a sidebar on the righthand side, and the TOC is placed before the body of the main text.

### Usage example

    pandoc -f markdown -t html -o Charities.html --template=template.html --include-after-body=_Footer.html --include-before-body=_Sidebar.html --toc --toc-depth=2 --metadata title=Charities --css template.css --self-contained Charities.md
