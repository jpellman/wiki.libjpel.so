

Miscellaneous
=============

This page contains miscellaneous snippets that I pick up that I haven't been able to group into bigger concepts yet.

-   In the sudoers file : *\#includedir* is **not** a comment. It's a directive that points to supplemental config files. There are several other *\#include* directives. This mimics C syntax.
-   fail2ban : a great way to get rid of spammers / brute force attacks. Thanks Yarik!
-   HP iLO power button options: <https://www.experts-exchange.com/questions/27971206/HP-iLO.html>
-   git branch != git checkout for creating a new branch using the CLI.
-   [Fiber (specialized form of thread)](https://en.wikipedia.org/wiki/Fiber_(computer_science))
-   cat /dev/null \> /path/to/log allows you to wipe a log without restarting any associated process / daemon
-   ZeroMQ references:
    -   <http://nichol.as/zeromq-an-introduction>
    -   <http://intothesaltmine.readthedocs.io/en/latest/chapters/command-and-control/zeromq.html>
    -   <https://news.ycombinator.com/item?id=2428004>
-   gpasswd - it exists ; it is a good way to remove users from groups etc
-   [modules](https://docs.saltstack.com/en/latest/salt-modindex.html) are often more useful than grains in getting system info in salt / just because a grain doesn't exist, doesn't mean there isn't an easy way to get it that's not cmd.run

**Outside Links to be Sorted:**

> <https://teachyourselfcs.com> <https://www.aosabook.org>

* * * * *

[Systems-Administration](../Systems-Administration)
