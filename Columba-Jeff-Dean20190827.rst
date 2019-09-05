#format rst

My Thoughts on Jeff Dean's 8/27/19 Deep Learning Presentation
=============================================================

Someone else did a `pretty okay summary`_ of this talk already, so I'm just going to add a few conjectures of my own to this page.  A lot of the presentation amounted to some form of "Look at this cool thing we did".  The demonstrations were indeed cool, but also oddly specific.  The thoughts below represent my distillation of what mattered the most in that talk to me.

.. contents:: :depth: 2

AutoML
------

Much as programmers used to produce primarily artisanal assembly code back before compilers (and larger memory/disk) became a thing, the current crop of data scientists produce artisanal machine learning models.  Just as a competent assembly programmer can produce hyper-optimized code by hand, an experienced data scientist can, with delicate care, produce a well-tuned model.  However, the individuals with this level of expertise are rare.

Given a set of constraints, Google's AutoML aims to evolve_ a machine learning model that is either "good enough" or in some cases better than a model that has been hand-tuned by a human.  This makes it functionally analogous to a modern compiler, which aims to take high-level specifications and convert them to an optimized form of machine code that is satisfactory or in some cases optimal.

Links
~~~~~

* Autocode_

* `Google AutoML`_

* AutoML_ (Wikipedia article about the field as a whole; not Google specific)

* `Google's AutoML: Cutting Through the Hype`_

* `AutoML from University of Freiburg`_

Neural Architecture Search
--------------------------

One challenge with creating machine learning models is that it's hard, long, and costly to get a model trained from scratch.  Google (and possibly other folks) proffer the following solution- if there are a number of pre-trained models out there that are close enough to what you need, you can take one of those pre-trained models and use it as a starting point when training for a new model.  This is conceptually similar (in my mind at least) to choosing a prior in Bayesian statistics.

These pre-trained models can be put together into a searchable "graph of expertise".

Links
~~~~~

* `Neural Architecture Search`_ (Wikipedia)

-------------------------

 MachineLearning_

.. ############################################################################

.. _pretty okay summary: https://medium.com/@anupradhan/recently-jeff-dean-from-google-gave-a-fascinating-presentation-at-columbia-university-bacf94efd1c8

.. _evolve: https://en.wikipedia.org/wiki/Neuroevolution

.. _Autocode: https://en.wikipedia.org/wiki/Autocode

.. _Google AutoML: https://cloud.google.com/automl/

.. _AutoML: https://en.wikipedia.org/wiki/Automated_machine_learning

.. _`Google's AutoML: Cutting Through the Hype`: https://www.fast.ai/2018/07/23/auto-ml-3/

.. _AutoML from University of Freiburg: https://www.automl.org

.. _Neural Architecture Search: https://en.wikipedia.org/wiki/Neural_architecture_search

.. _MachineLearning: ../MachineLearning

