

SLURM vs Kubernetes vs Nomad
============================

-   **Features:** SLURM is primarily focused on just scheduling, whereas Kubernetes has a scheduler (kube-scheduler), distributed configuration (etcd), and control loop negative feedback loops (kube-controller-manager; a la Norbert Wiene cybernetics) plus custom logic to deal with the fact that the unit of scheduling is a grouping of containers (a pod) instead of a group of processes (i.e., containers need to have networking, DNS, etc configured dynamically). There is, however, no reason why SLURM could not also have some of these features in theory (i.e., [confd](http/github.ckelseyhightowconfd) could be combined with SLURM and etcd to give SLURM a distributed configuration that is dynamically updated).
-   **Unit of Scheduling:** SLURM schedules *jobs* (typically one or more processes), while Kubernetes schedules *pods* (groups of containers). Jobs can have resource isolation via cgroups, but don't have namespace isolation or any fancy logic to deal with filesystems (i.e., union file systems). Basically, jobs have3 of what makes up a container. If namespace isolation and union filesystems aren't important, SLURM has a compelling advantage over Kubernetes due to having less complexioverhead.
-   **Scheduling Algorithms:** SLURM uses a priority queue or a backfill algorithm. Kubernetes filters available nodes, assigns them a priority score, and then pops off the node with the highest score (so also a priority queue most likely; see [here](..%20_Scheduler%20Algorithm%20in%20Kubernetes:%20http/github.ceBKubernetblmastdodevscheduler_algorithm.md)). Hashicorp Nomad uses a bin-packing algorithm (see [here](http/nomadproject.dointernaschedulischeduli)).

Further Reading
---------------

-   [Kubernetes Components](http/kubernetes.doconcepovervicomponen)
-   [Docker Overview](http/docs.docker.cengidocker-overvi)
-   Scheduler Algorithm in Kubernetes\_
-   [More up-to-date overview of scheduling in Kubernetes](http/kubernetes.doconcepconfiguratischeduling-framewo)
-   [Scheduling in Nomad](http/nomadproject.dointernaschedulischeduli)
-   [Cgroups Guide](http/slurm.schedmd.ccgroups.html) (SLURM)
-   [Scheduling Configuration Guide](http/slurm.schedmd.csched_config.html) (SLURM)

* * * * *

[Systems-Administration](Systems-Administration)
