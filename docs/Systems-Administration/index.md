Systems Administration Notes
============================

This page stores both generic notes, as well as additional pages and categories related to systems administration. My general modus operandi here is to start taking notes here, and then to break things out into separate pages when they get too large.

General Links
-------------

### Documentation Projects

-   <http://www.linfo.org/>
-   <http://www.tldp.org/>

### Blogs / Sysadmin Sites

-   <http://www.kegel.com/>
-   <http://www.rodsbooks.com/>
-   <http://grymoire.com/>
-   <https://daniel.haxx.se/>
-   <http://everythingsysadmin.com/>
-   <https://www.kennethreitz.org>
-   <http://www.guppylake.com/~nsb/>
-   <https://brendangregg.com> - Emphasis on monitoring
-   <https://pthree.org/> - Emphasis on storage / ZFS
-   <https://sysadmincasts.com>

Bootloaders
-----------

-   [UEFI Boot - How Does that Actually Work Then?](https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/)
-   [Fast Boot as an issue with bootable thumb drives](https://forums.freebsd.org/threads/58001/#post-331378)

Scripting Languages
-------------------

-   [Python](Python)

### Bash

-   [Explainshell](http://explainshell.com/)
-   Exec last command in bash *!!*.
-   Variable expansion doesn't work with watch (8/10/19 - I'm not sure I believe this- I might just have been doing something with single quotes instead of double quotes)
-   The -c flag for du caches file size estimates so that they can be retrieve more quickly on future invocations? ( [More reading](http://www.linfo.org/du.html) in addition to the man file)
-   Type 'reset' when screen messes up your keyboard mapping.
-   uniq -c : 'prefix lines by the number of occurrences'
-   <http://wiki.bash-hackers.org/howto/redirection_tutorial>
-   <http://sebug.net/paper/os/linux/Linux%20Shell%20Scripting%20Tutorial%20v2.0.pdf>
-   <http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html>
-   <http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html>
-   -   [Common Bash Pitfalls](http://mywiki.wooledge.org/BashPitfalls)
-   [Writing Robust Shell Scripts](http://www.davidpashley.com/articles/writing-robust-shell-scripts/)
-   [CommandlineFu](http://commandlinefu.com/)
-   [Good summary of redirection / control operators](https://unix.stackexchange.com/a/159514)
-   [Where I learned that Here strings need to have quotes around the word to be interpreted as string literals](https://en.wikipedia.org/wiki/Here_document#Here_strings)

### Regular Expressions

-   [RegEx Golf](https://regex.alf.nu/)
-   [Regular Expressions by Jan Goyvaerts](http://www.regular-expressions.info)

Monitoring / Debugging
----------------------

-   [Understanding Load Averages](http://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages)
-   [Strace: What a Process Does](http://www.linuxintro.org/wiki/Strace:_what_a_process_does)
-   [Practical strace](http://www.linux-magazine.com/Issues/2009/105/Practical-strace)

### Memory

-   [Linux Ate My RAM](http://linuxatemyram.com)
-   Apparently the Java heap makes use of the RAM allocated for buffer/cache (so the buffer/cache isn't freed up).
-   [Article on JVM Heap Size](https://www.yourkit.com/docs/kb/sizes.jsp) & [Oracle Docs on JVM Heap](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/garbage_collect.html)
-   [Memory Subsystem Deep Dive](https://frankdenneman.nl/2015/02/18/memory-configuration-scalability-blog-series/)

Networking
----------

-   [Succinct overview of iptables](https://wiki.centos.org/HowTos/Network/IPTables)
-   [QUIC at 10,000 feet](https://docs.google.com/document/d/1gY9-YNDNAB1eip-RTPbqphgySwSNSDHLq9D5Bty4FSU/edit)
-   [netstat overview](http://tldp.org/LDP/nag2/x-087-2-iface.netstat.html)
-   [Cheat Sheet for IP command](https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf)

### Application-Layer Protocols

#### HTTP

-   [Keep Alive Client](https://en.wikipedia.org/wiki/HTTP_persistent_connection)
-   <https://www.w3.org/History/19921103-hypertext/hypertext/WWW/Protocols/HTTP.html>
-   <https://www.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html>
-   <https://daniel.haxx.se/docs/ftp-vs-http.html>
-   [What inspired my interest in this topic](https://news.ycombinator.com/item?id=13075355)

### TCPDump Tutorials

-   <http://www.alexonlinux.com/tcpdump-for-dummies>
-   <http://bencane.com/2014/10/13/quick-and-practical-reference-for-tcpdump/>
-   <https://www.quora.com/What-is-the-difference-between-TCPs-FIN-and-RST-packets>

Security
--------

-   [Strong Ciphers for Web Servers](https://cipherli.st/)
-   [SSL Labs](https://www.ssllabs.com/) (assesses your site's security)
-   [Is TLS fast yet?](https://istlsfastyet.com/)
-   [TLS Overview](https://hpbn.co/transport-layer-security-tls/) (chapter of an O'Reilly book)
-   [CAA](https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization) (combines SSL/TLS certificate file w/ a DNS record to increase security)
-   [GPG Quickstart](https://www.madboa.com/geek/gpg-quickstart)
-   [Creating GPG Keys Using the CLI](https://fedoraproject.org/wiki/Creating_GPG_Keys#Creating_GPG_Keys_Using_the_Command_Line)
-   [Backup Encryption](http://www.crypt.gen.nz/papers/backup_encryption.html)
-   [Inventing the Sudo Command](http://hackaday.com/2014/05/28/interview-inventing-the-unix-sudo-command/)
-   [XKCD Password Generator](http://preshing.com/20110811/xkcd-password-generator/)
-   [Another XKCD Password Generator](http://correcthorsebatterystaple.net/)
-   [Dangerous Sudoers Entries](https://blog.compass-security.com/2012/10/dangerous-sudoers-entries-part-4-wildcards/)
-   [Stop Disabling SELinux](https://stopdisablingselinux.com/)
-   [Explain Like I'm 5: Kerberos](https://www.roguelynn.com/words/explain-like-im-5-kerberos/)

Storage
-------

-   [Why NFS Sucks](https://www.kernel.org/doc/ols/2006/ols2006v2-pages-59-72.pdf)
-   [How to improve ZFS performance](https://icesquare.com/wordpress/how-to-improve-zfs-performance/)
-   [ZFS RAID Speed Capacity](https://calomel.org/zfs_raid_speed_capacity.html)
-   [How I learned to stop worrying and love RAIDZ](https://www.delphix.com/blog/delphix-engineering/zfs-raidz-stripe-width-or-how-i-learned-stop-worrying-and-love-raidz)
-   [Lustre and Panasas Are Not So Different](http://clusterdesign.org/2012/08/lustre-and-panasas-are-not-so-different/)
-   [Backblaze Hard Drive Reliability Stats, Q1 2016](https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/)
-   [NDMP](https://www.snia.org/ndmp) (Description and whitepaper)
-   <http://www.tldp.org/LDP/intro-linux/html/sect_03_01.html>
-   [Does Writing to NFS Put Processes into Uninterruptible Sleep?](https://medium.com/@jonphilpott/does-writing-to-nfs-put-processes-into-un-interruptible-sleep-d58790cd13b6#.h4oi0ufqx)
-   [Create LUKS](http://redhat-admin.blogspot.com/2011/09/create-and-configure-luks-encrypted.html)
-   [Access xfs quota info from NFS client](https://serverfault.com/questions/560844/access-xfs-quota-info-from-nfs-client)
-   [rpc.rquotad](https://linux.die.net/man/8/rpc.rquotad)
-   [Using Linux quota command pointing to an /ifs nfs mounted filesystem.](https://www.dell.com/community/Isilon/Using-Linux-quota-command-pointing-to-an-ifs-nfs-mounted/td-p/6916630)

### ACLs

-   [En Francais](http://okki666.free.fr/docmaster/articles/linux100.htm)
-   <https://wiki.archlinux.org/index.php/Access_Control_Lists>
-   <https://www.freebsd.org/doc/handbook/fs-acl.html>

### RAID-5

A list of pages discussing why not to use RAID5:

-   <https://news.ycombinator.com/item?id=8306499>
-   <https://www.reddit.com/r/sysadmin/comments/ydi6i/dell_raid_5_is_no_longer_recommended_for_any/>
-   <https://www.reddit.com/r/sysadmin/comments/3yoc9z/raid_5raid_10_tradeoff/> (in which we learn that RAID5 works for SSDs)

An article on the RAID "write-hole", which seems to be especially salient for RAID5:

-   <http://www.raid-recovery-guide.com/raid5-write-hole.aspx>

### Tape

-   tar tvf **\<device\_name\>** - Read the file name from the tar header for the current file that the tape is pointed at.

### Database vs Filesystem

-   <https://stackoverflow.com/questions/38120895/database-vs-file-system-storage>
-   <https://softwareengineering.stackexchange.com/questions/190482/why-use-a-database-instead-of-just-saving-your-data-to-disk>
-   <https://dzone.com/articles/which-is-better-saving-files-in-database-or-in-fil>

### AI / Neural Network / Deep Learning Workloads

- [Why NFS Performance Won’t Cut it For AI and Machine Learning](https://www.weka.io/blog/nfs-performance-wont-cut-ai-machine-learning/)
- [Why Network File System (NFS) is not Suitable for AI Workloads?](https://www.weka.io/blog/network-file-system-nfs-and-ai-workloads/)
- [NFS vs Lustre](https://wiki.lustre.org/NFS_vs._Lustre)
- [Caching with CacheFS](https://www.admin-magazine.com/HPC/Articles/Caching-with-CacheFS)
- [TFRecord Format Details](https://www.tensorflow.org/tutorials/load_data/tfrecord#tfrecords_format_details)
- [Efficient PyTorch I/O library for Large Datasets, Many Files, Many GPUs](https://pytorch.org/blog/efficient-pytorch-io-library-for-large-datasets-many-files-many-gpus/) (in which NVIDIA uses tars to work around issues with file metadata performance penalty)
- [vmtouch](https://hoytech.com/vmtouch/) (Simple package to pre-warm RAM with file pages)

Identity Management / User Management
-------------------------------------

-   <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/s1-users-tools.html>
-   [Introduction to LDAP](http://ldapman.org/articles/intro_to_ldap.html)

Applications
------------

### Web Servers

-   An analogy: web/app servers / load balancers belong to the same sub-class of problems that HPC schedulers treat, but are just more narrow in scope.
-   A 301 redirect in nginx for HTTPS requires a cert because the packet needs to be decrypted for nginx to inspect the host field of the packet header.
-   [Canned nginx Configs (to use as templates)](https://www.nginx.com/resources/wiki/start/)

### Databases

-   <http://philip.greenspun.com/sql/>
-   [What an in-memory database is and how it persists data efficiently](https://medium.com/@denisanikin/what-an-in-memory-database-is-and-how-it-persists-data-efficiently-f43868cff4c1)
-   [What are pros and cons of PostgreSQL and MySQL? With respect to reliability, speed, scalability, and features.](https://www.quora.com/What-are-pros-and-cons-of-PostgreSQL-and-MySQL-With-respect-to-reliability-speed-scalability-and-features)

Virtualization
--------------

-   Apparently KVM and Virtualbox are incompatible / can't be run simultaneously. See [here](http://www.dedoimedo.com/computers/kvm-virtualbox.html) for an idea on how to handle that (or just don't do that at all because it doesn't make too much sense to begin with- quoth the older and wiser me).
-   [Xen Networking](https://wiki.xenproject.org/wiki/Xen_Networking)
-   [Importing an OVA into KVM](https://wiki.hackzine.org/sysadmin/kvm-import-ova.html)

Containerization
----------------

-   [Kubernetes: An Overview](https://thenewstack.io/kubernetes-an-overview/)
-   [Docker for Data Science](https://www.amazon.com/Docker-Data-Science-Extensible-Infrastructure/dp/1484230116)
-   [Docker Security Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Docker_Security_Cheat_Sheet.md)

Cloud Computing
---------------

-   If an AWS S3 upload is [MultiPart](MultiPart), the ETag attribute of an S3 bucket object is *not* an MD5 hash. It is the hashes for each part uploaded concatenated, plus a dash and the number of parts uploaded (see [here](http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html)).

### S3-compatible object stores

-   <https://minio.io/>
-   <https://cloudian.com/>
-   <https://wasabi.com/>
-   <http://pithos.io/>
-   <https://www.zenko.io/>
-   <https://leo-project.net/leofs/>
-   <https://github.com/eucalyptus/eucalyptus/wiki/Walrus-S3-API>
-   <http://docs.ceph.com/docs/master/radosgw/s3/>

Windows/Linux Compatibility
-----

-   [Debian9ADSharedDisks_Sssd_PamMount](https://wiki.debian.org/wiki/Debian9ADSharedDisks_Sssd_PamMount)
-   [Pam_mount](https://wiki.archlinux.org/index.php/Pam_mount)
-   [RHEL Guide for multi-user SMB mount](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/storage_administration_guide/index#performing_a_multi-user_smb_mount)
-   [RHEL Windows Integration Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/windows_integration_guide/index)

Tools
-----

-   [Atop](http://www.atoptool.nl/)
-   [Gas Hosts](https://github.com/2ndalpha/gasmask)
-   [last](https://linux.die.net/man/1/last) (can show reboot times)
-   [lastlog](https://linux.die.net/man/8/lastlog) (can show last login for a user- with decently informative timestamp)
-   <https://mxtoolbox.com/SuperTool.aspx>
-   <https://peteris.rocks/blog/htop/>
-   <http://md5deep.sourceforge.net/>
-   [GNU Parallel](http://www.shakthimaan.com/posts/2014/11/27/gnu-parallel/news.html)

