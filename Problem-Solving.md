

Problem Solving
===============

Difference-Reduction
--------------------

Means-End Analysis
------------------

An errant thought- might an application that is part of a stack might be considered an operator/tool in a way (i.e., your goal state is to have a web server, and you can use Apache as a means to attain that goal state)?

Problem Space and Trees
-----------------------

Functional Fixedness
--------------------

Set Effect
----------

Incubation Effects
------------------

Problems of Insight
-------------------

Breadth-First vs Depth-First Techniques for organizing problems
---------------------------------------------------------------

-   Breadth-first as making a spec / writing unit tests.

The Myst User's Manual
----------------------

This isn't really based off any empirical literature, but in a more applied sense I find the following quotation from the Myst user's manual to be sound advice for most any problem where you don't know what to do:

*Don’t thrash! If you’re not sure what to do next, clicking everywhere won’t help. Think about what you know already, ask yourself what you need to know, collect your thoughts, and piece them together. Think of related items or places you’ve seen, think of information you’ve been given, pay close attention to everything you see, and don’t forget anything. But most importantly - think of what you would do if you were really there. Remember, there is always [Google] if you need it...*

Working through the Stack
-------------------------

There are varying levels of analysis when you encounter a problem (i.e., OSI levels, dependencies). When troubleshooting it makes sense to treat each of these levels separately, first determining at what level the problem is occurring. So for instance, in a setup like the following:

-   haproxy
-   nginx
-   Apache
-   Application server

If a 503 server error is being propagated, you would first want to isolate which layer was causing the 503. You could accomplish this by perusing the logs at each level and comparing them.

Operators
---------

-   Increasing log verbosity- this should be a first step in troubleshooting/debugging.

References
----------

-   John R. Anderson - *Cognitive Psychology and its implications*
-   <http://cognitivepsychology.wikidot.com/cognition:problem-solving>

* * * * *

[Cognitive-Science](../Cognitive-Science)
