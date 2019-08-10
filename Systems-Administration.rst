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

Bash / Scripting Languages
--------------------------

* Explainshell_

* Exec last command in bash *!!*.

* Variable expansion doesn't work with watch (8/10/19 - I'm not sure I believe this- I might just have been doing something with single quotes instead of double quotes)

* The -c flag for du caches file size estimates so that they can be retrieve more quickly on future invocations? ( `More reading`_ in addition to the man file)

* Type 'reset' when screen messes up your keyboard mapping.

* uniq -c : 'prefix lines by the number of occurrences'

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

Storage
-------

* `Why NFS Sucks`_

* `How to improve ZFS performance`_

* `ZFS RAID Speed Capacity`_

* `How I learned to stop worrying and love RAIDZ`_

* `Lustre and Panasas Are Not So Different`_

* `Backblaze Hard Drive Reliability Stats, Q1 2016`_

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

-------------------------

 CategoryCategory_

.. ############################################################################

.. _UEFI Boot - How Does that Actually Work Then?: https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/

.. _Fast Boot as an issue with bootable thumb drives: https://forums.freebsd.org/threads/58001/#post-331378

.. _Explainshell: http://explainshell.com/

.. _More reading: http://www.linfo.org/du.html

.. _Understanding Load Averages: http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages

.. _`Strace: What a Process Does`: http://www.linuxintro.org/wiki/Strace:_what_a_process_does

.. _Practical strace: http://www.linux-magazine.com/Issues/2009/105/Practical-strace

.. _Linux Ate My RAM: http://linuxatemyram.com

.. _Article on JVM Heap Size: https://www.yourkit.com/docs/kb/sizes.jsp

.. _Oracle Docs on JVM Heap: https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html

.. _Succinct overview of iptables: https://wiki.centos.org/HowTos/Network/IPTables

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

.. _Why NFS Sucks: https://www.kernel.org/doc/ols/2006/ols2006v2-pages-59-72.pdf

.. _How to improve ZFS performance: https://icesquare.com/wordpress/how-to-improve-zfs-performance/

.. _ZFS RAID Speed Capacity: https://calomel.org/zfs_raid_speed_capacity.html

.. _How I learned to stop worrying and love RAIDZ: https://www.delphix.com/blog/delphix-engineering/zfs-raidz-stripe-width-or-how-i-learned-stop-worrying-and-love-raidz

.. _Lustre and Panasas Are Not So Different: http://clusterdesign.org/2012/08/lustre-and-panasas-are-not-so-different/

.. _Backblaze Hard Drive Reliability Stats, Q1 2016: https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/

.. _Canned nginx Configs (to use as templates): https://www.nginx.com/resources/wiki/start/

.. _What an in-memory database is and how it persists data efficiently: https://medium.com/@denisanikin/what-an-in-memory-database-is-and-how-it-persists-data-efficiently-f43868cff4c1

.. _here: http://www.dedoimedo.com/computers/kvm-virtualbox.html

.. _Xen Networking: https://wiki.xenproject.org/wiki/Xen_Networking

.. _Importing an OVA into KVM: https://wiki.hackzine.org/sysadmin/kvm-import-ova.html

.. _MultiPart: ../MultiPart

.. _CategoryCategory: ../CategoryCategory

