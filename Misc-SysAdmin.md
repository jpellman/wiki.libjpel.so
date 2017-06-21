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
-   [Fiber (specialized form of thread)](https://en.wikipedia.org/wiki/Fiber_(computer_science))
-   [CAA](https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization) (combines SSL/TLS certificate file w/ a DNS record to increase security)
-   The -c flag for du caches file size estimates so that they can be retrieve more quickly on future invocations? ( [More reading](http://www.linfo.org/du.html) in addition to the man file)
-   [XKCD Password Generator](http://preshing.com/20110811/xkcd-password-generator/)
-   [Canned nginx Configs (to use as templates)](https://www.nginx.com/resources/wiki/start/)
-   Apparently KVM and Virtualbox are incompatible / can't be run simultaneously. See [here](http://www.dedoimedo.com/computers/kvm-virtualbox.html) for an idea on how to handle that.
-   Fast Boot as an issue with bootable thumb drives: <https://forums.freebsd.org/threads/58001/#post-331378>
-   Succinct overview of iptables: <https://wiki.centos.org/HowTos/Network/IPTables>
-   More readings of ZFS configurations: <https://calomel.org/zfs_raid_speed_capacity.html> , <https://www.delphix.com/blog/delphix-engineering/zfs-raidz-stripe-width-or-how-i-learned-stop-worrying-and-love-raidz>
-   cat /dev/null \> /path/to/log allows you to wipe a log without restarting any associated process / daemon
-   When a user is encountering timeout errors with SSH: <https://www.bjornjohansen.no/ssh-timeout>
-   strace references:
    -   <http://www.linuxintro.org/wiki/Strace:_what_a_process_does>
    -   <http://www.linux-magazine.com/Issues/2009/105/Practical-strace>
-   ZeroMQ references:
    -   <http://nichol.as/zeromq-an-introduction>
    -   <http://intothesaltmine.readthedocs.io/en/latest/chapters/command-and-control/zeromq.html>
    -   <https://news.ycombinator.com/item?id=2428004>
-   gpasswd - it exists ; it is a good way to remove users from groups etc
-   [modules](https://docs.saltstack.com/en/latest/salt-modindex.html) are often more useful than grains in getting system info in salt / just because a grain doesn't exist, doesn't mean there isn't an easy way to get it that's not cmd.run
-   <https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/>
-   <http://hackaday.com/2014/05/28/interview-inventing-the-unix-sudo-command/>
-   Type 'reset' when screen messes up your keyboard mapping.

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
>
> <https://istlsfastyet.com/>
>
> <https://hpbn.co/transport-layer-security-tls/>
>
> <http://www.linfo.org/main_index.html>
>
> <https://medium.com/@denisanikin/what-an-in-memory-database-is-and-how-it-persists-data-efficiently-f43868cff4c1>
>
> <https://icesquare.com/wordpress/how-to-improve-zfs-performance/>
>
> <https://teachyourselfcs.com>
>
> <https://mxtoolbox.com/SuperTool.aspx>
>
> [Why NFS Sucks](https://www.kernel.org/doc/ols/2006/ols2006v2-pages-59-72.pdf)

A slew of Application-level protocol readings:

-   <https://www.w3.org/History/19921103-hypertext/hypertext/WWW/Protocols/HTTP.html>
-   <https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html>
-   <https://daniel.haxx.se/docs/ftp-vs-http.html>

Wizards:

-   <http://www.kegel.com/>
-   <http://www.rodsbooks.com/>
-   <http://grymoire.com/>
-   <https://daniel.haxx.se/>
-   <http://everythingsysadmin.com/>

Documentation Projects:

-   <http://www.linfo.org/>
-   <http://www.tldp.org/>

* * * * *

[SystemsAdministration](../SystemsAdministration)
