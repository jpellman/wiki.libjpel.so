

This will be a table mapping LONI Pipeline Engine XML tags to Common Workflow Language syntax.

| LONI XML Tag | Arguments/Attributes | Description | Equivalent Command Line Tool CWL Syntax |
| --- | --- | --- | --- |
| pipeline | | Tag used to declare pipeline | |
| | version | A version number for the pipeline. | cwlVersion |
| moduleGroup | | A collection of modules; can act as a single node in a workflow. | |
| module | | A single executable in a pipeline. | |
| | name | Name of the executable. | |
| | description | A description of the executable.| |
| | location | Path to the executable. | baseCommand |
| | package | Package the executable belongs to. | |
| | version | Version of the package the executable belongs to.| |
| | executableVersion | Version of the executable that the module wraps. | |
| executableAuthors | | Authors of the executable that the XML module definition wraps.| |
| author | | Author name.  Nested within ''executableAuthors'' and ''authors'' | |
| | fullName | Full name. | |
| | email| Author e-mail. | |
| | website | Author website. | |
| authors | | Authors of XML module definition for LONI Pipeline | |
| citations | | A grouping of multiple citation tags. | |
| citation | Unnamed string containing citation text. | Article citation. Nested within ''citations'' | |
| tag | | Tag used to identify the module using LONI Pipeline's search functionality. | |
| input/output | | An input or output parameter| inputs/outputs|
| | name | A name for the input parameter. | |
| | description | A description for the input parameter. | |
| | enabled | Whether or not a particular parameter is enabled for usage as part of the module. | |
| | required | Whether or not the input parameter is required for the module to execute.| |
| | order |  The order in which a parameter should appear on the command line (0-indexed). | |
| | switch | The switch used on the command line (e.g., ''-input'')| |
| | switchSpaced | Should there be a space between a switch and its arguments? | |
| format | | Defines the nature of the data accepted/produced by the parameter. | format |
| | type | Type of data produced/accepted by parameter.  Choose from the following options: **File**,**Directory**,**String** ,**Number**,**Enumerated**.  If you choose **File**, ''filetype'' must be defined within ''format''. | |
| | cardinality | How many arguments should be entered after the switch. -1 is infinite (unavailable for output) -2 is the number of arguments passed to the input (unavailable for input) | |
| | base | A base string to be transformed. | |
| filetypes | |  A grouping of file types accepted by the input/output.  | |
| filetype | | A file type accepted by the input/output. | |
| | name | The human readable name of the file type. | |
| | extension | The extension of the filetype (no ‘.’ required) | |
| | description | A short description of the file type | |
| need | | A nested element within the ''filetype'' tag that contains the extension of any file needed by this type.  You can have multiple ''need'' tags within a ''filetype''. | |
| transform | | Allows you to define an output file name using string operations and a base string. | |
| | order | An index value describing at which point the transform should be executed.(?) | |
| | op | **subtract**,**prepend**,**append**,**replace** | |

See:

<http://pipeline.bmap.ucla.edu/learn/xml-overview/>

<http://pipeline.bmap.ucla.edu/learn/glossary/>

