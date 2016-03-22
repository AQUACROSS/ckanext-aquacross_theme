# ckanext-aquacross_theme

CKAN extension
============

CKAN extension for the AQUACROSS Information Portal as part of the `AQUACROSS Project <http://aquacross.eu>`_ 

Dependencies::

     CKAN v2.5.1

Installation
============

1. Activate your CKAN virtual environment, for example::

     $. /usr/lib/ckan/default/bin/activate

2. Install the ckanext-aquacross_theme Python package into your virtual environment::

     $ pip install -e git+https://github.com/AQUACROSS/ckanext-aquacross_theme.git#egg=ckanext-aquacross_theme

3. Activate aquacross_theme extension in the .ini file, for example:: 

     /etc/ckan/default/development.ini

     ckan.plugins = aquacross_theme

4. Restart Apache::

     $ /etc/init.d/apache2 restart

Community
=========

This extension is currently developed by:

     * `The Intergovernmental Oceanographic Commission of UNESCO (IOC-UNESCO) <http://www.unesco.org/new/en/natural-sciences/ioc-oceans/>`_

     * `University College Cork, National University of Ireland (UCC) <http://www.ucc.ie/en/>`_

     * `BC3 Basque Centre for Climate Change (BC3) <http://www.bc3research.org>`_

     * `The Royal Belgian Institute of Natural Sciences (RBINS) <https://www.naturalsciences.be/>`_

     * `Belgium and the Leibniz Institute of Freshwater Ecology and Inland Fisheries (FVB-IGB) <http://www.igb-berlin.de/igb_homepage.html>`_

AQUACROSS has received funding from the European Union’s Horizon 2020 Programme for Research, Technological Development and Demonstration under Grant Agreement no. 642317.
