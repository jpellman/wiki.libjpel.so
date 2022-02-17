hypervisor01
============

Description
-----------

hypervisor01 (formerly known as Maxwell; I've stopped doing pet names for machines because I find such names obnoxious) is essentially a gaming workstation that I use to try out new things locally within my apartment. It runs [Proxmox VE](https://www.proxmox.com/en/) 6.2-4 off of a 240 GB SSD. I first built it around February/March 2017, with a goal of creating a workstation that I could use for both experimentation and running [BOINC](https://boincstats.com/en/stats/-1/user/detail/3500755).  Frankly, part of my motivation was to see how close I could get to surpassing (or at least equalling) some of the older scientific lab hardware I had dealt with in the past using only consumer-grade parts.

Specifications
--------------

| Key | Value |
| --- | --- |
| **CPU** | Core I7-6700 FC-LGA14C |
| **# of Cores (logical)** | 8 |
| **CPU Clock Speed (GHz)** | 3.40 |
| **Memory (GB)** | 32 |
| **Disks** | 240 GB SSD (Linux volume) |
| **OS** | Proxmox VE 6.2-4 |
| **IP Address** | 192.168.1.10 |
| **Ansible Playbook** | [hypervisor.yml](https://github.com/jpellman/home-ansible/blob/master/playbooks/hypervisor.yml) |

### Part List

 * [Zalman MS800 ATX Mid Tower Gaming Case (Black)](https://smile.amazon.com/gp/product/B00I0V4IMW/ref=ppx_yo_dt_b_asin_title_o03__o00_s01?ie=UTF8&psc=1)
 * [Rosewill 3 x 5.25-Inch to 4 x 3.5-Inch Hot-swap SATA III/SAS Hard Disk Drive Cage - Black](https://smile.amazon.com/gp/product/B00DGZ42SM/ref=ppx_yo_dt_b_asin_title_o03__o00_s00?ie=UTF8&psc=1)
 * [SanDisk SSD PLUS 240GB Internal SSD - SATA III 6 Gb/s](https://smile.amazon.com/gp/product/B01F9G43WU/ref=ppx_yo_dt_b_asin_title_o00__o00_s00?ie=UTF8&psc=1)
 * [Intel Boxed Core I7-6700 FC-LGA14C 3.40 GHz 8 M Processor Cache 4 LGA 1151 BX80662I76700](https://smile.amazon.com/gp/product/B0136JONG8/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
 * x2 [Crucial 16GB Single DDR4 2133 MT/s (PC4-17000) DR x8 Unbuffered DIMM 288-Pin Memory - CT16G4DFD8213](https://smile.amazon.com/gp/product/B015YPAZPU/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
 * [MSI Pro Solution Intel Z170A LGA 1151 DDR4 USB 3.1 ATX Motherboard (Z170A SLI)](https://smile.amazon.com/gp/product/B01DDR05P6/ref=ppx_yo_dt_b_asin_title_o02__o00_s00?ie=UTF8&psc=1)
 * [Corsair CX Series 750 Watt 80 Plus Bronze Certified Non-Modular Power Supply (CP-9020015-NA)](https://smile.amazon.com/gp/product/B008RJZQSW/ref=ppx_yo_dt_b_asin_title_o09__o00_s00?ie=UTF8&psc=1)
 * [EVGA GeForce GTX 1050 SC ITX, 2GB](https://smile.amazon.com/EVGA-GeForce-Support-Graphics-02G-P4-6152-KR/dp/B01M64G435?sa-no-redirect=1)

Applications
------------

 * KVM 
 * Proxmox
 * nginx (reverse proxy for Proxmox)

Service Accounts
----------------

 * `packerserv`: Used to create VM templates using Packer's `proxmox-iso` builder (see [here](https://www.packer.io/plugins/builders/proxmox/iso)).  Repository for VM templates can be found [here](https://github.com/jpellman/home-packer). 

Notes
-----

 * GPU passthrough is enabled.  This could not be accomplished previously when this workstation ran CentOS because Red Hat deliberately cripples GPU passthrough for consumer-grade cards in RHEL (see [here](https://bugzilla.redhat.com/show_bug.cgi?id=1492173)).
 * The GPU is assigned to one VM ( *compute01*; no article yet as of writing), which runs [Folding@Home](https://foldingathome.org/) and [BOINC](https://boinc.berkeley.edu/).
