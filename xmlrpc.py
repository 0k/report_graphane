# -*- coding: utf-8 -*-
"""Simple XML-RPC interface to Graphane.

Works for printing or publishing.

"""


import xmlrpclib


class XMLRPCException(Exception):
    pass


class GraphaneXMLRPC(object):

    METHOD_GENERATE = "service.generate-document"
    METHOD_SEND = "server.process-stream"

    def __init__(self, url):

        self.server = xmlrpclib.ServerProxy(url)

    def generate(self, filename, content):
        """Returns a 2-tuple containing the file raw content, and its extension

        Output is the result of the printing service of graphane depending of
        the content provided (usually a XML string).

        Example output: (<RAW BINARY PDF>, 'pdf')

        Please note that the ``filename`` argument provided might be used by
        graphane, but most of the time, it's not important.

        """

        method = getattr(self.server, self.METHOD_GENERATE)

        ## Graphane XML-RPC method awaits a hash (key, arg association) which
        ## is generated from the ``dict`` python type by ``xmlrpclib``
        ans = method({
            'stream-name': filename,
            'stream-data': xmlrpclib.Binary(content)
            })

        if ans['result-code'] != 0:
            try:
                msg = ans['result-message'] % ans['result-message-vars']
            except TypeError:
                raise XMLRPCException("Send XML-RPC failed (result-code: %s) "
                                      "and invalid result-message format:\n%r"
                                      % (ans['result-code'], ans))
            raise XMLRPCException("Send XML-RPC failed: %s (result-code: %s)"
                                  % (msg.split('\n')[0], ans['result-code']))

        sname = ans['document-name'].split('.')
        if len(sname) > 1:
            ext = sname[-1]
        else:
            ext = 'pdf'
        return ans['document-data'].data, ext

    def publish(self, filename, content):
        """Returns the XML-RPC lib answer of the graphane publishing service

        It'll call the publishing service of graphane with the filename and
        content provided.

        Usually the XML-RPC answer is some sort of acknoledgement. No important
        data has to be extracted from the answer.

        """

        method = getattr(self.server, self.METHOD_SEND)

        ## Graphane XML-RPC method awaits a hash (key, arg association) which
        ## is generated from the ``dict`` python type by ``xmlrpclib``
        ans = method({
            'stream-name': filename,
            'stream-data': xmlrpclib.Binary(content)
            })

        return ans
