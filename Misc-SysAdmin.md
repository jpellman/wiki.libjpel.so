\#format rst

Miscellaneous
=============

This page contains miscellaneous snippets that I pick up that I haven't been able to group into bigger concepts yet.

-   uniq -c : 'prefix lines by the number of occurrences'
-   In the sudoers file : *\#includedir* is **not** a comment. It's a directive that points to supplemental config files. There are several other *\#include* directives. This mimics C syntax.
-   fail2ban : a great way to get rid of spammers / brute force attacks. Thanks Yarik!
-   bash : .. raw:: html  
    &\#91;

-   If an AWS S3 upload is [MultiPart](../MultiPart), the ETag attribute of an S3 bucket object is *not* an MD5 hash. It is the hashes for each part uploaded concatenated, plus a dash and the number of parts uploaded (see [here](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html)).
-   Display line numbers in vim : <http://vim.wikia.com/wiki/Display_line_numbers>
-   Switch from less to vim- ':wv'.
-   Exec last command in bash *!!*.
-   Check before replacing in vim :s/foo/bar/gc'
-   Apparently the Java heap makes use of the RAM allocated for buffer/cache (so the buffer/cache isn't freed up).
-   [Article on JVM Heap Size](https://www.yourkit.com/docs/kb/sizes.jsp) & [Oracle Docs on JVM Heap](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html)
-   An analogy: web/app servers / load balancers belong to the same sub-class of problems that HPC schedulers treat, but are just more narrow in scope.
-   HP iLO power button options: <https://www.experts-exchange.com/questions/27971206/HP-iLO.html>
-   A 301 redirect in nginx for HTTPS requires a cert because the packet needs to be decrypted for nginx to inspect the host field of the packet header.
-   git branch != git checkout for creating a new branch using the CLI.
-   [Keep Alive Client](https://en.wikipedia.org/wiki/HTTP_persistent_connection)
-   Variable expansion doesn't work with watch.

**Outside Links to be Sorted:**

> <http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages>
>
> <https://peteris.rocks/blog/htop/>
>
> <https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/>
>
> <http://linuxatemyram.com>
>
> <https://fedoraproject.org/wiki/Creating_GPG_Keys#Creating_GPG_Keys_Using_the_Command_Line>
>
> <http://www.crypt.gen.nz/papers/backup_encryption.html>
>
> <https://www.madboa.com/geek/gpg-quickstart>
>
> <http://explainshell.com/>

* * * * *

[SystemsAdministration](../SystemsAdministration)
