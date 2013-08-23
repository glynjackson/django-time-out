Django Time Out
============

A reusable Django that allows you to put your Django site into maintenance mode.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-time-out

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://git.com:sparky300/django-time-out.git#egg=time_out

TODO: Describe further installation steps (edit / remove the examples below):

Add ``time_out`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'time_out',
    )

Add the ``time_out`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^app-url/', include('time_out.urls')),
    )

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate time_out


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-time-out
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
