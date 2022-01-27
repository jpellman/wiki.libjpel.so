storage01
=========

Description
-----------

storage01 is a simple NAS device.  It serves files from */srv/nfs* and uses [lvmcache](https://wiki.archlinux.org/title/LVM#Cache) to speed up load times for commonly accessed files.  lvmcache is built upon dm-cache, and it's important to note that the benefits of caching are only reaped for files that are accessed multiple times (see [here](https://www.redhat.com/en/blog/improving-read-performance-dm-cache)).

Specifications
--------------

| Key | Value |
| --- | --- |
| **CPU** | Intel(R) Celeron(R) J4005 CPU |
| **# of Cores (logical)** | 2 |
| **CPU Clock Speed (GHz)** | 2.00 |
| **Memory (GB)** | 4 |
| **Disks** | 60 GB SSD (LVM cache), 2 TB HDD |
| **OS** | CentOS 7 |
| **IP Address** | 192.168.1.4 |
| **Ansible Playbook** | [storage.yml](https://github.com/jpellman/home-ansible/blob/master/playbooks/storage.yml) |
| **Kickstart Config** | [centos7-storage01-full.cfg](https://github.com/jpellman/home-packer/blob/main/seeds/centos7-storage01-full.cfg) |

### Part List

 * [Cooler Master Elite 110 RC-110-KKN2 Midnight Black Steel / Plastic Mini-ITX Tower Computer Case](https://www.amazon.com/gp/product/B00ID2FBU6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
 * [CORSAIR VS Series, VS450, 450 Watt, 80+ White Certified, Non-Modular Power Supply](https://www.amazon.com/gp/product/B07XF8NP2V/)
 * [ASRock J4005B-ITX](https://www.amazon.com/gp/product/B079GFD84R)
 * [Western Digital 2TB WD Blue PC Hard Drive HDD](https://www.amazon.com/dp/B07JC1TQ7N)
 * [Corsair Force GT 60 GB](https://www.amazon.com/Corsair-Force-2-5-Inch-Solid-State/dp/B005IZ4IRS)

Applications
------------

 * NFS Server

Plans
-----

 * I want to convert storage01 into a dedicated backup device (rather than a crappy NAS with no RAID) that regularly syncs down all of my Google Drive, emails, and other bits of data that exist non-locally.  
 * I also want to install [rsnapshot](https://rsnapshot.org/) on my laptop to regularly sync my personal photo/home video collection (consisting of digitized VHS tapes, DAT tapes, etc) to this backup device.  Why don't I just back these up to the cloud?  Well, a) they take up a huge amount of space (the digitized DAT tapes I have are all encoded as FLAC files) and b) I'm reluctant to entrust my home / personal videos to a third-party provider.
 * I think it would make sense to install rsnapshot on the backup device as well and have it regularly take "snapshots" of my Google Drive / emails.
