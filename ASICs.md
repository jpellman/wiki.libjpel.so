\#format rst

A List of ASICs Used in Scientific Computing
============================================

I'm using this page to track instances where scientific computing could make use of hardware acceleration (or other advantages) for specific applications. Essentially, most of these technologies represent an instance where "old is new again" and the computing paradigms of the 40s-60s (where hardware was specialized and general purpose computing was not particularly commonplace) are back in vogue. Also see [here](https://en.wikipedia.org/wiki/Hardware_acceleration#Hardware_acceleration_units_by_application).

In general, due to the high expense and low flexibility involved in producing ASICs, any hardware acceleration undertaken in science should leverage existing acceleration that is widely available in the general market first. If that is insufficient, FPGAs can be used, but custom ASIC production is well beyond the scope of most labs (as well as definitely out of budget). Chances are that CPUs and GPUs (which have mostly incorporated the innovations of physics ASICs at this point) are more than sufficient for most common tasks. FPGAs might only come into play for higher precision floats (octs are necessary in astrophysics) or universal numbers.

Also, see [IT Technology and Markets, Status and Evolution](https://indico.cern.ch/event/658060/contributions/2889027/attachments/1622791/2583013/tech_market_BPS_Mar2018_v9pptx.pdf) (26 March 2018) for more accelerators / trends.

-   [QCDSP and QCDOC](https://en.wikipedia.org/wiki/QCDOC) (photo [here](https://www.flickr.com/photos/brookhavenlab/3113601360); also see [here](https://web.archive.org/web/20181222005715/http://phys.columbia.edu/~cqft/)
-   [DSPs more broadly](https://www.hpcwire.com/2012/09/27/another_look_at_dsps_for_high_performance_computing/) (also see [here](https://en.wikipedia.org/wiki/Multidimensional_DSP_with_GPU_Acceleration)
-   [Anton](https://en.wikipedia.org/wiki/Anton_(computer))
-   [Intan](http://intantech.com/index.html) (used primarily for data acquisition; less about acceleration and more about miniaturization)
-   [Falcon Computing](https://www.falconcomputing.com/falcon-accelerated-genomics-pipeline/) (genomics)
-   [General reading on hardware acceleration](http://arcade.cs.columbia.edu/accels-amasbt10.pdf)

Storage Acceleration
--------------------

-   [ZFS Hardware Acceleration via QAT](http://open-zfs.org/wiki/ZFS_Hardware_Acceleration_with_QAT)

AI Acceleration
---------------

-   [Graphcore](https://www.graphcore.ai/)
-   [Google's TPU](https://cloud.google.com/tpu/)
-   [Nervana](https://www.intel.ai/nervana-nnp/)

Database Acceleration
---------------------

-   [CMU Database Acceleration Seminars](https://db.cs.cmu.edu/seminar2018/)
-   <https://news.ycombinator.com/item?id=18937101>

### ASICs

-   [Swarm64](https://www.swarm64.com/)
-   [Oracle's "Software in Silicon"](http://storageconference.us/2017/Presentations/Phillips.pdf)
-   [Q100](http://arcade.cs.columbia.edu/q100-asplos14.pdf) and [DB Mesh](http://arcade.cs.columbia.edu/dbmesh-damon17.pdf) ( see [here](http://arcade.cs.columbia.edu/netsyn-dac17.pdf) and [here](http://arcade.cs.columbia.edu/q100-ieeemicro15.pdf) too)

### Via GPUS

-   [PGStrom](http://on-demand.gputechconf.com/gtc/2015/presentation/S5276-Kohei-KaiGai.pdf)
-   [Alenka](https://github.com/antonmks/Alenka)
-   [BlazingSQL](https://blazingsql.com/)
-   <https://www.reddit.com/r/hardware/comments/9ld5df/in_a_parallel_universe_data_warehouses_run_on_gpus/>

Network Acceleration
--------------------

-   [SmartNICs and eBPF offloading](https://netdevconf.org/1.2/slides/oct7/10_nic_viljoen_eBPF_Offload_to_Hardware__cls_bpf_and_XDP_finalised.pdf) (see [here](https://www.netronome.com/blog/ever-deeper-bpf-update-hardware-offload-support/) and [here](https://netdevconf.org/1.2/slides/oct7/10_nic_viljoen_eBPF_Offload_to_Hardware__cls_bpf_and_XDP_finalised.pdf) too).

* * * * *

> [ScientificComputing](../ScientificComputing)
