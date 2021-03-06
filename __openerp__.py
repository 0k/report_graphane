# -*- coding: utf-8 -*-

{
    "name" : "Graphane Report Engine",
    "description" : """This module adds a new Report Engine to use GRAPHANE as
backend.  The module structure and some code is inspired by the report_webkit
module.
""",
    "version" : "%%short-version%%",
    "depends" : ["base", "report_xml"],
    "author" : "Valentin LAB -- Simplee",
    "category": "Reports/Pdf",
    "url": "http://www.simplee.fr",
    "data": ["security/ir.model.access.csv",
             "wizard/publish.xml",
             "ir_report_view.xml",
    ],
    "installable" : True,
    "active" : False,
}
