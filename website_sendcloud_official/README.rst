===================
SendCloud eCommerce
===================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

|badge1| |badge2|

This module is part of the SendCloud official connector for Odoo.

At the moment, the SendCloud official connector for Odoo consists of two modules: delivery_sendcloud_official and website_sendcloud_official.

1) delivery_sendcloud_official. This module works for the backend.
2) website_sendcloud_official. This module is for the frontend (webshop) and it depends on delivery_sendcloud_official.

Full documentation for developers is in https://docs.sendcloud.sc/.

**Table of contents**

.. contents::
   :local:

Usage
=====

Quickstart
~~~~~~~~~~

In short this is how the module works:
 - the customer selects some products in the online shop. The products are added in the shopping Cart
 - then the customer opens his shopping Cart and clicks on Process Checkout
 - the customer chooses one of the delivery method that SendCloud provides


Service Point Picker
~~~~~~~~~~~~~~~~~~~~

The module contains a link that opens the Service Point Picker (javascript) in the website shopping Cart.
The link is placed near the selected SendCloud Shipping Method. The link is visible in case:

 - the configuration in the SendCloud panel has the Service Point flag to True (in the SendCloud integration config)
 - the Shipping Method selected in the picking is provided by Sendcloud
 - the Shipping Method has field sendcloud_service_point_input == "required"
 - all the criteria (from country, to country, weight) match with the current order
 - the Shipping Method is set to "Published" in the website


Case of multiple shops
~~~~~~~~~~~~~~~~~~~~~~

TODO

Credits
=======

Authors
~~~~~~~

* Onestein
