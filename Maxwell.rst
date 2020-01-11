#format rst

Maxwell
=======

.. contents::

Description
-----------

Maxwell is essentially a gaming workstation that I use to try out new things locally within my apartment.  It is dual-boot, with Windows 10 on a 60 GB SSD and CentOS 7 on a 240 GB SSD.  I first built it around February/March 2017, with a goal of creating a workstation that I could use for both experimentation and running BOINC_- to be completely honest, part of my motivation was to see how close I could get to surpassing (or at least equalling) some of the older scientific lab hardware I had dealt with in the past using only consumer-grade parts.

Specifications
--------------

[Table not converted]

Part List
~~~~~~~~~

* `Zalman MS800 ATX Mid Tower Gaming Case (Black)`_

* `Rosewill 3 x 5.25-Inch to 4 x 3.5-Inch Hot-swap SATAIII/SAS Hard Disk Drive Cage - Black`_

* `Corsair Force Series GT 2.5" 60GB SATA III Internal Solid State Drive`_

* `SanDisk SSD PLUS 240GB Internal SSD - SATA III 6 Gb/s`_

* x2 `WD Blue 1TB SATA 6 Gb/s 7200 RPM 64MB Cache 3.5 Inch Desktop Hard Drive (WD10EZEX)`_

* `Intel Boxed Core I7-6700 FC-LGA14C 3.40 GHz 8 M Processor Cache 4 LGA 1151 BX80662I76700`_

* x4 `Crucial 16GB Single DDR4 2133 MT/s (PC4-17000) DR x8 Unbuffered DIMM 288-Pin Memory - CT16G4DFD8213`_

* `MSI Pro Solution Intel Z170A LGA 1151 DDR4 USB 3.1 ATX Motherboard (Z170A SLI)`_

* `Corsair CX Series 750 Watt 80 Plus Bronze Certified Non-Modular Power Supply (CP-9020015-NA)`_

* `EVGA Geforce GTX 1050 SC ITX, 2GB`_

* `PNY NVIDIA GeForce GTX 1050 2GB Graphics Card`_

Applications
------------

* KVM / virt-manager / virt-install

* BOINC (custom compile w/o the BOINC manager app; just boinc-client)

* Folding@Home

* t_ (Twitter CLI)

* gmvault_

* CentOS 7's "Server w/ GUI" Install Group (GNOME 3, etc)

* x2go

* mate (since x2go breaks with Gnome 3)

* NVIDIA Drivers (for CUDA)

* ZFS on Linux

* AWS CLI

* rclone (for Google Drive backups)

* MoinMoin_

* Prey_ (of somewhat dubious utility)

Of these, the following can go away because I don't need a GUI for this host / don't want the rest:

* CentOS 7's "Server w/ GUI" Install Group (GNOME 3, etc)

* x2go

* mate (since x2go breaks with Gnome 3)

* MoinMoin_

* Prey_ (of somewhat dubious utility)

KVM is going to be managed via Proxmox in the future, as will ZFS on Linux (VMs will have volumes exposed to them via NFS).  That means that only the following need to be managed via Ansible:

* BOINC (custom compile w/o the BOINC manager app; just boinc-client)

* Folding@Home

* t_ (Twitter CLI)

* gmvault_

* rclone (for Google Drive backups)

* AWS CLI

Plans
-----

