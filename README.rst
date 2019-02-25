jwstinfo
========

``jwstinfo`` is a small Python module and command line tool that provides a
simple summary of JWST data files. It is intended to be a lightweight tool that
does not require the JWST pipeline or data models.

To use the command line tool, simply run the ``jwstinfo`` command:

::

   $ jwstinfo /path/to/jwst/data.fits

An example summary will look something like the following:

::

   original filename : jw10001001001_01101_00001_mirifushort_s3d.fits
   file creation date: 2018-11-13T14:33:33.924
   pipeline version  : 0.12.2a.dev45+g91aabdd6
   instrument        : MIRI
   detector          : MIRIFUSHORT
   model type        : IFUCubeModel
   target name       : NGC 104
   observation id    : M103-Q3-SHORT-6020222141


Installation
------------

Stable releases of the package are registered `at PyPi
<https://pypi.python.org/pypi/jwstinfo>`__. The latest stable version can be
installed using ``pip``:

::

    $ pip install jwstinfo

The latest development version is available from the ``master`` branch
`on github <https://github.com/spacetelescope/jwstinfo>`__. To clone the project:

::

    $ git clone https://github.com/spacetelescope/jwstinfo

To install:

::

    $ cd jwstinfo
    $ pip install .

To install in `development
mode <https://packaging.python.org/tutorials/distributing-packages/#working-in-development-mode>`__::

    $ pip install -e .


Contributing
------------

We welcome feedback and contributions to the project. Contributions of
code, documentation, or general feedback are all appreciated. Please
follow the `contributing guidelines <CONTRIBUTING.md>`__ to submit an
issue or a pull request.

We strive to provide a welcoming community to all of our users by
abiding to the `Code of Conduct <CODE_OF_CONDUCT.md>`__.
