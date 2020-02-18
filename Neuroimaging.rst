#format rst

Summaries / Reviews from the Neuroimaging Literature
====================================================

.. contents:: :depth: 2

General
-------

* `Connectome Networks: From Cells to Systems`_ - offers a taxonomy for the scales of imaging.  At a glance (I haven't really read it yet as of 1/7/19), it looks like you could combine different factors at different levels of analysis as part of a useful nested hierarchical schema (e.g., microscale neurovascular coupling and microscale action potentials are components of macroscale fMRI and EEG readings).

* `Functional Brain Imaging: A Comprehensive Survey`_

* `A Comparative Analysis of Registration Tools: Traditional vs Deep Learning Approach on High Resolution Tissue Cleared Data`_

* `Performance of Image Registration Tools on High-Resolution 3D Brain Images`_

fMRI
----

Image Quality
~~~~~~~~~~~~~

* `On the Definition of Signal-To-Noise Ratio and Contrast-To-Noise Ratio for fMRI Data`_

* `Size and shape matter: The impact of voxel geometry on the identification of small nuclei`_

Task-related
~~~~~~~~~~~~

Resting State
~~~~~~~~~~~~~

* `Chao-Gan Yan's rsfMRI Course`_

Open/Shared Datasets
~~~~~~~~~~~~~~~~~~~~

* `Summary Table from Poldrack and Gorgolewski 2014`_

* Cimbi_

* EAS_

* `Harvard Aging Brain Study`_

* CamCAN_

* `UK Biobank`_

MR Physics
~~~~~~~~~~

* http://www.grahamwideman.com/gw/brain/orientation/orientterms.htm

General Courses
~~~~~~~~~~~~~~~

* `Chris Rorden's Course at GA Tech`_

* `Overview of Functional Magnetic Resonance Imaging`_

Stats on MR Usage
~~~~~~~~~~~~~~~~~

* https://jamanetwork.com/journals/jama/fullarticle/2674671

* https://jamanetwork.com/journals/jama/fullarticle/2720430

* https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2016/08/Provisional-Monthly-Diagnostic-Imaging-Dataset-Statistics-2017-05-18.pdf

File Formats
~~~~~~~~~~~~

* Just as an errant thought, the file format used to store most MRI images (NifTI) is very similar to DV, in the sense that each frame is its own distinct bitmap(?) image.  Unlike DV, no compression is applied to individual frames in NifTI (as far as I know).  Compression is usually accomplished by gzipping an entire raw NifTI file, but I doubt that this provides an optimal compression ratio- in MPEG compression schemes the previous frame informs what the next frame will look like (`motion compensation`_).  It seems like something similar could be used for 3d volumetric scans.  Why not encode each slice with a lossless video compression algo?

EEG
---

* `Spatial and temporal resolutions of EEG: Is it really black and white? A scalp current density view`_

MEG
---

fNIRS
-----

ISOI
----

* https://www.photometrics.com/wp-content/uploads/2019/10/Intrinsic-Signal-Optical-Imaging-AppNote.pdf

* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5466092/

* https://doi.org/10.1007/s00701-019-04132-8

* https://doi.org/10.1016/j.jneumeth.2004.02.025

* https://blog.arduino.cc/2015/11/16/a-low-cost-approach-to-intrinsic-optical-signal/

* `In Vivo Optical Imaging of Brain Function, 2nd edition`_

.. ############################################################################

.. _`Connectome Networks: From Cells to Systems`: https://www.ncbi.nlm.nih.gov/books/NBK435773/

.. _`Functional Brain Imaging: A Comprehensive Survey`: https://arxiv.org/pdf/1602.02225.pdf

.. _`A Comparative Analysis of Registration Tools: Traditional vs Deep Learning Approach on High Resolution Tissue Cleared Data`: https://arxiv.org/pdf/1810.08315.pdf

.. _Performance of Image Registration Tools on High-Resolution 3D Brain Images: https://arxiv.org/pdf/1807.04917.pdf

.. _On the Definition of Signal-To-Noise Ratio and Contrast-To-Noise Ratio for fMRI Data: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0077089

.. _`Size and shape matter: The impact of voxel geometry on the identification of small nuclei`: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0215382

.. _Chao-Gan Yan's rsfMRI Course: http://rfmri.org/Course

.. _Summary Table from Poldrack and Gorgolewski 2014: http://www.nature.com/neuro/journal/v17/n11/fig_tab/nn.3818_T1.html

.. _Cimbi: http://www.sciencedirect.com/science/article/pii/S1053811915003158

.. _EAS: http://www.einstein.yu.edu/departments/neurology/clinical-research-program/eas/data-sharing.aspx

.. _Harvard Aging Brain Study: http://nmr.mgh.harvard.edu/lab/harvardagingbrain

.. _CamCAN: https://camcan-archive.mrc-cbu.cam.ac.uk/dataaccess/

.. _UK Biobank: http://www.ukbiobank.ac.uk/imaging-data/

.. _Chris Rorden's Course at GA Tech: https://web.archive.org/web/20110816023612/http://www.cabiatl.com/CABI/resources/Course/

.. _Overview of Functional Magnetic Resonance Imaging: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3073717/

.. _motion compensation: https://en.wikipedia.org/wiki/Motion_compensation

.. _`Spatial and temporal resolutions of EEG: Is it really black and white? A scalp current density view`: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4548479

.. _In Vivo Optical Imaging of Brain Function, 2nd edition: https://www.ncbi.nlm.nih.gov/books/NBK20234/

