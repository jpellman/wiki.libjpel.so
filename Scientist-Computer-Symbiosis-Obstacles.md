\#format rst

Top Challenges in Facilitating Man-Computer Symbiosis in 2019
=============================================================

In 1960, J.C.R. Licklider identified the following as the greatest obstacles in facilitating human / computer interaction (see [here](https://en.wikipedia.org/wiki/Man-Computer_Symbiosis)):

1.  A need for voice recognition.
2.  A need for GUIs (fulfilled at PARC) and tablet interfaces (fulfilled more recently with the smartphone revolution).
3.  A need for handwriting recognition- this need has become substantially less relevant, as most schoolchildren are taught to type in contemporary times (certainly not the case in my parents' generation), alternative Trie-based touch typing mechanisms are ubiquitous, and cursive is a dying art.
4.  Indelible memory.
5.  Some sort of workflow system (there was a passage where he anticipated Unix pipes).
6.  More elements I've forgotten.

Essentially, Licklider thought that man-computer symbiosis would look something like [this](https://www.youtube.com/watch?v=JIE8xk6Rl1w) (or [this full length version](https://www.youtube.com/watch?v=9bjve67p33E)).

Today, my completely ancedotal observation is that for human/computer symbiosis to be optimal, scientific researchers need:

1.  Consistent and intuitive packaging and reproducible environments. As an addendum, the need for consistent packaging has been a perennial issue in scientific computing- that's why Seth Vidal and Michael Stenner wrote [yum](https://en.wikipedia.org/wiki/Yum_(software)) and why [SBGrid](https://sbgrid.org/about/history/) was created.
2.  Scientific literature condensed into machine-parseable data that can be readily extracted (i.e., non-voice / handwriting related NLP). Methods and results sections need to be easy to aggregate and evaluate at a glance- the excessive verbosity of most publications is a hindrance to scientific progress. Metrics similar to those aggregated in [The secret lives of experiments](https://www.ncbi.nlm.nih.gov/pubmed/22796459) should be automatically generated constantly, without need for painstaking human intervention.
3.  Related to the above, there should be open datasets that are readily discoverable.
4.  Some sort of intuitive workflow system.
5.  Hardware-based accelerators (although this may be more of an optimization; see [ASICs](../ASICs)).

Of the above, I think that I personally can only contribute to the top 3, and that I should focus especially on packaging and environments / [DevOps](../DevOps) / [SciOps](../SciOps) in the immediate future. [Spack](https://spack.io/), [Nix](https://nixos.org/nix/) and [Ansible](https://www.ansible.com/) (or other config management systems) seem to be the best tools for this. I lean towards Spack and Ansible, since they seem to have the lowest barrier to entry conceptually / are more simple and elegant to maintain. The usage of DSLs should probably be discouraged absent any other additional advantages (I'm looking at you, Puppet, Cfengine, and nix).

Using NLP to enhance scholarship is a problem that ideally academic libraries should tackle via enhancements to their institutional repositories (or at least subscription services perhaps could work on this). It is possible (even likely) that scientists may delegate this responsibility to themselves, however (as occurred with arXiv). I see this as being of interest to me, but it should not occupy as much time as packaging.

I think that dataset discovery is also within the scope of libraries, although also it could be within the province of a data engineer. I'd be interested in continuing to work on this to some degree due to my past involvement with [BIDS](https://bids.neuroimaging.io/), although I think at most I would just do proof-of-concept stuff on my own time (e.g., embedding metadata within GZIP file headers).

A workflow system is definitely something a data engineer would work on, although I think that there's still some overlap with systems administration for this where I could become involved. Setting up a workflow manager would fall within the same realm as setting up a job scheduler such as SLURM. Working on [CWL wrappers](https://www.commonwl.org/) could be fun, and is arguably more in line with my primary goal of packaging/making reproducible environments.

I don't foresee working on hardware acceleration in any capacity beyond remaining aware of trends in industry and having enough knowledge to make informed choices / decipher a chip maker's propaganda accurately enough. Designing chips in FPGAs could be fun, although my call is that it's better to leave that sort of stuff to the professionals / electrical engineers / chemical engineers. Furthermore, I don't even know the field well enough to really know where I could best contribute- the only unimplemented logic I'm aware of that could potentially useful would be for some sort of [Unum](https://en.wikipedia.org/wiki/Unum_(number_format)) processing. Again, there are already professionals working on this at the various chip companies.

I address the above problems in more depth in the following pages:

1.  [Packaging](../Packaging)
2.  TODO - probable sub-page of [ComputationalLinguistics](../ComputationalLinguistics)
3.  TODO - probable sub-page of [OpenScience](../OpenScience)
4.  TODO - [CWLMake](../CWLMake) might be adapted for this.
5.  [ASICs](../ASICs)

* * * * *

> [ScientificComputing](../ScientificComputing)
