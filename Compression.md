\#format rst

Archive, compress, unpack, and uncompress files using tar, star, gzip, and bzip2
================================================================================

Compressing a file or directory
-------------------------------

-   gzip *target*
-   bzip *target*
-   tar cvzf *destination.tar.gz* *target*
-   tar cvjf *destination.tar.bz2* *target*
-   star -xattr -H=exustar -c -f=\*destination.star\* *target*.
-   For directories, you must use tar or star.
-   For directories, you may include the *--selinux* flag to preserve [SELinux file contexts](../RHCSA_SELinuxFileandProcessContext).
-   For directories, you may want to use a relative path rather than an absolute path. An absolute path will create intermediate directories in the tree.
-   Make sure that the *f* option for tar is at the end.

Decompressing a file or directory
---------------------------------

-   gunzip *target.gz*
-   bunzip *target.bz2*
-   tar xvzf *target.tar.gz*
-   tar xvjf *target.tar.bz2*
-   star -x -f=\*target.star\*
-   If you used the *--selinux* flag to archive and compress a directory, you should include it again when untarring and decompressing.

Reading archive contents
------------------------

-   tar tzvf target.tar.gz
-   tar tjvf target.bz2
-   Also see: [TapeBackup](../TapeBackup).

References / Further Reading
============================

-   [CertDepot](http://www.certdepot.net/sys-archive-compress-unpack-and-uncompress-files/)

Man Pages
---------

-   <http://linux.die.net/man/1/gzip>
-   <http://linux.die.net/man/1/bzip2>
-   <http://linux.die.net/man/1/tar>
-   <http://linux.die.net/man/1/star>

