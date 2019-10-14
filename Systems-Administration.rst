#format rst
## master-page:CategoryTemplate
## master-date:Unknown-Date

Systems Administration Notes
============================

This page stores both generic notes, as well as additional pages and categories related to systems administration.  My general modus operandi here is to start taking notes here, and then to break things out into separate pages when they get too large.

.. contents::

List of pages in this category:
-------------------------------

`[[FullSearchCached(category:SystemsAdministration)]]`_

General Links
-------------

Documentation Projects
~~~~~~~~~~~~~~~~~~~~~~

* http://www.linfo.org/

* http://www.tldp.org/

Blogs / Sysadmin Sites
~~~~~~~~~~~~~~~~~~~~~~

* http://www.kegel.com/

* http://www.rodsbooks.com/

* http://grymoire.com/

* https://daniel.haxx.se/

* http://everythingsysadmin.com/

* https://www.kennethreitz.org

* http://www.guppylake.com/~nsb/

* https://brendangregg.com - Emphasis on monitoring

* https://pthree.org/ - Emphasis on storage / ZFS

* https://sysadmincasts.com

Bootloaders
-----------

* `UEFI Boot - How Does that Actually Work Then?`_

* `Fast Boot as an issue with bootable thumb drives`_

Scripting Languages
-------------------

* Python_

Bash
~~~~

* Explainshell_

* Exec last command in bash *!!*.

* Variable expansion doesn't work with watch (8/10/19 - I'm not sure I believe this- I might just have been doing something with single quotes instead of double quotes)

* The -c flag for du caches file size estimates so that they can be retrieve more quickly on future invocations? ( `More reading`_ in addition to the man file)

* Type 'reset' when screen messes up your keyboard mapping.

* uniq -c : 'prefix lines by the number of occurrences'

* http://wiki.bash-hackers.org/howto/redirection_tutorial

* http://sebug.net/paper/os/linux/Linux%20Shell%20Scripting%20Tutorial%20v2.0.pdf

* http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html

* http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html

* .. raw:: html
     &#91;

  .. raw:: html
     &#91;

   ${var} =~ "foo" .. raw:: html
     &#93;

  .. raw:: html
     &#93;

   - check if a string contains a substring "foo"

* `Common Bash Pitfalls`_

* `Writing Robust Shell Scripts`_

* CommandlineFu_

Regular Expressions
~~~~~~~~~~~~~~~~~~~

* `RegEx Golf`_

* `Regular Expressions by Jan Goyvaerts`_

Monitoring / Debugging
----------------------

* `Understanding Load Averages`_

* `Strace: What a Process Does`_

* `Practical strace`_

Memory
~~~~~~

* `Linux Ate My RAM`_

