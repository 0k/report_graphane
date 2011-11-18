#!/usr/bin/env python


import sys
import os.path
import xmlrpclib


class XMLRPCException(Exception): pass


def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


class GraphaneXMLRPC(object):

    METHOD_SEND = "service.generate-document"

    def __init__(self, url):

        self.server = xmlrpclib.ServerProxy(url)

    def generate_from_file(self, filename):

        basename = os.path.basename(filename)
        content = file_get_contents(filename)

        self.generate(self, basename, content)

    def generate(self, filename, content):

        method = getattr(self.server, self.METHOD_SEND)

        ## Graphane XML-RPC method awaits a hash (key, arg association) which
        ## is generated from the ``dict`` python type by ``xmlrpclib``
        ans = method({
            'stream-name': filename,
            'stream-data': xmlrpclib.Binary(content)
            })

        if ans['result-code'] != 0:
            try:
                msg = ans['result-message'] % ans['result-message-vars']
            except:
                import pdb; pdb.set_trace()
            raise XMLRPCException("Send XML-RPC failed: %s (result-code: %s)"
                                  % (msg.split('\n')[0], ans['result-code']))

        return ans['document-data'].data
