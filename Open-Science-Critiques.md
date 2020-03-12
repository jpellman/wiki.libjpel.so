

Critiques of Open Science
=========================

Metadata
--------

“At the heart of science is an essential balance between two seemingly contradictory attitudes – an openness to new ideas, no matter how bizarre or counterintuitive, and the most ruthlessly skeptical scrutiny of all ideas, old and new. This is how deep truths are winnowed from deep nonsense.” –Carl Sagan

Open science is poised to become one of the most innovative paradigm shifts in science, facilitated in great part by the capacity to share directly via the internet, increases in the ability to store large datasets, and a recognition from scientists that reproducibility and the future re-interpretation of data in light of methodological advances is necessary for the scientific enterprise. Despite this, no human institution is entirely perfect, and I would like to examine some of the caveats of open science in a series of blog posts here. I approach open science with skepticism since, as pointed out by the above Carl Sagan quotation, science necessarily progresses through critical thinking. Nevertheless, do not take this skepticism as cynicism, and my critiques as indictments- my intention is to point out major shortcomings in open science so that they may be addressed by the open science community. Just as iron must be forged by a hammer, so must creativity be refined through blunt inquiry.

The first topic I would like to approach is that of metadata. As researchers gather data, there is a huge bevy of supplemental data that is not always recorded. When you are in a room with the object of your study, you are exposed to more input, more sensations than recorded data. Data is an abstraction, and real life experience while collecting data can provide much information that aids in its interpretation. In short, the researchers collecting data will always be in a privileged position when it comes to being able to understand what signal they captured, since they captured other signal that they did not package. This can pose a problem for those who try to interpret that data later.

Let us look to the [New York Times](http://bits.blogs.nytimes.com/2013/02/24/disruptions-google-flu-trends-shows-problems-of-big-data-without-context/?smid=pl-share&_r=0) (as well as [Simply Statistics](http://simplystatistics.org/2013/03/04/big-data-context-bad/), where I first encountered this article ) to make this more tangible. In this article, NYU students set up an experiment with sensors next to stairs to track when students used the aforementioned stairs the most. They gathered data, but they were not performing the experiment in a hands-on way. In the absence of crucial metadata from the security guards at NYU (i.e., that the elevator was broken), they came to erroneous conclusions. Data released to websites such as the [Open Science Framework](https://osf.io/) or [Dataverse](http://dataverse.org/) is no different; without any context, it is possible that a great many individuals will reuse the data in a way that makes no sense because they are missing crucial information.

Another example can be found in neuroimaging. In MRI studies, subjects oftentimes will fall asleep while in the scanner. This is a serious confound that can lead to spurious results in data: an analyst must ask whether or not activity is task-related or due to the subject nodding off because they found the video they were viewing particularly boring and were tired. The research tech performing the scan might be able to inform the analyst’s conclusions by letting them know that, yes indeed, that subject was not conscious.

One last observation: the philosopher of science [John A. Schuster](http://descartes-agonistes.com/) in [Chapter 10](http://descartes-agonistes.com/index.php?option=com_docman&task=doc_view&gid=27&tmpl=component&format=raw&Itemid=53) of one of his introductory textbooks to philosophy and history of science notes that there is a gap between theory and data, and that there must be a subjective point at which a researcher decides that a gap is too big or too small and accepts or rejects a theory accordingly. He then notes an interesting point about how theory informs the apparatus of data collection itself\*. In this way, there is an element of circularity in data collection. If the assumptions behind data collection are incorrect, then the data itself might be totally useless. Imagine the biologist who spends years collecting data with a specialized microscope, only to realize that the conceptual underpinnings of the microscope itself were false and her data is now uninterpretable. Alternatively, consider the scientist who shaped a data gathering program with his fundamentally flawed theory in mind from the beginning (in a way, this resembles the logical fallacy of begging the question). Simply opening up data to the outside world does not address these issues.

These issues might not be capable of ever being fully addressed. Nevertheless, I would suggest some partial solutions at least. For one, researchers could record metadata in a manner similar to commenting code in software development and then upload it in addition to their datasets. With respect to the other observation regarding the theory-loading of data gathering / experimental apparatuses, researchers could lay out their assumptions for data gathering or provide references detailing the assumptions of the apparatus that they are using. That way, if other scientists disagree with those assumptions they will know to use different data or gather their own and release it accordingly. Knowing a great many researchers and how strained they are for time and the need to publish, I see these as ideals that likely will never be fulfilled unless we are in a Star Trek-like utopian future. But it doesn’t hurt to dream.

-   Problem 3 of Roger Peng’s Simply Stats post above is conceptually similar to this theory-loading.

### Response by Bill Broderick

I see your point about how metadata is crucial for the analysis of scientific data, but I don’t see how it’s more of a problem for Open Science than for regular/closed Science. Good practice would have people recording all relevant data with their data regardless, since it is necessary for any analysis that makes sense and if the lab wants to return to the data later, to use it for another project or to try and replicate their results, they’ll still need that metadata. So metadata is a necessity, regardless of whether you’re planning to share your data or not.

I think this is actually an upside for Open Science. Problems like metadata, proper annotation and care of data, etc. are no more a problem for Open Science than regular Science, but making your data or methods open adds another layer of incentive. These, and version-control and commenting of code, are practices that people should be doing anyway; making their stuff open will hopefully encourage scientists to use them, since they know their colleagues, collaborators, and editors will have access to everything. This is very similar to the argument for why Open Science will help reduce fraud: if your data / methods are out in the open, then dishonesty will be discouraged, because it’s easier to detect.

Open Science may also help with the metadata issue because it will encourage scientists to develop consistent metadata, which will improve the quality of meta-analyses and probably regular analyses as well. Poldrack has Cognitive Atlas, which is an effort towards encouraging just that.

### Response to Bill Broderick

The main point that I was trying to make was that openness is necessary, but not sufficient for scientific practice to truly improve. In my experience, the publish or perish culture has made investigators much more apathetic and sloppy about good metadata keeping and good coding practices. The prevailing attitude among postdocs in my current lab is one of, “Why write good code when the publication record is all that ultimately matters?” Ideally, this would not be the case and I do believe that open science could improve this, but only in the presence of sufficient funding and cultural incentives.

Relatedly, a recent column in the Baltimore Sun makes similar points in much greater detail:

<http://www.baltimoresun.com/news/opinion/oped/bs-ed-science-crisis-20150725-story.html>

* * * * *

> [Open-Science](Open-Science)
