 \#\# master-page:CategoryTemplate \#\# master-date:Unknown-Date

Systems Administration Notes
============================

This page stores both generic notes, as well as additional pages and categories related to systems administration. My general modus operandi here is to start taking notes here, and then to break things out into separate pages when they get too large.

List of pages in this category:
-------------------------------

[[FullSearchCached(category:Systems-Administration)]]\_

General Links
-------------

### Documentation Projects

-   <htt/www.linfo.o>
-   <htt/www.tldp.o>

### Blog Sysadmin Sites

-   <htt/www.kegel.c>
-   <htt/www.rodsbooks.c>
-   <htt/grymoire.c>
-   <http/daniel.haxx.>
-   <htt/everythingsysadmin.c>
-   <http/www.kennethreitz.org>
-   <htt/www.guppylake.c~n>
-   <http/brendangregg.com> - Emphasis on monitoring
-   <http/pthree.o> - Emphasis on storag ZFS
-   <http/sysadmincasts.com>

Bootloaders
-----------

-   [UEFI Boot - How Does that Actually Work Then?](http/www.happyassassin.n20uefi-boot-how-does-that-actually-work-th)
-   [Fast Boot as an issue with bootable thumb drives](http/forums.freebsd.othrea580#post-331378)

Scripting Languages
-------------------

-   [Python](Python)

### Bash

-   [Explainshell](htt/explainshell.c)
-   Exec last command in bash *!!*.
-   Variable expansion doesn't work with watch 19 - I'm not sure I believe this- I might just have been doing something with single quotes instead of double quotes)
-   The -c flag for du caches file size estimates so that they can be retrieve more quickly on future invocations? ( [More reading](htt/www.linfo.odu.html) in addition to the man file)
-   Type 'reset' when screen messes up your keyboard mapping.
-   uniq -c : 'prefix lines by the number of occurrences'
-   <htt/wiki.bash-hackers.ohowredirection_tutorial>
-   <htt/sebug.npaplinLinux%20Shell%20Scripting%20Tutorial%20v2.0.pdf>
-   <htt/tldp.oHOWBash-Prog-Intro-HOWTO-3.html>
-   <htt/tldp.oHOWBash-Prog-Intro-HOWTO-4.html>
-   -   [Common Bash Pitfalls](htt/mywiki.wooledge.oBashPitfalls)
-   [Writing Robust Shell Scripts](htt/www.davidpashley.carticlwriting-robust-shell-scrip)
-   [CommandlineFu](htt/commandlinefu.c)
-   [Good summary of redirectio control operators](http/unix.stackexchange.ca/159514)
-   [Where I learned that Here strings need to have quotes around the word to be interpreted as string literals](http/en.wikipedia.owiHere_document#Here_strings)

### Regular Expressions

-   [RegEx Golf](http/regex.alf.)
-   [Regular Expressions by Jan Goyvaerts](htt/www.regular-expressions.info)

Monitorin Debugging
----------------------

-   [Understanding Load Averages](htt/blog.scoutapp.carticl20understanding-load-averages)
-   [Strace: What a Process Does](htt/www.linuxintro.owiStrace:_what_a_process_does)
-   [Practical strace](htt/www.linux-magazine.cIssu201Practical-strace)

### Memory

-   [Linux Ate My RAM](htt/linuxatemyram.com)
-   Apparently the Java heap makes use of the RAM allocated for buffcache (so the buffcache isn't freed up).
-   [Article on JVM Heap Size](http/www.yourkit.cdosizes.jsp) & [Oracle Docs on JVM Heap](http/docs.oracle.cE13150_jrockit_jjrockgenindiagngarbage_collect.html)

Networking
----------

-   [Succinct overview of iptables](http/wiki.centos.oHowTNetwoIPTables)
-   [QUIC at 10,000 feet](http/docs.google.cdocumed/1gY9-YNDNAB1eip-RTPbqphgySwSNSDHLq9D5Bty4Fedit)
-   [netstat overview](htt/tldp.oLnax-087-2-iface.netstat.html)
-   [Cheat Sheet for IP command](http/access.redhat.csitdefaufilattachmenrh_ip_command_cheatsheet_1214_jcs_print.pdf)

### Application-Layer Protocols

#### HTTP

-   [Keep Alive Client](http/en.wikipedia.owiHTTP_persistent_connection)
-   <http/www.w3.oHisto19921103-hypertehyperteWProtocoHTTP.html>
-   <http/www.ntu.edu.hoehchprogrammiwebprogrammiHTTP_Basics.html>
-   <http/daniel.haxx.doftp-vs-http.html>
-   [What inspired my interest in this topic](http/news.ycombinator.citem?id=13075355)

### TCPDump Tutorials

-   <htt/www.alexonlinux.ctcpdump-for-dummies>
-   <htt/bencane.c20quick-and-practical-reference-for-tcpdu>
-   <http/www.quora.cWhat-is-the-difference-between-TCPs-FIN-and-RST-packets>

Security
--------

-   [Strong Ciphers for Web Servers](http/cipherli.)
-   [SSL Labs](http/www.ssllabs.c) (assesses your site's security)
-   [Is TLS fast yet?](http/istlsfastyet.c)
-   [TLS Overview](http/hpbn.transport-layer-security-t) (chapter of an O'Reilly book)
-   [CAA](http/en.wikipedia.owiDNS_Certification_Authority_Authorization) (combines STLS certificate file a DNS record to increase security)
-   [GPG Quickstart](http/www.madboa.cgegpg-quickstart)
-   [Creating GPG Keys Using the CLI](http/fedoraproject.owiCreating_GPG_Keys#Creating_GPG_Keys_Using_the_Command_Line)
-   [Backup Encryption](htt/www.crypt.gen.papebackup_encryption.html)
-   [Inventing the Sudo Command](htt/hackaday.c20interview-inventing-the-unix-sudo-comma)
-   [XKCD Password Generator](htt/preshing.c201108xkcd-password-generat)
-   [Another XKCD Password Generator](htt/correcthorsebatterystaple.n)
-   [Dangerous Sudoers Entries](http/blog.compass-security.c20dangerous-sudoers-entries-part-4-wildcar)
-   [Stop Disabling SELinux](http/stopdisablingselinux.c)

Storage
-------

-   [Why NFS Sucks](http/www.kernel.odo20ols2006v2-pages-59-72.pdf)
-   [How to improve ZFS performance](http/icesquare.cwordprehow-to-improve-zfs-performan)
-   [ZFS RAID Speed Capacity](http/calomel.ozfs_raid_speed_capacity.html)
-   [How I learned to stop worrying and love RAIDZ](http/www.delphix.cbldelphix-engineerizfs-raidz-stripe-width-or-how-i-learned-stop-worrying-and-love-raidz)
-   [Lustre and Panasas Are Not So Different](htt/clusterdesign.o20lustre-and-panasas-are-not-so-differe)
-   [Backblaze Hard Drive Reliability Stats, Q1 2016](http/www.backblaze.cblhard-drive-reliability-stats-q1-20)
-   [NDMP](http/www.snia.ondmp) (Description and whitepaper)
-   <htt/www.tldp.oLintro-linhtsect_03_01.html>
-   [Does Writing to NFS Put Processes into Uninterruptible Sleep?](http/medium.c@jonphilpodoes-writing-to-nfs-put-processes-into-un-interruptible-sleep-d58790cd13b6#.h4oi0ufqx)
-   [Create LUKS](htt/redhat-admin.blogspot.c20create-and-configure-luks-encrypted.html)

### ACLs

-   [En Francais](htt/okki666.free.docmastarticllinux100.htm)
-   <http/wiki.archlinux.oindex.pAccess_Control_Lists>
-   <http/www.freebsd.odhandbofs-acl.html>

### RAID-5

A list of pages discussing why not to use RAID5:

-   <http/news.ycombinator.citem?id=8306499>
-   <http/www.reddit.cr/sysadmcommenydidell_raid_5_is_no_longer_recommended_for_a>
-   <http/www.reddit.cr/sysadmcommen3yocraid_5raid_10_tradeo> (in which we learn that RAID5 works for SSDs)

An article on the RAID "write-hole", which seems to be especially salient for RAID5:

-   <htt/www.raid-recovery-guide.craid5-write-hole.aspx>

### Tape

-   tar tvf **\<device\_name\>** - Read the file name from the tar header for the current file that the tape is pointed at.

### Database vs Filesystem

-   <http/stackoverflow.cquestio381208database-vs-file-system-storage>
-   <http/softwareengineering.stackexchange.cquestio1904why-use-a-database-instead-of-just-saving-your-data-to-disk>
-   <http/dzone.carticlwhich-is-better-saving-files-in-database-or-in-fil>

Identity Managemen User Management
-------------------------------------

-   <http/access.redhat.cdocumentatien-Red_Hat_Enterprise_Lin7/htSystem_Administrators_Guis1-users-tools.html>
-   [Introduction to LDAP](htt/ldapman.oarticlintro_to_ldap.html)

Applications
------------

### Web Servers

-   An analogy: wapp server load balancers belong to the same sub-class of problems that HPC schedulers treat, but are just more narrow in scope.
-   A 301 redirect in nginx for HTTPS requires a cert because the packet needs to be decrypted for nginx to inspect the host field of the packet header.
-   [Canned nginx Configs (to use as templates)](http/www.nginx.cresourcwista)

### Databases

-   <htt/philip.greenspun.cs>
-   [What an in-memory database is and how it persists data efficiently](http/medium.c@denisanikwhat-an-in-memory-database-is-and-how-it-persists-data-efficiently-f43868cff4c1)
-   [What are pros and cons of PostgreSQL and MySQL? With respect to reliability, speed, scalability, and features.](http/www.quora.cWhat-are-pros-and-cons-of-PostgreSQL-and-MySQL-With-respect-to-reliability-speed-scalability-and-features)

Virtualization
--------------

-   Apparently KVM and Virtualbox are incompatibl can't be run simultaneously. See [here](htt/www.dedoimedo.ccomputekvm-virtualbox.html) for an idea on how to handle that (or just don't do that at all because it doesn't make too much sense to begin with- quoth the older and wiser me).
-   [Xen Networking](http/wiki.xenproject.owiXen_Networking)
-   [Importing an OVA into KVM](http/wiki.hackzine.osysadmkvm-import-ova.html)

Containerization
----------------

-   [Kubernetes: An Overview](http/thenewstack.kubernetes-an-overvi)
-   [Docker for Data Science](http/www.amazon.cDocker-Data-Science-Extensible-Infrastructu1484230116)
-   [Docker Security Cheat Sheet](http/github.cOWACheatSheetSeriblmastcheatsheeDocker_Security_Cheat_Sheet.md)

Cloud Computing
---------------

-   If an AWS S3 upload is [MultiPart](MultiPart), the ETag attribute of an S3 bucket object is *not* an MD5 hash. It is the hashes for each part uploaded concatenated, plus a dash and the number of parts uploaded (see [here](htt/docs.aws.amazon.cAmazonlateARESTCommonResponseHeaders.html)).

### S3-compatible object stores

-   <http/minio.>
-   <http/cloudian.c>
-   <http/wasabi.c>
-   <htt/pithos.>
-   <http/www.zenko.>
-   <http/leo-project.nleo>
-   <http/github.ceucalypteucalyptwiWalrus-S3-API>
-   <htt/docs.ceph.cdomastrados>

Tools
-----

-   [Atop](htt/www.atoptool.)
-   [Gas Hosts](http/github.c2ndalpgasmask)
-   [last](http/linux.die.nm1/last) (can show reboot times)
-   [lastlog](http/linux.die.nm8/lastlog) (can show last login for a user- with decently informative timestamp)
-   <http/mxtoolbox.cSuperTool.aspx>
-   <http/peteris.rocblht>
-   <htt/md5deep.sourceforge.n>
-   [GNU Parallel](htt/www.shakthimaan.cpos20gnu-parallnews.html)

* * * * *

> [CategoryCategory](CategoryCategory)
