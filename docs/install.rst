.. _install:


Installation guide
==================

Before installing ``django-project-portfolio``, you'll need to have a
copy of `Django <https://www.djangoproject.com>`_ already
installed. For information on obtaining and installing Django, consult
the `Django download page <https://www.djangoproject.com/download/>`_,
which offers convenient packaged downloads and installation
instructions.

The |version| release of ``django-project-portfolio`` supports Django
1.8 and 1.9, on any of Python version supported by those versions of
Django:

* Django 1.8 suports Python 2.7, 3.2, 3.3, 3.4 and 3.5.

* Django 1.9 supports Python 2.7, 3.4 and 3.5.

.. important:: **Python 3.2**

   Although Django 1.8 supports Python 3.2, and
   ``django-project-portfolio`` |version| supports it, many Python
   libraries supporting Python 3 impose a minimum requirement of
   Python 3.3 (due to conveniences added in Python 3.3 which make
   supporting Python 2 and 3 in the same codebase much simpler).

   As a result, use of Python 3.2 is discouraged; Django 1.9 has
   already dropped support for it, and a future release of
   ``django-project-portfolio`` will likely drop Python 3.2 support as
   well.


Normal installation
-------------------

The preferred method of installing ``django-project-portfolio`` is via
``pip``, the standard Python package-installation tool. If you don't
have ``pip``, instructions are available for `how to obtain and
install it <https://pip.pypa.io/en/latest/installing.html>`_.

Once you have ``pip``, simply type::

    pip install django-project-portfolio


Manual installation
-------------------

It's also possible to install ``django-project-portfolio``
manually. To do so, obtain the latest packaged version from `the
listing on the Python Package Index
<https://pypi.python.org/pypi/django-project-portfolio/>`_. Unpack the
``.tar.gz`` file, and run::

    python setup.py install

Once you've installed ``django-project-portfolio``, you can verify
successful installation by opening a Python interpreter and typing
``import projects``.

If the installation was successful, you'll simply get a fresh Python
prompt. If you instead see an ``ImportError``, check the configuration
of your install tools and your Python import path to ensure
``django-project-portfolio`` installed into a location Python can
import from.


Installing from a source checkout
---------------------------------

The development repository for ``django-project-portfolio`` is at
<https://github.com/ubernostrum/django-project-portfolio>. Presuming
you have `git <http://git-scm.com/>`_ installed, you can obtain a copy
of the repository by typing::

    git clone https://github.com/ubernostrum/django-project-portfolio.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``python setup.py install``.


Basic use
---------

You'll need to add ``django-project-portfolio`` to your Django-based
project; since this application makes use of a custom signal which
needs to be set up, it's done via `a Django AppConfig
<https://docs.djangoproject.com/en/1.8/ref/applications/#configuring-applications>`_
subclass. So rather than adding ``projects`` to your
``INSTALLED_APPS`` setting, instead add
``projects.apps.ProjectsConfig``, like so::

    INSTALLED_APPS = [
        # ... other apps here
       'projects.apps.ProjectsConfig',
    ]

Then run ``manage.py migrate`` to set up the required database tables,
and you can start adding instances of :ref:`the provided models
<models>` though the Django admin interface, and wiring up :ref:`the
provided views <views>` in your URLconf.

