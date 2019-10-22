#format rst

List of Neuroinformatics Tools w/ GPU-based Implementations
===========================================================

* `General Page on Medical Imaging Using Nvidia GPUs`_

* `ITK page on GPU Acceleration`_ (possibly useful for making ANTS go faster)

* `recon-all and mrisurf (Freesurfer)`_ (paper_).

* BROCCOLI_

* GLIRT_ (article_)

* `Another GPU-based implementation of FLIRT`_

* `GPU-Accelerated FLIRT and ANTS`_

* `FSL's bedpost-x`_

* CEREBRuM_

* `Google FFN`_ and here_

* CLIJ_ (an ImageJ plugin that maps macro calls to OpenCL calls)

* http://on-demand.gputechconf.com/gtc/2017/presentation/S7342-robert-zigon-data-mining-in%20neuroimagic-%20genomics.pdf

How exactly do GPUs work anyways?
---------------------------------

* `How a GPU Works`_ by Kayvon Fatahalian (`course website`_

* `GPGPU Lectures at Haifa LUG`_ by Ofer Rosenberg

* `Summary in the article about GPU-enabled FSL bedpost-x`_

* `CUDA Streams Best Practices`_

Discussions
-----------

AFNI
~~~~

* https://afni.nimh.nih.gov/afni/community/board/read.php?1,143063,143063

* https://afni.nimh.nih.gov/afni/community/board/read.php?1,71356,71365

* https://afni.nimh.nih.gov/afni/community/board/read.php?1,67402,73081

Exciting News for AFNI
::::::::::::::::::::::

* https://www.openmp.org/updates/openmp-accelerator-support-gpus/

* http://on-demand.gputechconf.com/gtc/2018/presentation/s8344-openmp-on-gpus-first-experiences-and-best-practices.pdf

ANTS
~~~~

* https://sourceforge.net/p/advants/discussion/840260/thread/260e1e38/

* https://sourceforge.net/p/advants/discussion/840260/thread/4b134259/

FSL
~~~

* http://godzilla.kennedykrieger.org/penguin/fsl.shtml

ImageJ
~~~~~~

* https://forum.image.sc/t/does-imagej-utilize-the-gpu/10333

Misc
~~~~

The case for consumer GPUs over enterprise GPUs:

* https://lambdalabs.com/blog/best-gpu-tensorflow-2080-ti-vs-v100-vs-titan-v-vs-1080-ti-benchmark/

* https://timdettmers.com/2019/04/03/which-gpu-for-deep-learning/

CryoEM
~~~~~~

* https://developer.download.nvidia.com/video/gputechconf/gtc/2019/presentation/s9664-how-to-scale-from-workstation-through-cloud-to-hpc-in-cryo-em-processing.pdf

* http://on-demand.gputechconf.com/gtc/2017/presentation/s7232-lance-wilson-processing-the-next.pdf

-------------------------



ScientificComputing_

.. ############################################################################

.. _General Page on Medical Imaging Using Nvidia GPUs: http://www.nvidia.com/object/medical_imaging.html

.. _ITK page on GPU Acceleration: https://itk.org/Wiki/ITK/Release_4/GPU_Acceleration

.. _recon-all and mrisurf (Freesurfer): https://surfer.nmr.mgh.harvard.edu/fswiki/CUDADevelopersGuide

.. _paper: http://www.ncbi.nlm.nih.gov/pubmed/24430512

.. _BROCCOLI: https://github.com/wanderine/BROCCOLI

.. _GLIRT: https://github.com/sfchen/GPU-Image-Registration

.. _article: http://ieeexplore.ieee.org/document/5405778/?reload=true

.. _Another GPU-based implementation of FLIRT: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0136718

.. _GPU-Accelerated FLIRT and ANTS: https://figshare.com/articles/GPU_accelerated_FLIRT_AND_ANTs/1501449

.. _FSL's bedpost-x: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061892

.. _CEREBRuM: https://arxiv.org/abs/1909.05085

.. _Google FFN: https://arxiv.org/abs/1611.00421

.. _here: https://github.com/google/ffn

.. _CLIJ: https://clij.github.io/clij-docs/

.. _How a GPU Works: https://www.cs.cmu.edu/afs/cs/academic/class/15462-f11/www/lec_slides/lec19.pdf

.. _course website: https://www.cs.cmu.edu/afs/cs/academic/class/15462-f11/www/

.. _GPGPU Lectures at Haifa LUG: http://haifux.org/lectures/267/

.. _Summary in the article about GPU-enabled FSL bedpost-x: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0061892#s2

.. _CUDA Streams Best Practices: http://on-demand.gputechconf.com/gtc/2014/presentations/S4158-cuda-streams-best-practices-common-pitfalls.pdf

.. _ScientificComputing: ../ScientificComputing

