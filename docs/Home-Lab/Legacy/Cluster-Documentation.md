# Documentation for Home Beowulf Cluster - SDH (The Salon of Digital Humanists)

An inventory of all the computers used in my home cluster, including their specs, software installed, the present topology of the cluster, and the users.

## Section 1: Machine Specifications

### Hugo (head node)

| Key | Value |
| --- | --- |
|**Brand**| Apple Macbook Pro (circa 2008) |
|**CPU**| 2.4 Ghz Intel Core 2 Duo (64-bit) |
|**Cores**| 2 |
|**RAM**| 2 GB |
|**Graphics Card**| NVIDIA GeForce 8600M GT |
|**Hard Drive**| 142 GB (according to df) |

### Voltaire

| Key | Value |
| --- | --- |
|**Brand**| Apple iBook G4 (circa 2006) |
|**CPU**| 1.33 Ghz PowerPC 7447a (32-bit) |
|**Cores**| 1  |
|**RAM**| 512 MB |
|**Graphics Card**| ATI Mobility Radeon 9550 |
|**Hard Drive**| 40GB (36 GB according to df)  |

### Montaigne

| Key | Value |
| --- | --- |
|**Brand**| Custom Made (circa 2002)  |
|**CPU**| 900 Mhz AMD Duron (32-bit) |
|**Cores**| 1 |
|**RAM**| 512 MB SDRAM |
|**Graphics Card**| (2) ATI Rage 128 and ATI Radeon 9000 |
|**Hard Drive**| 15.3 GB (14 GB according to df) |

### Cervantes

| Key | Value |
| --- | --- |
|**Brand**| Macbook Pro (circa 2011) |
|**CPU**| 2.5 Ghz Intel Core 2 Duo (64-bit) |
|**Cores**| 2  |
|**RAM**| 4 GB (hypervisor); 2 GB (VM) |
|**Graphics Card**| NVIDIA GeForce 8600M GT (128 MB video memory for VM) |
|**Hard Drive**| 320 GB (hypervisor); 181 GB (VM) |

## Section 2: Software Installed

### Hugo (head node)

 * nfs-kernel-server
 * OpenSSH
 * PostgreSQL 8.4
 * MPICH
 * R 2.10.1 (r-base)
 * dsh
 * slapd, ldap-utils
 * SLURM (not presently configured)

### Voltaire

 * nfs-common
 * OpenSSH
 * PostgreSQL 8.4
 * MPICH
 * R 2.10.1 (r-base)
 * dsh
 * slapd, ldap-utils

### Montaigne

 * nfs-common
 * OpenSSH
 * PostgreSQL 8.4
 * MPICH
 * R 2.10.1 (r-base)
 * dsh
 * slapd, ldap-utils

### Cervantes

 * nfs-kernel-server
 * nfs-common
 * OpenSSH
 * PostgreSQL 8.4
 * SLURM (not presently configured)
 * dpkg-server

## Section 3: Network Topology

Hugo, Voltaire, Montaigne and Cervantes are connected to a 6 port hub, with 4 ports used.  1 port is broken.  The last port is an unused uplink port.
All nodes can connect to each other.  Cervantes can connect outside of the LAN using Wifi, and is thus used as a means of downloading packages from the Canonical repos.  Cervantes has a user (*installuser*) whose home directory is mounted as an nfs partition on the other nodes- this user's home directory contains .deb files and a Packages.gz file.

## Section 4: Users

### Hugo (head node)

 * jpellman
 * mpiuser (home folder is nfs mount; hugo is nfs server), uid=999
 * installuser (home folder is nfs mount; fstab modified), uid=998

### Voltaire

 * jpellman
 * mpiuser (home folder is nfs mount; fstab modified), uid=999
 * installuser (home folder is nfs mount; fstab modified), uid=998

### Montaigne

 * jpellman
 * mpiuser (home folder is nfs mount; fstab modified), uid=999
 * installuser (home folder is nfs mount; fstab modified), uid=998

### Cervantes
 * jpellman
 * mpiuser (home folder is nfs mount; fstab modified), uid=999
 * installuser (home folder is nfs mount; cervantes is nfs server), uid=998

## TODO

 * Install SLURM.  
 * Configure SLURM on all nodes. Complication: Version of SLURM installed on Cervantes and Hugo is 64-bit.  Will need to recompile SLURM for 32-bit if possible.
