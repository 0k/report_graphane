Graphane Report module for OpenERP
==================================

**Please consider as pre-Alpha software** ;)

This module provides a new report type in OpenERP_ which can:

  - print documents thanks to a `graphane server`_ printing service (which could
    create PDF, ODT, HTML, or any format you may dream of)

  - publish documents thanks to a `graphane server`_ publish service (which could
    print document directly on any printer, send mail, send files through SFTP, FTP, ...)

.. _graphane server: http://www.callidoc.com
.. _OpenERP: http://www.openerp.com/


Usage
=====

This module depends on report_xml_ module to generate XML dumps that are then sent to
the printing service or the publishing service of a graphane server.

Also, you'll need to have access (or install) a full `graphane server`_ to use this module.

.. _report_xml: https://github.com/simplee/report_xml
.. _graphane server: http://www.callidoc.com


Installation
============

Once the code downloaded, don't forget to run "./autogen.sh" which will
generate the correct version number.

This is an openerp module, working with OpenERP 6.0, 6.1 and greater. So please
install as any other openerp module.

Once installed, you can create reports (Customization > Low Level Object >
Actions > Reports) of ``Report Type`` "graphane", which should give you a new
"Graphane Print" tab and a "Graphane Publish" tab.

These tabs should help you configure the host and port of the graphane publish
service and graphane print service.


Maturity
========

While this code is in full production in real GED environment, the code and
interface is not finished and the release was done in intent to share what
we are working on.

**Please consider this code as pre-Alpha software**.

Any contribution, idea, comments are welcome.


Roadmap
=======

Towards 1.0.0:

  - Complete examples of templates and XML

  - Openerp security permissions.

  - Full translations.

  - provide or use a real UI widget to display previews.

  - write a doc on HOW TO install and use this code.

  - give some examples of URL and maybe a documentation on how to set up
    correctly graphane and report_graphane to work correctly together.
