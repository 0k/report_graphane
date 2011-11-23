# -*- coding: utf-8 -*-

import subprocess
import os
import tempfile
import time

from mako.template import Template
from mako import exceptions
import netsvc
import pooler


#from report.report_sxw import *
import addons
import tools
from tools.translate import _
from osv.osv import except_osv

from report_xml import xml_report

from .xmlrpc import GraphaneXMLRPC


class GraphaneParser(xml_report.XmlParser):
    """Custom class that dump data to XML to send it to Graphane PDF generator
       Code partially taken from report webkit. Thanks guys :)
    """

    def __init__(self, name, table, rml=False, parser=False,
        header=True, store=False):
        super(GraphaneParser, self).__init__(name, table, rml,
                                        parser, header, store)

    def generate_pdf(self, comm_path, report_xml, header, footer, html_list):
        ## should return the raw data of a pdf
        return None

    # override needed to keep the attachments' storing procedure
    def create_single_pdf(self, cr, uid, ids, data, report_xml, context=None):
        """Override of inherited function to divert it and generate the XML
        instead of PDF if report_type is 'xml'."""

        if context is None:
            context={}

        if report_xml.report_type != 'graphane':
            return super(GraphaneParser,self).create_single_pdf(cr, uid, ids, data, report_xml, context=context)

        ## XXXvlab: who calls this function
        xml_content, _ =  self._create_full_dump_xml(cr, uid, ids, data, report_xml, context,
                                                     additional_data=report_xml.graphane_print_header)
        server = GraphaneXMLRPC(report_xml.graphane_print_xmlrpc_url)
        pdf_content = server.generate("input.xml", xml_content)

        return (pdf_content, 'pdf')

    def create(self, cursor, uid, ids, data, context=None):
        """We override the create function in order to handle generator
           Code taken from report webkit. Thanks guys :) """

        pool = pooler.get_pool(cursor.dbname)
        ir_obj = pool.get('ir.actions.report.xml')
        report_xml_ids = ir_obj.search(cursor, uid,
                [('report_name', '=', self.name[7:])], context=context)
        if report_xml_ids:
            report_xml = ir_obj.browse(
                                        cursor,
                                        uid,
                                        report_xml_ids[0],
                                        context=context
                                    )
            report_xml.report_rml = None
            report_xml.report_rml_content = None
            report_xml.report_sxw_content_data = None
        else:
            return super(GraphaneParser, self).create(cursor, uid, ids, data, context)
        if report_xml.report_type != 'graphane' :
            return super(GraphaneParser, self).create(cursor, uid, ids, data, context)
        result = self.create_source_pdf(cursor, uid, ids, data, report_xml, context)
        if not result:
            return (False,False)
        return result
