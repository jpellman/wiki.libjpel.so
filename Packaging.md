

Notes on Software Packaging
===========================

I'm using this page to keep notes on the wonderful world of software packagin distribution.

Tools
-----

-   rpmbuild : Tool used to create RPMs, taking into account dependency resolution.
-   alien : Allows you to convert RPMs to Debian packages. Doesn't take into account dependencies.
-   [CPack](http/cmake.oWiCMake:Packaging_With_CPack) : Allows you to create multiple package formats from the same source code.
-   [Python's distutils](htt/jeromebelleman.gitlab.posdevosetup) can be used to create RPM packages. (see [here](http/docs.python.o2dicreating-rpms.html) too)
-   [stdeb](http/pypi.oprojestd#authors) can also be used with distutils to create Debian packages (see [here](htt/shallowsky.cblprogrammipython-debian-packages-w-stdeb.html) too).
-   [PyInstaller](http/www.pyinstaller.o). See issue with wx [here](http/github.cchriskieGooissu259)

Spec file Formats
-----------------

-   dsc
-   RPM spec

Further Reading
---------------

-   [Env and StacProjecUserLevelPackageManagement - Fedora Project Wiki](http/fedoraproject.owiEnv_and_StacProjecUserLevelPackageManagement)

* * * * *

> [Scientific-Computing](Scientific-Computing) [Systems-Administration](Systems-Administration)
