

How to Create an AMI to Run BOINC
=================================

Why Run BOINC In the Cloud
--------------------------

Consumer PCs are not designed for power-hungry, memory-intensive scientific computing applications. Server hardware is. Even with the performance penalty for virtualization, it's much better to have numbers being crunched in a data center than on your laptop; you won't drive up your electric bill and incur needless wear and tear on your everyday electronics.

Launch An Instance Using the Starcluster AMI
--------------------------------------------

Start an instance with one of the public Starcluster AMIs, since they already have many drivers and applications pre-installed for HPC (BLAS,CUDA,etc). Choose an HVM AMI, since these will include GPU support (should you ever want to use a GPU-based instance type). I chose Ubuntu 12.04 (starcluster-base-ubuntu-12.04-x86\_64-hvm; ami-52a0c53b). Avoid Ubuntu 13.04, as support for that from Canonical is spotty.

Install A Lightweight GUI and Remote Desktop Server
---------------------------------------------------

There are some operations for BOINC that you can accomplish from the command line (boinccmd). Other operations (such as changing resources allocated to BOINC) are not possible or are difficult. A lot of BOINC's design seems to be centered upon the user interacting with the client via the graphical BOINC manager.

To get around this, install a lightweight GUI like lxde and a remote desktop server like x2go.

Create an AttachabDetachable Volume
--------------------------------------

Make a new volume in the AWS console. Attach to the instance. Partition, create a file system and mount at a suitable location (likeboinc').

Install BOINC
-------------

Use apt-get or yum to install BOINC client and BOINC manager. Move BOINC client's data frovlboinc-client to the new volume you created (mounted atboinc' or wherever you decided to mount it). Ediedefauboinc-client and change BOINC\_DIR fromvlboinc-client" to the new mount point boinc').

Separating the data from the instance's root volume allows the tasks that were currently running to be preserved in the case of a poweroff (i.e., if you are using spot instances and the instance is abruptly terminated).

Save the Instance as an AMI
---------------------------

Remove the bash history, ssh directory in your home folder. Save as an EBS-backed AMI in the AWS console.

When Running
------------

When you start a new instance with the AMI, don't forget to a) mount the attached volume and b) start the BOINC client service with sudeinitboinc-client start.

With Spot Instances
-------------------

Make a snapshot of the BOINC data volume beforehand, since you don't know which AZ the instance will pop up in. Make new volume from snapshot in the instance's AZ accordingly.

* * * * *

> [Scientific-Computing](Scientific-Computing)
