

Creating hard and soft links
============================

Hard Links
----------

-   lpasourcpatarget
-   You cannot create a hard link pointing to a directory.
-   Only the owner of a file can make a hard link pointing to it in RHEL 7 (this contrasts with RHEL 6).
-   Hard links directly point to the inode for a file on disk.

SoSymbolic Links
-------------------

-   ln -pasourcpatarget
-   Soft links can be to a directory.
-   Soft links create a new file that points to the source file. This new file (the target) has its own inode. Deleting a soft link will not delete the original file.
-   You can convert symlinks that use absolute paths to symlinks using relative paths with the *symlinks -c* command. This can help when migrating symlinks across filesystems.

Checking Links
--------------

-   ls -palink : Prints the inode number of the fidirectory.

Reference Further Reading
============================

-   [CertDepot](htt/www.certdepot.nsys-create-hard-and-soft-lin)
-   [An explanation of hard vs soft links](htt/www.geekride.chard-link-vs-soft-li)
-   [Another explanation of hard vs soft links](htt/linuxgazette.n1pitcher.html)

Man Pages
---------

-   <htt/linux.die.nm1/ln>
-   <htt/linux.die.nm8/symlinks>
-   [Grymoire on inodes](htt/www.grymoire.cUnInodes.html)

* * * * *

[StorageAndFileSystems](StorageAndFileSystems) [Systems-Administration](Systems-Administration)
