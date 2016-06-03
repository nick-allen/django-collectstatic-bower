==========================
django-collectstatic-bower
==========================

Django static file finder that automatically runs bower install and collects components when running Django's collectstatic

Respects .bowerrc directory config when collecting files

Tested on python 2.7 and 3.5

Install
------------------

Pip install package

``pip install django-collectstatic-bower``

Add to ``STATICFILE_FINDERS``::

    STATICFILE_FINDERS = (
      ...
      'django_collectstatic_bower.staticfiles.finders.BowerComponentFinder',
    )
 
That's it, just collectstatic files like normal

``./manage.py collectstatic``
