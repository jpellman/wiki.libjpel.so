# Neuroscience Notes

## fMRI Methods Notes
 * Pitch (like baseball, lurch forward) - sagittal motion; Roll (roy --> king) - coronal motion; Yaw (aw --> axial) -- horizontal motion
	Elaboration: pitch - 'yes' nod (rotation around x-axis); roll - 'no' nod(rotation around z-axis); yaw - 'maybe' nod (rotation around y-axis)
 * Partial voluming - large voxel sizes bring together distinct elements, water down differences.  Small voxels --> higher noise.  Large voxels --> less granularity, ability to distinguish; Solution? Blur smaller voxels? Yes.

## PyMVPA Notes
 * samples - rows in a matrix (e.g., runs, session, participants); 1st axis/index in a 2D array
 * features - columns in a matrix (e.g., voxels); like regressors almost in GLM design matrix; 2nd axis/index in a 2D array
 * sample attributes - categories under which a sample can be binned

## SPM Notes 
 * Website documenting SPM data structures - http://www.its.caltech.edu/~nsulliva/spmdatastructure.htm
 * Andy's Brain Blog documentation of data structures - http://andysbrainblog.blogspot.com/2013/02/using-spmmat-to-stay-on-track-ii.html
 * Information on preprocessing:
   * http://www.ernohermans.com/wp-content/uploads/2011/11/spm8_startersguide.pdf 
   * http://www.fil.ion.ucl.ac.uk/~mgray/Presentations/Co-registration%20&%20Spaital%20Normalisation.ppt
 * *SPM.xY.P* is a character matrix for first-level analyses, a cell array for second level-analyses.	
