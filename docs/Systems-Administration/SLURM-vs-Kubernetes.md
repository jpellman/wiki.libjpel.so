SLURM vs Kubernetes vs Nomad
============================

-   **Features:** SLURM is primarily focused on just scheduling, whereas Kubernetes has a scheduler (kube-scheduler), distributed configuration (etcd), and control loops / negative feedback loops (kube-controller-manager; a la Norbert Wiener / cybernetics) plus custom logic to deal with the fact that the unit of scheduling is a grouping of containers (a pod) instead of a group of processes (i.e., containers need to have networking, DNS, etc configured dynamically). There is, however, no reason why SLURM could not also have some of these features in theory (i.e., [confd](https://github.com/kelseyhightower/confd) could be combined with SLURM and etcd to give SLURM a distributed configuration that is dynamically updated).
-   **Unit of Scheduling:** SLURM schedules *jobs* (typically one or more processes), while Kubernetes schedules *pods* (groups of containers). Jobs can have resource isolation via cgroups, but don't have namespace isolation or any fancy logic to deal with filesystems (i.e., union file systems). Basically, jobs have 1/3 of what makes up a container. If namespace isolation and union filesystems aren't important, SLURM has a compelling advantage over Kubernetes due to having less complexity/overhead.
-   **Scheduling Algorithms:** SLURM uses a priority queue or a backfill algorithm. Kubernetes filters available nodes, assigns them a priority score, and then pops off the node with the highest score (so also a priority queue most likely; see [here](https://github.com/eBay/Kubernetes/blob/master/docs/devel/scheduler_algorithm.md)). Hashicorp Nomad uses a bin-packing algorithm (see [here](https://nomadproject.io/docs/internals/scheduling/scheduling/)).

SLURM / Kubernetes Analogies
-----------------------------

|Kubernetes|SLURM|
|-----------|-------|
| Namespace | Partition |
| kubelet | slurmd |
| kube-scheduler / kube-controller-manager / slurm-apiserver | slurmctld |
| Container Runtime | Vanilla cgroups |
| etcd | slurm.conf + NFS |
| Prometheus / ELK | slurmdbd (?) |
| Labels / Selectors | GRES / TRES / Features |
| Marking a node as unschedulable / cordoning | Draining a node / Making a resource reservation |

Further Reading
---------------

-   [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
-   [Docker Overview](https://docs.docker.com/engine/docker-overview/)
-   [A Summary of OverlayFS](https://jvns.ca/blog/2019/11/18/how-containers-work--overlayfs/)
-   [Scheduler Algorithm in Kubernetes](https://github.com/eBay/Kubernetes/blob/master/docs/devel/scheduler_algorithm.md)
-   [More up-to-date overview of scheduling in Kubernetes](https://kubernetes.io/docs/concepts/configuration/scheduling-framework/)
-   [Scheduling in Nomad](https://nomadproject.io/docs/internals/scheduling/scheduling/)
-   [Cgroups Guide](https://slurm.schedmd.com/cgroups.html) (SLURM)
-   [Scheduling Configuration Guide](https://slurm.schedmd.com/sched_config.html) (SLURM)

