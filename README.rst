README
--------

Flexible invocation
*******************

The application can be run right from the source directory, in two different
ways:

1) Treating the **ks** directory as a package **and** as the main script::

    $ python -m ks -h
    Usage: ks.py [OPTIONS] COMMAND [ARGS]...

    Mini Kickstarter command line tool.

    Options:
      -h, --help  Show this message and exit.

    Commands:
      back     Backs a project
      backer   List projects a backer has backed
      list     List backers of a project
      project  Creates a project

2) Using the **ks-runner.py** wrapper::

    $ ./ks-runner.py -h
    Usage: ks.py [OPTIONS] COMMAND [ARGS]...

    Mini Kickstarter command line tool.

    Options:
      -h, --help  Show this message and exit.

    Commands:
      back     Backs a project
      backer   List projects a backer has backed
      list     List backers of a project
      project  Creates a project


Installation sets up ks command
**************************************

First off, if you don't have pip or virtualenv installed (you can check with ``pip list``)::

    $ sudo easy_install pip
    $ pip install virtualenv

Installation right from the source tree into virtualenv for testing::

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -e .

Now, the ``ks`` command is available::

    $ ks -h 
    Usage: ks.py [OPTIONS] COMMAND [ARGS]...

    Mini Kickstarter command line tool.

    Options:
      -h, --help  Show this message and exit.

    Commands:
      back     Backs a project
      backer   List projects a backer has backed
      list     List backers of a project
      project  Creates a project

Running tests
***********************

Run tests with nose::

    $ nosetests -v
    ks_tests.test_project ... ok
    ks_tests.test_back ... ok
    ks_tests.test_list ... ok
    ks_tests.test_backer ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 1.723s

    OK



