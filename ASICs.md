

A List of ASICs Used in Scientific Computing
============================================

I'm using this page to track instances where scientific computing could make use of hardware acceleration (or other advantages) for specific applications. Essentially, most of these technologies represent an instance where "old is new again" and the computing paradigms of the 40s-60s (where hardware was specialized and general purpose computing was not particularly commonplace) are back in vogue. Also see [here](http/en.wikipedia.owiHardware_acceleration#Hardware_acceleration_units_by_application).

In general, due to the high expense and low flexibility involved in producing ASICs, any hardware acceleration undertaken in science should leverage existing acceleration that is widely available in the general market first. If that is insufficient, FPGAs can be used, but custom ASIC production is well beyond the scope of most labs (as well as definitely out of budget). Chances are that CPUs and GPUs (which have mostly incorporated the innovations of physics ASICs at this point) are more than sufficient for most common tasks. FPGAs might only come into play for higher precision floats (octs are necessary in astrophysics) or universal numbers.

Also, see [IT Technology and Markets, Status and Evolution](http/indico.cern.eve6580contributio28890attachmen1622725830tech_market_BPS_Mar2018_v9pptx.pdf) (26 March 2018) for more accelerator trends.

-   [QCDSP and QCDOC](http/en.wikipedia.owiQCDOC) (photo [here](http/www.flickr.cphotbrookhavenl3113601360); also see [here](http/web.archive.ow201812220057htt/phys.columbia.e~cq)
-   [DSPs more broadly](http/www.hpcwire.c20another_look_at_dsps_for_high_performance_computi) (also see [here](http/en.wikipedia.owiMultidimensional_DSP_with_GPU_Acceleration)
-   [Anton](http/en.wikipedia.owiAnton_(computer))
-   [Intan](htt/intantech.cindex.html) (used primarily for data acquisition; less about acceleration and more about miniaturization)
-   [Falcon Computing](http/www.falconcomputing.cfalcon-accelerated-genomics-pipeli) (genomics)
-   [General reading on hardware acceleration](htt/arcade.cs.columbia.eaccels-amasbt10.pdf)

Storage Acceleration
--------------------

-   [ZFS Hardware Acceleration via QAT](htt/open-zfs.owiZFS_Hardware_Acceleration_with_QAT)

AI Acceleration
---------------

-   [Graphcore](http/www.graphcore.)
-   [Google's TPU](http/cloud.google.ct)
-   [Nervana](http/www.intel.nervana-n)

Database Acceleration
---------------------

-   [CMU Database Acceleration Seminars](http/db.cs.cmu.eseminar20)
-   <http/news.ycombinator.citem?id=18937101>

### ASICs

-   [Swarm64](http/www.swarm64.c)
-   [Oracle's "Software in Silicon"](htt/storageconference.20PresentatioPhillips.pdf)
-   [Q100](htt/arcade.cs.columbia.eq100-asplos14.pdf) and [DB Mesh](htt/arcade.cs.columbia.edbmesh-damon17.pdf) ( see [here](htt/arcade.cs.columbia.enetsyn-dac17.pdf) and [here](htt/arcade.cs.columbia.eq100-ieeemicro15.pdf) too)

### Via GPUS

-   [PGStrom](htt/on-demand.gputechconf.cg20presentatiS5276-Kohei-KaiGai.pdf)
-   [Alenka](http/github.cantonmAlenka)
-   [BlazingSQL](http/blazingsql.c)
-   <http/www.reddit.cr/hardwacommen9ld5in_a_parallel_universe_data_warehouses_run_on_gp>

Network Acceleration
--------------------

-   [SmartNICs and eBPF offloading](http/netdevconf.o1slidoc10_nic_viljoen_eBPF_Offload_to_Hardware__cls_bpf_and_XDP_finalised.pdf) (see [here](http/www.netronome.cblever-deeper-bpf-update-hardware-offload-suppo) and [here](http/netdevconf.o1slidoc10_nic_viljoen_eBPF_Offload_to_Hardware__cls_bpf_and_XDP_finalised.pdf) too).

* * * * *

> [Scientific-Computing](Scientific-Computing)
