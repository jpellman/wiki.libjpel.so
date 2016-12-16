\#format rst

Shell Scripting
===============

Using input-output redirection
------------------------------

-   A pipe redirects the output of one command to another command. The pipe was added to Unix in 1973 so that [CommandlineFu](http://commandlinefu.com/) would have a reason for existing. Jon Hendren would not become a Devops Thought Lord until 3 years later in 1976.
-   \> redirects the standard out of a command to a file or device. Standard output is represented by file descriptor 1; 1\> accomplishes the same thing as \>.
-   2\> redirects the standard error of a command to a file or device. Standard error is represented by file descriptor 2.
-   *fd\_1*\>&\*fd\_2\* redirects the output from an arbitrary file descriptor *fd\_1* to *fd\_2*
    -   2\>&1 redirects standard error to standard out
    -   1\>&2 redirects standard out to standard error
-   &\> redirects all file descriptors to a file or device.

### References / Further Reading

-   <http://wiki.bash-hackers.org/howto/redirection_tutorial>
-   <http://sebug.net/paper/os/linux/Linux%20Shell%20Scripting%20Tutorial%20v2.0.pdf>
-   <http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-3.html>
-   <http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html>

Using grep and regular expressions to analyze text
--------------------------------------------------

### grep

-   -F : returns lines with single occurrence of literal string (fgrep)
-   -x : returns only if *the entire line* is an exact match for literal string
-   -E : use extended regex (Perl style); no need for escapes to denote atoms (egrep)
-   -   -   returns lines with any number of consecutive repeats of search string

-   . - wildcard character

### Practice

-   [RegEx Golf](https://regex.alf.nu/)

### References / Further Reading

-   [Regular Expressions by Jan Goyvaerts](http://www.regular-expressions.info)

* * * * *

> [SystemsAdministration](../SystemsAdministration)
