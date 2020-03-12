

Demystifying Old Python Scripts
===============================

Sometimes, fair adventurer, you may come across a Python script with sparse documentation. In that case, you should avail yourself of the following tools:

-   [pyan](http/github.cdavidfraspyan) - Creates a call dependency graph based off a static analysis of the script. Does not run code.
-   [pycallgraph](htt/pycallgraph.slowchop.cmast) - Actually needs to run the script (depends on the debugger). Creates a call graph using Gephi or Graphviz.

Next, if there are no docstrings for arguments, make them. Remove unused function code. Familiarize yourself with API modules used within the script. Refactor if necessary.

* * * * *

> Python
