

Notes on Software Packaging
===========================

I'm using this page to keep notes on the wonderful world of software packaging / distribution.

Tools
-----

-   rpmbuild : Tool used to create RPMs, taking into account dependency resolution.
-   alien : Allows you to convert RPMs to Debian packages. Doesn't take into account dependencies.
-   [CPack](https://cmake.org/Wiki/CMake:Packaging_With_CPack) : Allows you to create multiple package formats from the same source code.
-   [Python's distutils](http://jeromebelleman.gitlab.io/posts/devops/setuppy/) can be used to create RPM packages. (see [here](https://docs.python.org/2.0/dist/creating-rpms.html) too)
-   [stdeb](https://pypi.org/project/stdeb/#authors) can also be used with distutils to create Debian packages (see [here](http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html) too).
-   [PyInstaller](https://www.pyinstaller.org/). See issue with wx [here](https://github.com/chriskiehl/Gooey/issues/259)

Spec file Formats
-----------------

-   dsc
-   RPM spec

Further Reading
---------------

-   [Env and Stacks/Projects/UserLevelPackageManagement - Fedora Project Wiki](https://fedoraproject.org/wiki/Env_and_Stacks/Projects/UserLevelPackageManagement)

* * * * *

> [Scientific-Computing](../Scientific-Computing) [Systems-Administration](../Systems-Administration)
