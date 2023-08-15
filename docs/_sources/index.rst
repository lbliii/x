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


.. .. automodule:: determined.core
..    :members: init



.. toctree::
   :glob:
   :hidden:
   :maxdepth: 5
   

   ./latest/*/_index



.. Analysis
.. ==========

.. Observations
.. -------------

.. 1. The code needed for autodocs mostly lives in ``/harness/determined``.


.. Pros 
.. ----
.. - Autodoc 
.. - Crosslinking

.. Cons 
.. ----
.. 1. Initial setup is hard because building docs also requires building Determined
   <TODO: document steps on fresh install>
.. 2. TOC/directory has to be manually curated using toctree statements on every parent article unless you are okay with the default glob organization. Weights aren't allowed.
   workaround: number the sections.

.. Migration Challenges
.. ----
.. 1. There isn't a direct replacement for **crosslinking** or **autodocs**. 

