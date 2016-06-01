\#format rst

Various Musings
===============

-   "Release early, release often." - Principles of '[DevOps](../DevOps)' / Continuous Integration in accord with the [Bermuda Principles](https://en.wikipedia.org/wiki/Bermuda_Principles). Could such practices be applied to scientific data? Is not programming code data in a sense?
    -   [DataOps](../DataOps) - '[DevOps](../DevOps) for Data Science'
        -   a.k.a. data warehousing
        -   Jupyter notebooks do for science what configuration management tools like Puppet/Chef do for systems administration.
-   Thought: A machine-learning based scheduler for scientific workflow management.
    -   Train on a few runs of a pipeline to determine memory, CPU needs (maybe use priors supplied by researcher or some heuristic).
    -   Allow researchers to mark whether or not a pipeline has failed and have the classifier learn from this.
        -   If the pipeline is marked as failed, allow the researcher to manually inspect the outputs of each step to determine which node is the culprit.
        -   Use this data to predict future failures. If a future failure seems plausible, notify the researcher, pause the pipeline, or some combination of these two.
        -   If a failure happens often enough, request manual intervention/maintenance.
-   There should be a facilitation method of connecting philanthropists/foundations to worthy projects based on the insights in Jon Kleinberg et al's social networks book.

