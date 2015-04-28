README
--------


Installation sets up ``ks`` command
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


Each subcommand has its own help::

    $ ks project -h 
    Usage: ks project [OPTIONS] PROJECTNAME TARGETAMOUNT

      Create a new project with a project name and a target dollar amount

    Options:
      -h, --help  Show this message and exit.



    $ ks back -h 
    Usage: ks back [OPTIONS] BACKERNAME PROJECTNAME CREDITCARD BACKERAMOUNT

      Back a project with a given backer name, the project to be backed, a
        credit card number and a backing dollar amount

    Options:
      -h, --help  Show this message and exit.



    $ ks list -h 
    Usage: ks list [OPTIONS] PROJECTNAME

      Display a project including backers and backed amounts

    Options:
      -h, --help  Show this message and exit.



    $ ks backer -h 
    Usage: ks backer [OPTIONS] BACKERNAME

      Display a list of projects that a backer has backed and the amounts backed

    Options:
      -h, --help  Show this message and exit.



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



