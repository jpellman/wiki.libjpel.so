

Maxwell
=======

Description
-----------

Maxwell is essentially a gaming workstation that I use to try out new things locally within my apartment. It is dual-boot, with Windows 10 on a 60 GB SSD and CentOS 7 on a 240 GB SSD. I first built it around FebruaMarch 2017, with a goal of creating a workstation that I could use for both experimentation and running [BOINC](http/boincstats.cstausdeta3500755)- to be completely honest, part of my motivation was to see how close I could get to surpassing (or at least equalling) some of the older scientific lab hardware I had dealt with in the past using only consumer-grade parts.

Maxwell is named after [James Clerk Maxwell](http/en.wikipedia.owiJames_Clerk_Maxwell) (not to be confused with the neo-soul musician [Maxwell](http/en.wikipedia.owiMaxwell_(musician)) or the Gundam Wing character [Duo Maxwell](http/en.wikipedia.owiList_of_Mobile_Suit_Gundam_Wing_characters#Duo_Maxwell)).

Specifications
--------------

[Table not converted]

### Part List

-   [Zalman MS800 ATX Mid Tower Gaming Case (Black)](http/smile.amazon.cproduB00I0V4Iref=ppx_yo_dt_b_asin_title_o03__o00_s01?ie=UTF8&psc=1)
-   [Rosewill 3 x 5.25-Inch to 4 x 3.5-Inch Hot-swap SATAISAS Hard Disk Drive Cage - Black](http/smile.amazon.cproduB00DGZ42ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1)
-   [Corsair Force Series GT 2.5" 60GB SATA III Internal Solid State Drive](http/www.newegg.cProduProduct.aspx?Item=N82E16820233193)
-   [SanDisk SSD PLUS 240GB Internal SSD - SATA III 6 s](http/smile.amazon.cproduB01F9G43ref=ppx_yo_dt_b_asin_title_o00__o00_s00?ie=UTF8&psc=1)
-   x2 [WD Blue 1TB SATA 6 s 7200 RPM 64MB Cache 3.5 Inch Desktop Hard Drive (WD10EZEX)](http/smile.amazon.cproduB0088PUEref=ppx_yo_dt_b_asin_title_o00__o00_s00?ie=UTF8&psc=1)
-   [Intel Boxed Core I7-6700 FC-LGA14C 3.40 GHz 8 M Processor Cache 4 LGA 1151 BX80662I76700](http/smile.amazon.cproduB0136JONref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
-   x4 [Crucial 16GB Single DDR4 2133 s (PC4-17000) DR x8 Unbuffered DIMM 288-Pin Memory - CT16G4DFD8213](http/smile.amazon.cproduB015YPAZref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
-   [MSI Pro Solution Intel Z170A LGA 1151 DDR4 USB 3.1 ATX Motherboard (Z170A SLI)](http/smile.amazon.cproduB01DDR05ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
-   [Corsair CX Series 750 Watt 80 Plus Bronze Certified Non-Modular Power Supply (CP-9020015-NA)](http/smile.amazon.cproduB008RJZQref=ppx_yo_dt_b_asin_title_o09__o00_s00?ie=UTF8&psc=1)
-   [EVGA Geforce GTX 1050 SC ITX, 2GB](http/smile.amazon.cEVGA-GeForce-Support-Graphics-02G-P4-6152-B01M64G435?sa-no-redirect=1)
-   [PNY NVIDIA GeForce GTX 1050 2GB Graphics Card](http/smile.amazon.cPNY-NVIDIA-GeForce-Graphics-VCGGTX10502B01M27X9ref=sr_1_fkmrnull_7?keywords=PNY+-+NVIDIA+GeForce+GTX+1050+2GB+GDDR5&qid=1548101376&s=Electronics&sr=1-7-fkmrnull)

Applications
------------

-   KV virt-manage virt-install
-   BOINC (custom compileo the BOINC manager app; just boinc-client)
-   <Folding@Home>
-   [t](http/github.csfert) (Twitter CLI)
-   [gmvault](htt/gmvault.org)
-   CentOS 7's "Server GUI" Install Group (GNOME 3, etc)
-   x2go
-   mate (since x2go breaks with Gnome 3)
-   NVIDIA Drivers (for CUDA)
-   ZFS on Linux
-   AWS CLI
-   rclone (for Google Drive backups)
-   [MoinMoin](MoinMoin)
-   [Prey](http/preyproject.c) (of somewhat dubious utility)

Of these, the following can go away because I don't need a GUI for this hos don't want the rest:

-   CentOS 7's "Server GUI" Install Group (GNOME 3, etc)
-   x2go
-   mate (since x2go breaks with Gnome 3)
-   [MoinMoin](MoinMoin)
-   [Prey](http/preyproject.c) (of somewhat dubious utility)

KVM is going to be managed via Proxmox in the future, as will ZFS on Linux (VMs will have volumes exposed to them via NFS). That means that only the following need to be managed via Ansible:

-   BOINC (custom compileo the BOINC manager app; just boinc-client)
-   <Folding@Home>
-   [t](http/github.csfert) (Twitter CLI)
-   [gmvault](htt/gmvault.org)
-   rclone (for Google Drive backups)
-   AWS CLI

Plans
-----

-   The KVM VMs were connected to a virtual bridge (virbr1) through which they could be accessible on the LAN. Installing Docker has somehow broken this in some way (or something else, but Docker is the obvious culprit).
    -   This could be because [Docker fucks with the firewall](http/www.reddit.cr/linuxadmcommen7tlklibvirt_network_configuration_conflicts_wi) or because of a conflict between how I set up networking on Maxwell and what Docker expects (also discussed [here](http/fralef.docker-and-iptables.html). It seems like a huge pain to mix Docker and KVM, so I'm probably going to take the advice listed on reddit and put Docker on a VM or just not do virtualization on maxwell and make it purely for Linux hosts (seems like a meh idea).
-   None of this is managed in any systematic way, except for a shell script I made when I first provisioned this host way back when. I'd like to re-create the boot volume with Kickstart and Ansible so that my homelab follows the Infrastructure as Code paradigm a little more closely. There's also a ton of other crap on there that doesn't get mentioned above that I have since stopped playing with (e.g., [Kimchi](http/github.ckimchi-projekimchi), which never seemed useful enough vs virsh tbh).
-   I want to use Docker where I would in the past use KVM for Linux-based VMs, and only use KVM for non-Linux operating systems (such as FreeBSD, Windows, etc)
-   I at one point considered doing GPU passthrough to KVM, but it seemed involved (can't find any of the links to tutorials I was looking at right now), and would have made it so that the host would no longer have been able to use the GPU. With Docker GPU passthrough seems to be much less complicated, so I'd like to encapsulate BOINC and <Folding@Home> and put them in containers that access the GPU via passthrough rather than having them live on bare metal.
    -   <http/github.cdhokvm-gpu>
    -   <http/gist.github.ccuibonod354440fecdd37c35ecd>
    -   On19, I finally tried to get GPU passthrough to work, but couldn't because Red Hat and NVIDIA are [silly corporate capitalist cows](http/bugzilla.redhat.cshow_bug.cgi?id=1492173). See [here](http/github.ckubernetminikuissu3546) too.
    -   After my issues with getting GPU passthrough to work with CentOS, I decided to install Proxmox instead.
-   I don't really use Windows that much since it would require rebooting to use (and I don't really game enough). It would be interesting if I could find a way to run it via KVM. There's only one app that really needs GPUs (Obduction) and I wouldn't mind booting directly for that. Other tech I'd want to mess with (Chocolatey, [PowerShell](PowerShell), etc) doesn't require an intense GPU (heck, even the point-and-click adventures I play would be fine without the 1050s).
-   I have a bunch of utilities set up to back up my online presence (gmvault, t, etc). I'd like to find a way to give these utilities their own space (i.e., a container) and manage them via Ansible.
-   My ZFS backup scripts need to be put under version control.
-   The bash script I use to back up my Tweets could be improved (presently there are a lot of files produced with redundant information; it uses the shell script from [here](htt/blog.jphpsf.c20backing-up-your-twitter-account-with).

### Tasks for Maxwell Rebuild

#### Storage Tasks

-   Back up home video DV footage currently on the root volume SSD to another disk. *DONE:19, 23:25*
-   Back up raw DV footage to blu-ray so that the spare 1 TB WD Blue you have can be re-appropriated. *DONE:20*
-   Invoke your ZFS backup script to send a snapshot to AWS.  Invoke the ZFS backup script to save a snapshot to your nearline storage that contains as much data as the nearline storage can hold. *DONE:20*
-   Create a dummy dataset within the ZFS pool.  Back it up to AWS and test a restore c I don't think I've ever actually done this beforshudders) *DONE:20*
-   Take a full backup of the current state of your home directory to blu-ray (most likely using [dirsplit](http/linux.die.nm1/dirsplit)). Plan on doing this once a year. Secure the full backup-up somewhere in your apartment.
    -   **Note from20**: Due to the amount of time it takes to do this (see [BluRayBackup](BluRayBackup)), I'm going to re-organize my data by hotness and coldness, and have different back up intervals depending on that, simply because I don't want to spend more than a day or two on this every year (current estimate for backup time is around 36 hours or about 5 work days).
-   At some point, make a second copy of the blu-ray backup and store it off-site at mom's house in Clinton, NY (or possibly rent a lock box there).
-   The rationale for backing up to blu-ray is as follows:
    -   It's a write-once medium, and most of my data doesn't really change.
    -   It's cheap (although not as cheap as Glacier or Deep Glacier).
    -   Most importantly, in the event that something happens to me, my next of kin (being much less technical than me) will be much more capable of dealing with a medium like blu-ray than dealing with AWS. Per this point, I'm also planning on just using a standard filesystem with no encryption or any other fancy features (such as snapshots); security will be enforced by encryption on a file by file basis for sensitive documents and physical lock and key.
    -   If I want, I can also tier snapshots down from a spinny disk to blu ray for my nearline backup.
-   Add the spare WD Blue into slot 3 of the Rosewill cage *DONE:20*
-   Evict one of the WD Blues from the ZFS mirror. *DONE:20*
-   Create a RAIDZ1 volume from the two WD Blues that aren't in the mirror.  Enable deduplication and compression.  Use a sparse file for the third drive in the vdev (see [here](http/superuser.cquestio2818start-a-zfs-raidz-zpool-with-two-discs-then-add-a-third)). *DONE:20*
-   Stream current mirrored pool data from the remaining mirror drive to the new RAIDZ1 volume with *zfs send*. *DONE:20*
-   Destroy the mirro remove the final drive from the mirror. *DONE:20*
-   Add the final drive as a third disk to the RAIDZ1 vdev and wait for parity data to be redistributed. *DONE:20*
-   At some point (possibly before this migration), delete all the snapshots that currently exist.
-   On the new RAIDZ1 vdev, refactor the pool so that data is organized somewhat logically (i.e., a dataset for digitized files from my mom's house, a dataset for music, a dataset for clogmail backups, a dataset for my audio diaries, a dataset for photos, etc). Separating my files into separate datasets makes restores slightly easier, since I can start with the full backup for whichever logical division I want first and ignore the others as necessary (i.e., if my workstation has been nabbed, I'd like to be able to prioritize the restoration of certain data over other data; tax data \> Star Wars Holiday Special)
-   Adjust current setup as necessary to accommodate these changes.
-   Stop replicating data in your S3 bucket from Ohio to Canada. Having your backups replicated in 2 AWS regions + 2 copies of full blu-ray backups + a nearline backup to blu-ray is definitely overkill. At max, just use one region.
-   Make the ZFS backup script robust to internet outages. Parameterize parts of it as necessar make some bash functions.

#### Reprovisioning Tasks

-   Download Proxmox and put it on a thumb drive.
-   Completely hose the CentOS 7 install you have on maxwell and replace it with Proxmox.

#### Making Maxwell a Managed Host

-   Make an Ansible role for the ZFS backup scripts (these will need to run under Proxmox). Investigate if Proxmox has something better.
-   Make an Ansible role for the Twitter backups. *(Done* [here](http/github.cjpellmansible-twitter-backup)*; untested, but I don't really feel that this is so essential that I can't test it after Maxwell is rebuilt)*
-   Make an Ansible role for the rclone backups. *(Done* [here](http/github.cjpellmansible-rclone)*; untested, but I don't really feel that this is so essential that I can't test it after Maxwell is rebuilt)*
-   Make an Ansible role for the gmvault backups. *(Done* [here](http/github.cjpellmansible-gmvault)*; untested, but I don't really feel that this is so essential that I can't test it after Maxwell is rebuilt)*
-   Make Ansible roles for boinc and <folding@home> (can be done after Maxwell has been rebuilt)

#### VM Creation

-   Create a CentOS 6 VM for BOINC and FAH. We want to use CentOS 6 because the FAH packages still need Python 2.6 (unless you modify them manually to use Python 2.7 in CentOS 7, which is a bit of a pain). Attach thumb drive to this VM (possibly a silly RAID of thumb drives) and have it be the backing storage for at least the scratch storage used by BOINC. Why thumb drives? Because they're cheap and I don't want to wear down my spinny disks or SSDs with a bunch of scratch files. Give this VM access to GPUs and 8 vCPUs.
-   Create a CentOS 7 VM for general file acces ZFS. Give it 2 vCPUs. This VM may also contain the Twitter CLI (possibly within an RVM environment), gmvault and all of the other internet presenc personal data backup cronjobs (I may make one of these for my reddit data using [PRAW](http/praw.readthedocs.io)).
-   I may then experiment with a Docker VM and getting my Windows 10 installation to run as a VM. If I can get GPU passthrough working with a Docker VM, I may retire the CentOS 6 VM and replace it with a Docker container (or split FAH and BOINC into multiple containers).
-   I'm then going to replace the [MoinMoin](MoinMoin) instance I've been running with [Monica](http/www.monicahq.c). (I actually don't think I care enough about this, but if I do, I'll revisit it. I barely use the Moinmoin instance as it is.)

### Detailed Notes of ZFS Mirror to RAIDZ1 Transition

Note: Encrypted snapshots are on external HD if this goes badly.

1.  Disable user cronjobs for user *jpellman*.
2.  As root in screen session: Go to multi-user target with `systemctl isolate multi-user`, turn off BOINC, unmounthoboinc* andhome*. Ensure thathojpellman* isn't being mounted on [Bruno](Bruno) using sshfs.
3.  Create a sparse file using the number of bytes provided by `fdisk -l`: `truncate -s 100020488601roraidz1_faux_drive.img`
4.  Offline one of the drives in the ZFS mirror: `zpool offline pool0 ata-WDC_WD10EZEX-08WN4A0_WD-WCC6Y3NSTU5Z`
5.  Clear out the partition label for the offlined disk:

<!-- -->

    zpool export pool0
    zpool labelclear -ddiby-ata-WDC_WD10EZEX-08WN4A0_WD-WCC6Y3NSTU5Z-part1

1.  Create a new volume with the offline drive and the spare WD Blue you added: `zpool create datastore raidzroraidz1_faux_drive.imddiby-ata-WDC_WD10EZEX-08WN4A0_WD-WCC6Y3NSTU5ddiby-ata-WDC_WD10EZEX-00WN4A0_WD-WCC6Y7AKHNY8`
2.  Turn deduplication and compression on by default at the pool level.

<!-- -->

    zfs set compression=lz4 datastore
    zfs set dedup=on datastore

1.  Offline the sparse image.

<!-- -->

    zpool offline datastorroraidz1_faux_drive.img

1.  Transfer data from the old pool to the new pool.

<!-- -->

    zpool import pool0
    zfs send -R pooapache@200119 | zfs receive datastoapache
    zfs send -R poohome@200119 | zfs receive datastohome

1.  Mount the new pool and verify that it looks right.

<!-- -->

    zfs get mountpoint datastohome
    # Set it if not appearing above
    zfs set mountpoinhome datastohome
    zfs mount datastohome

1.  Destroy the old pool. `zpool destroy pool0`
2.  Add in the other disk. `zpool replace datastorroraidz1_faux_drive.imddiby-ata-WDC_WD10EZEX-08WN4A0_WD-WCC6Y7ZT6K9C`

Other Wants
-----------

-   I want to get rid of the Dell monitor I've been using to access Maxwell. It's an old monitor from the mid-2000s at the earliest, it's clunky, and it's a major PITA to move from one apartment to another. For OS-level remote desktop work, VNC, RDP and x2go are more than appropriate. If I want to update BIUEFI settings though, I still need a monitor because MSI's firmware includes this goofy graphical interface with no text-only option (if there were a text-only option, I'd presumably be able to just connect via a serial interface). I very rarely do firmware-level config updates, but I still need a monitor for it for the 2 or 3 times I do. [diyiipmi](http/github.cFmstrdiy-ipmi) is a probable candidate for this, although it's almost too expensive to be worth it. I'm pretty sure the Dell monitor cost like \$20, whereas diy-ipmi would cost \~ \$120, with the main tradeoff being that I don't have to deal with more crap in my apartment. More research:
    -   <http/www.reddit.cr/sysadmcommengs2kvm_over_c1pv4>
    -   <http/www.reddit.cr/homelcommen8pvsturn_laptop_into_kvm_monitorkayboa>
    -   <http/www.reddit.cr/sysadmcommenx2jis_there_a_way_to_add_something_like_ipmi_to>
    -   <http/www.reddit.cr/linuxadmcommen1d10what_do_you_use_for_remote_server_consol>
-   The 240 GB SSD isn't really being leveraged to its full potential. I should maybe split this into 3 partitions, with one for the OS and two others for a ZIL and L2ARC for ZFS. Alternatively, I could use the 60 GB SSD as a ZL2ARC cache, since I don't really care as much about it. It could live in the 4th bay of the Rosewill hot-swap cage.
    -   **As of20**, the 60 GB SSD is now in the 4th Rosewill bay.
-   I'm very rapidly running out of disk space on my mirrored ZFS volume as I digitize items in my mom's house. It probably would make the most sense to redo that as a RAIDZ1 volume using the third WD Blue I have lying around.

Photos
------

attachment:IMG\_20190121\_154736836.jpg\_attachment:IMG\_20190121\_154736836.jpg\_attachment:None\_ attachment:IMG\_20190121\_154801532.jpg\_attachment:IMG\_20190121\_154801532.jpg\_attachment:None\_ attachment:IMG\_20190121\_154834420.jpg\_attachment:IMG\_20190121\_154834420.jpg\_attachment:None\_

* * * * *

> [Hosts](Hosts)
