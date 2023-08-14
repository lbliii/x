.. project-x documentation master file, created by
   sphinx-quickstart on Mon Aug 14 12:02:51 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to project-x's documentation!
=====================================

.. toctree::
   :maxdepth: 3
   :caption: Contents:



Indices
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. toctree::
   :glob:

   tutorials/**



The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.