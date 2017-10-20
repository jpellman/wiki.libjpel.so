\#format rst

Demystifying Old Python Scripts
===============================

Sometimes, fair adventurer, you may come across a Python script with sparse documentation. In that case, you should avail yourself of the following tools:

-   [[https://github.com/davidfraser/pyan|pyan](https://github.com/davidfraser/pyan|pyan)] - Creates a call dependency graph based off a static analysis of the script. Does not run code.
-   [[http://pycallgraph.slowchop.com/en/master/|pycallgraph](http://pycallgraph.slowchop.com/en/master/|pycallgraph)] - Actually needs to run the script (depends on the debugger). Creates a call graph using Gephi or Graphviz.

Next, if there are no docstrings for arguments, make them. Remove unused functions / code. Familiarize yourself with APIs / modules used within the script. Refactor if necessary.

* * * * *

> Python