* Apparently the Java heap makes use of the RAM allocated for buffer/cache (so the buffer/cache isn't freed up).

* `Article on JVM Heap Size`_ & `Oracle Docs on JVM Heap`_

Networking
----------

* `Succinct overview of iptables`_

* `QUIC at 10,000 feet`_

* `netstat overview`_

* `Cheat Sheet for IP command`_

Application-Layer Protocols
~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTTP
::::

* `Keep Alive Client`_

* https://www.w3.org/History/19921103-hypertext/hypertext/WWW/Protocols/HTTP.html

* https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html

* https://daniel.haxx.se/docs/ftp-vs-http.html

* `What inspired my interest in this topic`_

TCPDump Tutorials
~~~~~~~~~~~~~~~~~

* http://www.alexonlinux.com/tcpdump-for-dummies

* http://bencane.com/2014/10/13/quick-and-practical-reference-for-tcpdump/

* https://www.quora.com/What-is-the-difference-between-TCPs-FIN-and-RST-packets

Security
--------

* `Strong Ciphers for Web Servers`_

* `SSL Labs`_ (assesses your site's security)

* `Is TLS fast yet?`_

* `TLS Overview`_ (chapter of an O'Reilly book)

* CAA_ (combines SSL/TLS certificate file w/ a DNS record to increase security)

* `GPG Quickstart`_

* `Creating GPG Keys Using the CLI`_

* `Backup Encryption`_

* `Inventing the Sudo Command`_

* `XKCD Password Generator`_

* `Another XKCD Password Generator`_

* `Dangerous Sudoers Entries`_

* `Stop Disabling SELinux`_

Storage
-------

* `Why NFS Sucks`_

* `How to improve ZFS performance`_

* `ZFS RAID Speed Capacity`_

* `How I learned to stop worrying and love RAIDZ`_

* `Lustre and Panasas Are Not So Different`_

* `Backblaze Hard Drive Reliability Stats, Q1 2016`_

* NDMP_ (Description and whitepaper)

* http://www.tldp.org/LDP/intro-linux/html/sect_03_01.html

* `Does Writing to NFS Put Processes into Uninterruptible Sleep?`_

* `Create LUKS`_

ACLs
~~~~

* `En Francais`_

* https://wiki.archlinux.org/index.php/Access_Control_Lists

* https://www.freebsd.org/doc/handbook/fs-acl.html

RAID-5
~~~~~~

A list of pages discussing why not to use RAID5:

* https://news.ycombinator.com/item?id=8306499

* https://www.reddit.com/r/sysadmin/comments/ydi6i/dell_raid_5_is_no_longer_recommended_for_any/

* https://www.reddit.com/r/sysadmin/comments/3yoc9z/raid_5raid_10_tradeoff/ (in which we learn that RAID5 works for SSDs)

An article on the RAID "write-hole", which seems to be especially salient for RAID5:

* http://www.raid-recovery-guide.com/raid5-write-hole.aspx

Identity Management / User Management
-------------------------------------

* https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/s1-users-tools.html

* `Introduction to LDAP`_

Applications
------------

Web Servers
~~~~~~~~~~~

* An analogy: web/app servers / load balancers belong to the same sub-class of problems that HPC schedulers treat, but are just more narrow in scope.

* A 301 redirect in nginx for HTTPS requires a cert because the packet needs to be decrypted for nginx to inspect the host field of the packet header.

* `Canned nginx Configs (to use as templates)`_

Databases
~~~~~~~~~

* http://philip.greenspun.com/sql/

* `What an in-memory database is and how it persists data efficiently`_

Virtualization
--------------

* Apparently KVM and Virtualbox are incompatible / can't be run simultaneously.  See here_ for an idea on how to handle that (or just don't do that at all because it doesn't make too much sense to begin with- quoth the older and wiser me).

* `Xen Networking`_

* `Importing an OVA into KVM`_

Cloud Computing
---------------

* If an AWS S3 upload is MultiPart_, the ETag attribute of an S3 bucket object is *not* an MD5 hash.  It is the hashes for each part uploaded concatenated, plus a dash and the number of parts uploaded (see `here <http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html>`__).

S3-compatible object stores
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* https://minio.io/

* https://cloudian.com/

* https://wasabi.com/

* http://pithos.io/

* https://www.zenko.io/

* https://leo-project.net/leofs/

* https://github.com/eucalyptus/eucalyptus/wiki/Walrus-S3-API

* http://docs.ceph.com/docs/master/radosgw/s3/

Tools
-----

* Atop_

* `Gas Hosts`_

* last_ (can show reboot times)

* lastlog_ (can show last login for a user- with decently informative timestamp)

* https://mxtoolbox.com/SuperTool.aspx

* https://peteris.rocks/blog/htop/

* http://md5deep.sourceforge.net/

* `GNU Parallel`_

-------------------------

 CategoryCategory_

.. ############################################################################

.. _UEFI Boot - How Does that Actually Work Then?: https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/

.. _Fast Boot as an issue with bootable thumb drives: https://forums.freebsd.org/threads/58001/#post-331378

.. _Python: ../Python

.. _Explainshell: http://explainshell.com/

.. _More reading: http://www.linfo.org/du.html

.. _Common Bash Pitfalls: http://mywiki.wooledge.org/BashPitfalls

.. _Writing Robust Shell Scripts: http://www.davidpashley.com/articles/writing-robust-shell-scripts/

.. _CommandlineFu: http://commandlinefu.com/

.. _RegEx Golf: https://regex.alf.nu/

.. _Regular Expressions by Jan Goyvaerts: http://www.regular-expressions.info

.. _Understanding Load Averages: http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages

.. _`Strace: What a Process Does`: http://www.linuxintro.org/wiki/Strace:_what_a_process_does

.. _Practical strace: http://www.linux-magazine.com/Issues/2009/105/Practical-strace

.. _Linux Ate My RAM: http://linuxatemyram.com

.. _Article on JVM Heap Size: https://www.yourkit.com/docs/kb/sizes.jsp

.. _Oracle Docs on JVM Heap: https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html

.. _Succinct overview of iptables: https://wiki.centos.org/HowTos/Network/IPTables

.. _QUIC at 10,000 feet: https://docs.google.com/document/d/1gY9-YNDNAB1eip-RTPbqphgySwSNSDHLq9D5Bty4FSU/edit

.. _netstat overview: http://tldp.org/LDP/nag2/x-087-2-iface.netstat.html

.. _Cheat Sheet for IP command: https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf

.. _Keep Alive Client: https://en.wikipedia.org/wiki/HTTP_persistent_connection

.. _What inspired my interest in this topic: https://news.ycombinator.com/item?id=13075355

.. _Strong Ciphers for Web Servers: https://cipherli.st/

.. _SSL Labs: https://www.ssllabs.com/

.. _Is TLS fast yet?: https://istlsfastyet.com/

.. _TLS Overview: https://hpbn.co/transport-layer-security-tls/

.. _CAA: https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization

.. _GPG Quickstart: https://www.madboa.com/geek/gpg-quickstart

.. _Creating GPG Keys Using the CLI: https://fedoraproject.org/wiki/Creating_GPG_Keys#Creating_GPG_Keys_Using_the_Command_Line

.. _Backup Encryption: http://www.crypt.gen.nz/papers/backup_encryption.html

.. _Inventing the Sudo Command: http://hackaday.com/2014/05/28/interview-inventing-the-unix-sudo-command/

.. _XKCD Password Generator: http://preshing.com/20110811/xkcd-password-generator/

.. _Another XKCD Password Generator: http://correcthorsebatterystaple.net/

.. _Dangerous Sudoers Entries: https://blog.compass-security.com/2012/10/dangerous-sudoers-entries-part-4-wildcards/

.. _Stop Disabling SELinux: https://stopdisablingselinux.com/

.. _Why NFS Sucks: https://www.kernel.org/doc/ols/2006/ols2006v2-pages-59-72.pdf

.. _How to improve ZFS performance: https://icesquare.com/wordpress/how-to-improve-zfs-performance/

.. _ZFS RAID Speed Capacity: https://calomel.org/zfs_raid_speed_capacity.html

.. _How I learned to stop worrying and love RAIDZ: https://www.delphix.com/blog/delphix-engineering/zfs-raidz-stripe-width-or-how-i-learned-stop-worrying-and-love-raidz

.. _Lustre and Panasas Are Not So Different: http://clusterdesign.org/2012/08/lustre-and-panasas-are-not-so-different/

.. _Backblaze Hard Drive Reliability Stats, Q1 2016: https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/

.. _NDMP: https://www.snia.org/ndmp

.. _Does Writing to NFS Put Processes into Uninterruptible Sleep?: https://medium.com/@jonphilpott/does-writing-to-nfs-put-processes-into-un-interruptible-sleep-d58790cd13b6#.h4oi0ufqx

.. _Create LUKS: http://redhat-admin.blogspot.com/2011/09/create-and-configure-luks-encrypted.html

.. _En Francais: http://okki666.free.fr/docmaster/articles/linux100.htm

.. _Introduction to LDAP: http://ldapman.org/articles/intro_to_ldap.html

.. _Canned nginx Configs (to use as templates): https://www.nginx.com/resources/wiki/start/

.. _What an in-memory database is and how it persists data efficiently: https://medium.com/@denisanikin/what-an-in-memory-database-is-and-how-it-persists-data-efficiently-f43868cff4c1

.. _here: http://www.dedoimedo.com/computers/kvm-virtualbox.html

.. _Xen Networking: https://wiki.xenproject.org/wiki/Xen_Networking

.. _Importing an OVA into KVM: https://wiki.hackzine.org/sysadmin/kvm-import-ova.html

.. _MultiPart: ../MultiPart

.. _Atop: http://www.atoptool.nl/

.. _Gas Hosts: https://github.com/2ndalpha/gasmask

.. _last: https://linux.die.net/man/1/last

.. _lastlog: https://linux.die.net/man/8/lastlog

.. _GNU Parallel: http://www.shakthimaan.com/posts/2014/11/27/gnu-parallel/news.html

.. _CategoryCategory: ../CategoryCategory

