==========================
What's new in PyPy2.7 6.0+
==========================

.. this is a revision shortly after release-pypy-6.0.0
.. startrev: e50e11af23f1

.. branch: cppyy-packaging

Main items: vastly better template resolution and improved performance. In
detail: upgrade to backend 1.4, improved handling of templated methods and
functions (in particular automatic deduction of types), improved pythonization
interface, range of compatibility fixes for Python3, free functions now take
fast libffi path when possible, moves for strings (incl. from Python str),
easier/faster handling of std::vector by numpy, improved and faster object
identity preservation

.. branch: socket_default_timeout_blockingness

Make sure 'blocking-ness' of socket is set along with default timeout

.. branch: crypt_h

Include crypt.h for crypt() on Linux

.. branch: gc-more-logging

Log additional gc-minor and gc-collect-step info in the PYPYLOG

.. branch: reverse-debugger

The reverse-debugger branch has been merged.  For more information, see
https://bitbucket.org/pypy/revdb


.. branch: pyparser-improvements-3

Small refactorings in the Python parser.

.. branch: fix-readme-typo

.. branch: avoid_shell_injection_in_shutil

Backport CPython fix for possible shell injection issue in `distutils.spawn`,
https://bugs.python.org/issue34540

.. branch: cffi_dlopen_unicode

Enable use of unicode file names in `dlopen`

.. branch: rlock-in-rpython

Backport CPython fix for `thread.RLock` 
