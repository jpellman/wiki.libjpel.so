

Creating hard and soft links
============================

Hard Links
----------

-   ln /path/to/source /path/to/target
-   You cannot create a hard link pointing to a directory.
-   Only the owner of a file can make a hard link pointing to it in RHEL 7 (this contrasts with RHEL 6).
-   Hard links directly point to the inode for a file on disk.

Soft/Symbolic Links
-------------------

-   ln -s /path/to/source /path/to/target
-   Soft links can be to a directory.
-   Soft links create a new file that points to the source file. This new file (the target) has its own inode. Deleting a soft link will not delete the original file.
-   You can convert symlinks that use absolute paths to symlinks using relative paths with the *symlinks -c* command. This can help when migrating symlinks across filesystems.

Checking Links
--------------

-   ls -i /path/to/link : Prints the inode number of the file/directory.

References / Further Reading
============================

-   [CertDepot](http://www.certdepot.net/sys-create-hard-and-soft-links/)
-   [An explanation of hard vs soft links](http://www.geekride.com/hard-link-vs-soft-link/)
-   [Another explanation of hard vs soft links](http://linuxgazette.net/105/pitcher.html)

Man Pages
---------

-   <http://linux.die.net/man/1/ln>
-   <http://linux.die.net/man/8/symlinks>
-   [Grymoire on inodes](http://www.grymoire.com/Unix/Inodes.html)

* * * * *

[StorageAndFileSystems](../StorageAndFileSystems) [SystemsAdministration](../SystemsAdministration)
