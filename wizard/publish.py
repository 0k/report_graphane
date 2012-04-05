# -*- coding: utf-8 -*-

import netsvc

from tools.translate import _
from osv import fields, osv

from ..xmlrpc import GraphaneXMLRPC
from ..ir_report import register_report


class report_graphane_publish_actions(osv.osv_memory):

    _name = "report.graphane_publish.actions"
    _description = "Graphane Publish Actions"

    _columns = {
    }

    _defaults = {
    }

    def do_action(self, cr, uid, _ids, context=None):

        ## XXXvlab: bad way to get the GraphaneParser instance of the action
        obj_model = context['active_model']
        reports = self.pool.get('ir.actions.report.xml')
        report_ids = reports.search(cr, uid,
                [('model', '=', obj_model),
                 ('report_type', '=', 'graphane')], context=context)

        assert report_ids, "There should be at least one graphane report "  \
               "on this object."

        report = reports.browse(cr, uid, report_ids[0], context=context)

        ## ensuring that the service is created !
        register_report(report.report_name, report.model, report.report_rml)
        ## This should be an instance of ReportGraphane

        service = netsvc.Service._services['report.%s' % report.report_name]
        ## XXXvlab: who calls this function
        new_context = context.copy()

        ## Removing any active_* keys, as they are active_id(s) and
        ## active_model will break the underlying searches
        for k in new_context.keys():
            if k.startswith("active_"):
                del new_context[k]

        for active_id in context['active_ids']:
            xml_content, _ = service.create_single_xml(
                cr, uid, [active_id], None,
                report, new_context,
                additional_data=report.graphane_publish_header)

            server = GraphaneXMLRPC(report.graphane_publish_xmlrpc_url)
            server.publish("input.xml", xml_content)

        return {'type': 'ir.actions.act_window_close'}


report_graphane_publish_actions()
