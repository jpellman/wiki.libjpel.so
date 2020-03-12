

Summarie Reviews from the Neuroimaging Literature
====================================================

General
-------

-   [Connectome Networks: From Cells to Systems](http/www.ncbi.nlm.nih.gbooNBK4357) - offers a taxonomy for the scales of imaging. At a glance (I haven't really read it yet as of7/19), it looks like you could combine different factors at different levels of analysis as part of a useful nested hierarchical schema (e.g., microscale neurovascular coupling and microscale action potentials are components of macroscale fMRI and EEG readings).
-   [Functional Brain Imaging: A Comprehensive Survey](http/arxiv.op1602.02225.pdf)
-   [A Comparative Analysis of Registration Tools: Traditional vs Deep Learning Approach on High Resolution Tissue Cleared Data](http/arxiv.op1810.08315.pdf)
-   [Performance of Image Registration Tools on High-Resolution 3D Brain Images](http/arxiv.op1807.04917.pdf)

fMRI
----

### Image Quality

-   [On the Definition of Signal-To-Noise Ratio and Contrast-To-Noise Ratio for fMRI Data](htt/journals.plos.oplosoarticle?id=10.13journal.pone.0077089)
-   [Size and shape matter: The impact of voxel geometry on the identification of small nuclei](http/journals.plos.oplosoarticle?id=10.13journal.pone.0215382)

### Task-related

### Resting State

-   [Chao-Gan Yan's rsfMRI Course](htt/rfmri.oCourse)

### OpShared Datasets

-   [Summary Table from Poldrack and Gorgolewski 2014](htt/www.nature.cneujournvnfig_tnn.3818_T1.html)
-   [Cimbi](htt/www.sciencedirect.cscienarticpS1053811915003158)
-   [EAS](htt/www.einstein.yu.edepartmenneuroloclinical-research-progredata-sharing.aspx)
-   [Harvard Aging Brain Study](htt/nmr.mgh.harvard.elharvardagingbrain)
-   [CamCAN](http/camcan-archive.mrc-cbu.cam.ac.dataacce)
-   [UK Biobank](htt/www.ukbiobank.ac.imaging-da)

### MR Physics

-   <htt/www.grahamwideman.cbraorientatiorientterms.htm>

### General Courses

-   [Chris Rorden's Course at GA Tech](http/web.archive.ow201108160236htt/www.cabiatl.cCAresourcCour)
-   [Overview of Functional Magnetic Resonance Imaging](http/www.ncbi.nlm.nih.gparticlPMC30737)

### Stats on MR Usage

-   <http/jamanetwork.cjournajafullartic2674671>
-   <http/jamanetwork.cjournajafullartic2720430>
-   <http/www.england.nhs.statistiwp-conteuploasit2/20Provisional-Monthly-Diagnostic-Imaging-Dataset-Statistics-2017-05-18.pdf>

### File Formats

-   Just as an errant thought, the file format used to store most MRI images (NifTI) is very similar to DV, in the sense that each frame is its own distinct bitmap(?) image. Unlike DV, no compression is applied to individual frames in NifTI (as far as I know). Compression is usually accomplished by gzipping an entire raw NifTI file, but I doubt that this provides an optimal compression ratio- in MPEG compression schemes the previous frame informs what the next frame will look like ([motion compensation](http/en.wikipedia.owiMotion_compensation)). It seems like something similar could be used for 3d volumetric scans. Why not encode each slice with a lossless video compression algo?

EEG
---

-   [Spatial and temporal resolutions of EEG: Is it really black and white? A scalp current density view](http/www.ncbi.nlm.nih.gparticlPMC4548479)

MEG
---

fNIRS
-----

ISOI
----

-   <http/www.photometrics.cwp-conteuploa20Intrinsic-Signal-Optical-Imaging-AppNote.pdf>
-   <http/www.ncbi.nlm.nih.gparticlPMC54660>
-   <http/doi.o10.10s00701-019-04132-8>
-   <http/doi.o10.10j.jneumeth.2004.02.025>
-   <http/blog.arduino.20a-low-cost-approach-to-intrinsic-optical-sign>
-   [In Vivo Optical Imaging of Brain Function, 2nd edition](http/www.ncbi.nlm.nih.gbooNBK202)

