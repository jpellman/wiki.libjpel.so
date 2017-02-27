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
-   [Article on JVM Heap Size](https://www.yourkit.com/docs/kb/sizes.jsp) & [Oracle Docs on JVM Heap](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html)

**Outside Links to be Sorted:**

> <http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages>
>
> <https://peteris.rocks/blog/htop/>
>
> <https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/>

* * * * *

[SystemsAdministration](../SystemsAdministration)