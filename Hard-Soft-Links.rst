#format rst

Create hard and soft links
==========================

.. contents:: :depth: 2

Hard Links
----------

* ln /path/to/source /path/to/target

* You cannot create a hard link pointing to a directory.

* Only the owner of a file can make a hard link pointing to it in RHEL 7 (this contrasts with RHEL 6).

Soft Links
----------

* ln -s /path/to/source /path/to/target

* Soft links can be to a directory.

Checking Links
--------------

* ls -i /path/to/link : Prints the inode number of the file/directory.

References / Further Reading
============================

* CertDepot_

Man Pages
---------

* http://linux.die.net/man/1/ln

.. ############################################################################

.. _CertDepot: http://www.certdepot.net/sys-create-hard-and-soft-links/

