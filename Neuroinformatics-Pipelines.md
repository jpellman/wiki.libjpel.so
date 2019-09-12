\#format rst

Neuroinformatics Pipelines
==========================

A page to store links to documentation for common bits of software, and take notes on steps that overlap. I think that, by and large, the majority of neuroscience problems fall into three categories: image manipulation, quantifying behavioral observations, manipulating physiological observations, and stimulus presentation.

Image Manipulation
------------------

These utilities ultimately should amount to specialized versions of Photoshop/the GIMP that operate in 3D space rather than 2D. Some of them include some statistical processing tools as well. Essentially these then become hybridized versions of Photoshop and R/Stata/SPSS/SAS.

-   [RELION](https://hpc.nih.gov/apps/RELION/relion30_tutorial.pdf)
-   [SPM12](https://www.fil.ion.ucl.ac.uk/spm/doc/spm12_manual.pdf)
-   [AFNI](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/)
-   [ANTS](https://github.com/stnava/ANTsDoc/raw/master/ants2.pdf)
-   [BROCCOLI](https://github.com/wanderine/BROCCOLI/raw/master/documentation/broccoli.pdf)
-   [Brainstorm](https://neuroimage.usc.edu/brainstorm/)
-   [BrainVoyager](http://www.brainvoyager.com/bvqx/doc/UsersGuide/BrainVoyagerQXUsersGuide.html)
-   [ITK](https://itk.org/ItkSoftwareGuide.pdf)
-   [BEaST](http://rstudio-pubs-static.s3.amazonaws.com/8431_d05daa5d49aa4cada417b6afc8ffd295.html) (also [here](https://github.com/BIC-MNI/BEaST))
-   [Imaging Software Installed by the NIH](https://hpc.nih.gov/apps/#image)
-   [MNI Tools](https://www.mcgill.ca/bic/software/tools-data-analysis)

As per earlier statements, compare these manuals to:

-   [The GIMP](https://www.gimp.org/docs/)
-   [Adobe Photoshop](https://helpx.adobe.com/photoshop/user-guide.html)

### Other Image Processing Libraries

#### Open Source

-   [Ilastik](https://www.ilastik.org/)
-   [OpenCV](https://opencv.org/)
-   [scikitiimage](https://scikit-image.org/)
-   [vips](https://libvips.github.io/libvips/)
-   [Tomopy](https://tomopy.readthedocs.io/en/latest/)
-   [netpbm](http://netpbm.sourceforge.net/) (AFNI dependency)
-   [ImageMagick](https://imagemagick.org/)

#### Proprietary

-   [Huygens](https://svi.nl/HomePage)
-   [Amira and Avizo](https://www.thermofisher.com/us/en/home/industrial/electron-microscopy/electron-microscopy-instruments-workflow-solutions/3d-visualization-analysis-software.html)
-   [Aphelion](http://www.adcis.net/en/aphelion-lab/)
-   [Imaris](https://imaris.oxinst.com/)

### Additional Links

-   [An Inventory of Image Processing Algorithms](https://web.archive.org/web/20181220224256/http://www.efg2.com/Lab/Library/ImageProcessing/Algorithms.htm)
-   [Wikipedia's list of image processing algorithms](https://en.wikipedia.org/wiki/List_of_algorithms#Image_processing)

Quantifying Behavioral Data
---------------------------

-   [DeepLabCut](https://github.com/AlexEMG/DeepLabCut/wiki/DeepLabCut2.x-Quick-Guide-to-Commands)

### Sentiment Analysis

-   [TextBlob](https://textblob.readthedocs.io/en/dev/)
-   [CoreNLP](https://stanfordnlp.github.io/CoreNLP/index.html)
-   [NLTK](http://www.nltk.org/book/)

### Eye-Tracking

-   [PyGaze](http://www.pygaze.org/)
-   [WebGazer](https://webgazer.cs.brown.edu/)
-   [eyetrackingR](http://www.eyetracking-r.com/)
-   [saccades](https://github.com/tmalsburg/saccades)

Manipulating Physiological Data
-------------------------------

-   [Bioread](https://github.com/uwmadison-chm/bioread) (for BIOPAC)

Stimulus Presentation
---------------------

Stimulus presentation packages, by their very nature, also quantify behavioral data into reaction times and specific responses.

-   [DirectRT](http://www.empirisoft.com/directrt.aspx)
-   [ePrime](https://pstnet.com/products/e-prime/)
-   [PsychoPy](https://www.psychopy.org/)
-   [jsPsych](https://www.jspsych.org/)
-   [PsyScope](http://psy.ck.sissa.it/)

* * * * *

[ScientificComputing](../ScientificComputing)
