\#format rst

Scientific Programming
======================

Conventional development techniques seem to be ill-suited for scientific programming, which is more focused on rapid prototyping than on producing stable, enterprise code that's supposed to run for long stretches of time. I'm going to spitball some ideas for how scientific programming methodologies might work here.

General Algorithm
-----------------

1.  Prototype in Jupyter notebook / an IDE / [JupyterLab](../JupyterLab).
2.  Convert notebook to plain, no-frills script.
3.  Create an interface to the script with something like argparse. This allows you to execute your script's logic via bash, which is a common environment that can access scripts written in many different languages.
4.  Wrap that interface in CWL so that it can work with a workflow scheduler / editor.
5.  Create a rudimentary GUI if your code requires human interaction with something like [Gooey](https://github.com/chriskiehl/Gooey).

* * * * *

> [ScientificComputing](../ScientificComputing)
