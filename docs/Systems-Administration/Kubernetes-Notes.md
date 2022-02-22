# Kubernetes Notes

I'm using this page as an unorganized dumping ground for various thoughts on k8s.

## k8s as an operating system

Kubernetes is often thought of as a sort of second-level operating system, or an operating system that runs on top of another (lower-level) operating system (currently this is only GNU/Linux, although in principle a version of Kubernetes could be built for Solaris Zones or FreeBSD jails).  

By Andrew Tanenbaum's definition, a conventional first-level OS provides abstract interfaces to hardware for programmers (i.e., system calls) and a way of managing hardware resources (i.e., a process scheduler, I/O scheduler, drivers).  Kubernetes, as a second-level OS, provides abstract interfaces not to low-level hardware resources, but to coarse-grained allocations of resources (e.g., CPU time, memory, whole GPUs / ASICs) and a sort of proxy-based switching setup (e.g., Services) using abstract objects.  Just as a first-level operating system uses processes to enforce isolation between programs running in tandem, Kubernetes uses Pods/containers/cgroups to enforce isolation.  Pods are like processes, containers are like threads.

An operating system is like a government, and the layering of a second-level OS (Kubernetes) on top of a first-level OS (GNU/Linux) is like a kind of federalism.

The Kubernetes control plane is almost like a microkernel in how it functions.  Services within the `kube-system` namespace are like userspace-based drivers / components in a microkernel system (e.g., the file system, drivers, etc).  Microservices are processes that live within userspace and make heavy use of interprocess communication (i.e., HTTP calls).  `kube-proxy` is the Kubernetes control panel's implementation of IPC.  Istio / service meshes are an alternative implementation of IPC where routing functionality, logging, and security are tightly-coupled with a service as a sidecar/ambassador container (i.e., a thread).

A traditional distributed OS attempts to create a single virtual machine that spans many nodes using a microkernel.  The cost of this lofty goal is that distributed operating systems are typically extremely complex / are a beast to maintain.  By separating coarse-grained allocation of resources (handled by Kubernetes within userspace) from fine-grained allocation of resources (handled by GNU/Linux on individual hosts) and making nodes more loosely-coupled instead of integrated into a single cohesive whole, the Kubernetes developers have decreased complexity while providing many of the advantages of the distributed operating system (in terms of providing resources at scale and optimizing resource utilization).  A true distributed operating system should in theory be able to make scheduling / resource allocation decisions that are better than Kubernetes, but Kubernetes is adequate and easier (perfect is the enemy of good).
