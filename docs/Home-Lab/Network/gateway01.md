gateway01
=========

Description
-----------

gateway01 is a firewall appliance / router running pfSense on top of a [Protectli Vault FW2](https://www.amazon.com/gp/product/B01KLECNDG/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1).  A hardware overview can be found [here](https://protectli.com/kb/fw4-series-hardware-overview/) on the Protectli website.

Part of my motivation for putting this appliance together is that I noticed that [ap01](ap01.md) was running on an ancient version of the Linux kernel that hadn't been updated since 2008, and [ap02's](ap02.md) firmware couldn't be updated past Kong's 2015 build of dd-wrt.  I wanted the main gateway to my LAN to be a piece of hardware that was a) readily updatable, b) versatile (in terms of being able to switch out firmware) and c) secure.  The Protectli satisfied these criteria by using the most mainstream CPU architecture in the consumer market (x86_64; although ARM was also appealing) and basically being a full-fledged PC (that is nonetheless not as powerful as most modern desktops).  Right now it runs pfSense, but if I ever want to switch to another OS (i.e., if pfSense gets abandoned and doesn't receive security updates or similar) I should be able to do so quite readily (worst case scenario I could just use plain Linux with iptables/firewalld; see [here](https://arstechnica.com/gadgets/2016/04/the-ars-guide-to-building-a-linux-router-from-scratch/)).

Specifications
--------------

| Key | Value |
| --- | --- |
| **CPU** | [Celeron J1800](https://ark.intel.com/content/www/us/en/ark/products/78866/intel-celeron-processor-j1800-1m-cache-up-to-2-58-ghz.html) |
| **# of Cores (logical)** | 2 |
| **CPU Clock Speed (GHz)** | 2.41 |
| **Memory (GB)** | 4 (DDR3 SODIMM) |
| **Disks** | [32 GB mSATA](https://www.amazon.com/gp/product/B00K64HXRS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) |
| **OS** | pfSense |
| **IP Address** | 192.168.1.1 |

Configuration Backup
--------------------

I have not yet backed up the configuration for this.  After I create a dedicated backup machine I'll stash a backup there.
