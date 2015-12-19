#format rst

Various Musings
===============

* "Release early, release often." - Principles of 'DevOps_' / Continuous Integration in accord with the `Bermuda Principles`_.  Could such practices be applied to scientific data?  Is not programming code data in a sense?

  * DataOps_ - 'DevOps_ for Data Science'

    * a.k.a. data warehousing

* Thought: A machine-learning based scheduler for scientific workflow management.

  * Train on a few runs of a pipeline to determine memory, CPU needs (maybe use priors supplied by researcher or some heuristic).

  * Allow researchers to mark whether or not a pipeline has failed and have the classifier learn from this.

    * If the pipeline is marked as failed, allow the researcher to manually inspect the outputs of each step to determine which node is the culprit.

    * Use this data to predict future failures.  If a future failure seems plausible, notify the researcher, pause the pipeline, or some combination of these two.

    * If a failure happens often enough, request manual intervention/maintenance.

    .. ############################################################################

    .. _DevOps: ../DevOps

    .. _Bermuda Principles: https://en.wikipedia.org/wiki/Bermuda_Principles

    .. _DataOps: ../DataOps

