

Notes on Backing Up My Hard Disk to Blu-Ray
===========================================

Commands to Follow
------------------

To distribute files into more or less evenly sized buckets (as you would when having a backup span multiple disks:

    dirsplit -e4 -s 25025314816b $PATH_TO_DIR_TO_BACK_UP

`dirsplit` generates multiple lists of which files will live on which disk. You can preview how much each disk space will ultimately be consumed with:

    cut -d= -f2  $PATH_TO_DIRSPLIT_LIST | tr '\n' '\0'  | du -sch --files0-from=-

And you can use the following to generate the actual image files. Note that this will produce a hybrid UDF/ISO-9660 image file, files that are larger than 4 GB will appear to be truncated when read by drives that do not support UDF (see [here](https://superuser.com/questions/597929/what-is-the-largest-file-i-can-write-to-a-dvd) and [here](https://unix.stackexchange.com/questions/17594/how-to-create-udf-images-and-burn-them-to-dvd-or-cdrom).

    mkisofs -udf -V $VOLNAME -D -r --joliet-long -graft-points -allow-limited-size -path-list $PATH_TO_DIRSPLIT_LIST -o $ISONAME

Once an image is generated, copy it down to [Bruno](../Bruno) (or equivalent desktop/laptop). Use `scp` to get a progress bar, and to eliminate some of the `rsync` overhead (not as necessary when there's only one file and file metadata doesn't matter).

    scp jpellman@maxwell.so:$ISOPATH  .

Timing
------

Here are some approximate benchmarks for how long the above steps take:

[Table not converted]

Speeds based off [this LG Blu-Ray Writer](https://smile.amazon.com/LG-Electronics-External-Optical-WP50NB40).

* * * * *

> [HomeLab](../HomeLab)
