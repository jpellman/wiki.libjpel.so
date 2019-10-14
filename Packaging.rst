#format rst

Notes on Software Packaging
===========================

I'm using this page to keep notes on the wonderful world of software packaging / distribution.

.. contents:: :depth: 2

Tools
-----

* rpmbuild : Tool used to create RPMs, taking into account dependency resolution.

* alien : Allows you to convert RPMs to Debian packages.  Doesn't take into account dependencies.

* CPack_ : Allows you to create multiple package formats from the same source code.

* `Python's distutils`_ can be used to create RPM packages. (see here_ too)

* stdeb_ can also be used with distutils to create Debian packages (see `here <http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html>`__ too).

* PyInstaller_.  See issue with wx `here <https://github.com/chriskiehl/Gooey/issues/259>`__

Spec file Formats
-----------------

* dsc

* RPM spec

Further Reading
---------------

* `Env and Stacks/Projects/UserLevelPackageManagement - Fedora Project Wiki`_

-------------------------

 ScientificComputing_ SystemsAdministration_

.. ############################################################################

.. _CPack: https://cmake.org/Wiki/CMake:Packaging_With_CPack

.. _Python's distutils: http://jeromebelleman.gitlab.io/posts/devops/setuppy/

.. _here: https://docs.python.org/2.0/dist/creating-rpms.html

.. _stdeb: https://pypi.org/project/stdeb/#authors

.. _PyInstaller: https://www.pyinstaller.org/

.. _Env and Stacks/Projects/UserLevelPackageManagement - Fedora Project Wiki: https://fedoraproject.org/wiki/Env_and_Stacks/Projects/UserLevelPackageManagement

.. _ScientificComputing: ../ScientificComputing

.. _SystemsAdministration: ../SystemsAdministration