* The KVM VMs were connected to a virtual bridge (virbr1) through which they could be accessible on the LAN.  Installing Docker has somehow broken this in some way (or something else, but Docker is the obvious culprit).

  * This could be because `Docker fucks with the firewall`_ or because of a conflict between how I set up networking on Maxwell and what Docker expects (also discussed here_.  It seems like a huge pain to mix Docker and KVM, so I'm probably going to take the advice listed on reddit and put Docker on a VM or just not do virtualization on maxwell and make it purely for Linux hosts (seems like a meh idea).

* None of this is managed in any systematic way, except for a shell script I made when I first provisioned this host way back when.  I'd like to re-create the boot volume with Kickstart and Ansible so that my homelab follows the Infrastructure as Code paradigm a little more closely.  There's also a ton of other crap on there that doesn't get mentioned above that I have since stopped playing with (e.g., Kimchi_, which never seemed useful enough vs virsh tbh).

* I want to use Docker where I would in the past use KVM for Linux-based VMs, and only use KVM for non-Linux operating systems (such as FreeBSD, Windows, etc)

* I at one point considered doing GPU passthrough to KVM, but it seemed involved (can't find any of the links to tutorials I was looking at right now), and would have made it so that the host would no longer have been able to use the GPU.  With Docker GPU passthrough seems to be much less complicated, so I'd like to encapsulate BOINC and Folding@Home and put them in containers that access the GPU via passthrough rather than having them live on bare metal.

  * https://github.com/dholt/kvm-gpu

  * https://gist.github.com/cuibonobo/d354440fecdd37c35ecd

  * On 7/31/19, I finally tried to get GPU passthrough to work, but couldn't because Red Hat and NVIDIA are `silly corporate capitalist cows`_.  See `here <https://github.com/kubernetes/minikube/issues/3546>`__ too.

  * After my issues with getting GPU passthrough to work with CentOS, I decided to install Proxmox instead.

* I don't really use Windows that much since it would require rebooting to use (and I don't really game enough).  It would be interesting if I could find a way to run it via KVM.  There's only one app that really needs GPUs (Obduction) and I wouldn't mind booting directly for that.  Other tech I'd want to mess with (Chocolatey, PowerShell_, etc) doesn't require an intense GPU (heck, even the point-and-click adventures I play would be fine without the 1050s).

* I have a bunch of utilities set up to back up my online presence (gmvault, t, etc).  I'd like to find a way to give these utilities their own space (i.e., a container) and manage them via Ansible.

* My ZFS backup scripts need to be put under version control.

* The bash script I use to back up my Tweets could be improved (presently there are a lot of files produced with redundant information; it uses the shell script from `here <http://blog.jphpsf.com/2012/05/07/backing-up-your-twitter-account-with-t/>`__.

To-Do Items to Make Maxwell A Fully-Managed Host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Make an Ansible role for the ZFS backup scripts (these will need to run under Proxmox).  Investigate if Proxmox has something better.

* Make an Ansible role for the Twitter backups.

* Make an Ansible role for the rclone backups.

* Make an Ansible role for the gmvault backups.

* Make Ansible roles for boinc and folding@home.

* :strike:`Back up home video DV footage currently on the root volume SSD to another disk.` *DONE: 2/24/19, 23:25*

* Invoke your ZFS backup script to send a snapshot to AWS.  Invoke the ZFS backup script to save a snapshot to your nearline storage.

* Create a CentOS 6 VM for BOINC and FAH.  We want to use CentOS 6 because the FAH packages still need Python 2.6 (unless you modify them manually to use Python 2.7 in CentOS 7, which is a bit of a pain).  Attach thumb drive to this VM and have it be the backing storage for at least the scratch storage used by BOINC.  Give this VM access to GPUs and 8 vCPUs.

* Create a CentOS 7 VM for general file access / ZFS.  Give it 2 vCPUs.  This VM may also contain the Twitter CLI (possibly within an RVM environment), gmvault and all of the other internet presence  / personal data backup cronjobs (I may make one of these for my reddit data using PRAW_).

* I may then experiment with a Docker VM and getting my Windows 10 installation to run as a VM.  If I can get GPU passthrough working with a Docker VM, I may retire the CentOS 6 VM and replace it with a Docker container (or split FAH and BOINC into multiple containers).

* I'm then going to replace the MoinMoin_ instance I've been running with Monica_.

Photos
------

`attachment:IMG_20190121_154736836.jpg`_`attachment:IMG_20190121_154736836.jpg`_`attachment:None`_ `attachment:IMG_20190121_154801532.jpg`_`attachment:IMG_20190121_154801532.jpg`_`attachment:None`_ `attachment:IMG_20190121_154834420.jpg`_`attachment:IMG_20190121_154834420.jpg`_`attachment:None`_

-------------------------

 Hosts_

.. ############################################################################

.. _BOINC: https://boincstats.com/en/stats/-1/user/detail/3500755

.. _Zalman MS800 ATX Mid Tower Gaming Case (Black): https://smile.amazon.com/gp/product/B00I0V4IMW/ref=ppx_yo_dt_b_asin_title_o03__o00_s01?ie=UTF8&psc=1

.. _Rosewill 3 x 5.25-Inch to 4 x 3.5-Inch Hot-swap SATAIII/SAS Hard Disk Drive Cage - Black: https://smile.amazon.com/gp/product/B00DGZ42SM/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1

.. _Corsair Force Series GT 2.5" 60GB SATA III Internal Solid State Drive: https://www.newegg.com/Product/Product.aspx?Item=N82E16820233193

.. _SanDisk SSD PLUS 240GB Internal SSD - SATA III 6 Gb/s: https://smile.amazon.com/gp/product/B01F9G43WU/ref=ppx_yo_dt_b_asin_title_o00__o00_s00?ie=UTF8&psc=1

.. _WD Blue 1TB SATA 6 Gb/s 7200 RPM 64MB Cache 3.5 Inch Desktop Hard Drive (WD10EZEX): https://smile.amazon.com/gp/product/B0088PUEPK/ref=ppx_yo_dt_b_asin_title_o00__o00_s00?ie=UTF8&psc=1

.. _Intel Boxed Core I7-6700 FC-LGA14C 3.40 GHz 8 M Processor Cache 4 LGA 1151 BX80662I76700: https://smile.amazon.com/gp/product/B0136JONG8/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1

.. _Crucial 16GB Single DDR4 2133 MT/s (PC4-17000) DR x8 Unbuffered DIMM 288-Pin Memory - CT16G4DFD8213: https://smile.amazon.com/gp/product/B015YPAZPU/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1

.. _MSI Pro Solution Intel Z170A LGA 1151 DDR4 USB 3.1 ATX Motherboard (Z170A SLI): https://smile.amazon.com/gp/product/B01DDR05P6/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1

.. _Corsair CX Series 750 Watt 80 Plus Bronze Certified Non-Modular Power Supply (CP-9020015-NA): https://smile.amazon.com/gp/product/B008RJZQSW/ref=ppx_yo_dt_b_asin_title_o09__o00_s00?ie=UTF8&psc=1

.. _EVGA Geforce GTX 1050 SC ITX, 2GB: https://smile.amazon.com/EVGA-GeForce-Support-Graphics-02G-P4-6152-KR/dp/B01M64G435?sa-no-redirect=1

.. _PNY NVIDIA GeForce GTX 1050 2GB Graphics Card: https://smile.amazon.com/PNY-NVIDIA-GeForce-Graphics-VCGGTX10502PB/dp/B01M27X9WI/ref=sr_1_fkmrnull_7?keywords=PNY+-+NVIDIA+GeForce+GTX+1050+2GB+GDDR5&qid=1548101376&s=Electronics&sr=1-7-fkmrnull

.. _t: https://github.com/sferik/t

.. _gmvault: http://gmvault.org

.. _MoinMoin: ../MoinMoin

.. _Prey: https://preyproject.com/

.. _Docker fucks with the firewall: https://www.reddit.com/r/linuxadmin/comments/7tlkve/libvirt_network_configuration_conflicts_with/

.. _here: https://fralef.me/docker-and-iptables.html

.. _Kimchi: https://github.com/kimchi-project/kimchi

.. _silly corporate capitalist cows: https://bugzilla.redhat.com/show_bug.cgi?id=1492173

.. _PowerShell: ../PowerShell

.. _PRAW: https://praw.readthedocs.io

.. _Monica: https://www.monicahq.com/

.. _Hosts: ../Hosts

