Johns-MBP
=========

Description
-----------

Johns-MBP (formerly known as Bruno) is a [Mid 2012, 13-inch MacBook Pro](https://apple-history.com/mbp_13_mid_12).  I bought it refurbished around 1/1/15 and it is still kicking.  Prior to 2021, it had several issues, some of which have been corrected while the others I've come to tolerate.

It currently dual boots into both macOS Catalina and macOS High Sierra. Catalina is for everyday use (web browsing, etc) because it continues to receive security updates (as of early 2022; Apple will likely stop providing security updates in November 2022, but who really knows what their timelines are).  That said, there are some caveats to *how quickly* Apple provides patches for Catalina (see [here](https://arstechnica.com/gadgets/2021/11/psa-apple-isnt-actually-patching-all-the-security-holes-in-older-versions-of-macos/)).

The High Sierra boot partition is only used for the following applications:

 * iMovie HD 6; this is being run in an [incredibly hacky way](http://blog.iharder.net/2015/01/23/run-imovie-hd-and-maybe-other-older-applications-in-yosemite/) in order to rip a bunch of older DV tapes in my mom's house, and newer versions of OS X deprecate at least one Cocoa API call that iMovie HD 6 depends on.  This might no longer be necessary, since I *think* I ripped all the DV tapes at my mom's house in late 2020, but maybe not.
 * 32-bit OS X apps a.k.a. *most* of my Steam library (see [here](https://help.steampowered.com/en/faqs/view/5E0D-522A-4E62-B6EF#:~:text=Yes.,many%20cases%20Linux%20as%20well.)).  Kind of a reasonable idea, but also a very unnecessary and brusque move on Apple's part (even thought the decision is far in the past at this point).

Catalina has the following applications installed:

 * Vagrant
 * VMWare Fusion Desktop
 * Docker Desktop
 * Kodi
 * Malwarebytes
 * Signal
 * Veracrypt

The overall partition scheme is such that there are several major APFS volumes:

 * High Sierra boot volume
 * Catalina boot volume
 * Logical volume for Google Drive mirror / sync
 * Logical volume to hold personal multimedia (i.e., home videos, digitized DV tapes, digitzed photos, contemporary photos/videos from phone)
 * Logical volume to hold VMs

Separating my data into distinct APFS volumes makes it easier to perform selective backups.

### What's Broken

 * One of the RAM slots is bad (see [here](https://www.youtube.com/watch?v=xpagfXraSn4) and [here](https://www.reddit.com/r/computertechs/comments/4gu93k/starting_to_see_mid2012_13_macbook_pro_bottom_ram/)). Essentially Apple used two different types of solder for the RAM banks and one of them is more liable to crap out. As such I only use one RAM slot now, with half of the MacBook's original RAM (4 GB). In theory I could purchase a single 8 GB SODIMM to fill in this one slot, but I've never felt it to be particularly worth it / performance with 4 GB RAM has been good enough for my purposes (90% of the gaming I do involves 2D graphics only).

### What's Fixed

 * Modern versions of OS X seem to assume that they're running on SSDs ([APFS definitely makes this assumption](https://blog.macsales.com/43043-using-apfs-on-hdds-and-why-you-might-not-want-to/)) and don't run well at all on mechanical disks. To work around this, I switched out Johns-MBP's spinning disk to an SSD. Of course, this might just be because I've become so used to SSDs that I can't tolerate the slow speeds of spinning disks, although [anecdotally](https://arstechnica.com/civis/viewtopic.php?p=32860197&sid=b7559584bdb86396f9a4dcf1500d1901#p32860197) some other people blame Apple as well.
 * Touchpad was replaced around 9/17/21 ([part](https://www.ifixit.com/Store/Mac/MacBook-Pro-13-Inch-Unibody-Mid-2009-Mid-2012-Trackpad/IF163-025?o=1))
 * Battery has been replaced with an aftermarket battery around 9/17/21 ([part](https://www.ifixit.com/Store/Mac/MacBook-Pro-13-Inch-Unibody-Mid-2009-Mid-2012-Battery/IF163-054))
 * Ailing DVD drive that constantly sounded like it was raspily chanting, "Kill meeee" has been replaced with a second SSD ( ~ 12/4/21; [part](https://www.ifixit.com/Store/Mac/Unibody-Laptop-Dual-Drive/IF107-080))

### What I Like

 * Having an actual Ethernet port and not having to deal with the dongle hell bullshit of the newer USB-C and Thunderbolt 3 Macs.
 * Not having to deal with that asinine / comically useless touch bar.
 * Being able to actually fix parts / take this laptop apart. I believe that this is one of the last Mac models that you can potentially self-service or upgrade/tweak. All of the modern ones involve gluing components together in an unnecessarily thin chassis. I'd gladly trade functionality for aesthetics.

Specifications
--------------

| Key | Value |
| --- | --- |
| **CPU** | Core i7 |
| **# of Cores (logical)** | 4 |
| **CPU Clock Speed (GHz)** | 2.9 |
| **Memory (GB)** | 4 |
| **GPU** | Intel HD Graphics 4000 1536 MB |
| **Disks** | 250 GB SSD (boot volume) , 1 TB SSD (photos, home movies, etc) |
| **OS** | macOS High Sierra (10.13), macOS Catalina (10.15) |

Plans
-----

The electricity consumption on the laptop isn't that bad and it seems serviceable enough, so I'm aiming to try to get 1-2 more years of use out of it (as of January 2022).  When Apple stops providing security updates for Catalina, I'll start doing web browsing in a virtualized sandbox running [Neverware](https://www.neverware.com/) to mitigate risk.

I'll probably replace this with an ARM-based MacBook. I've toyed around with just using a tablet (e.g., iPad, Surface) in the past, but due to the amount of multimedia work I do as I digitize documents and other media in my childhood home, I think that I'll still need a portable computer with a modest amount of horsepower.
