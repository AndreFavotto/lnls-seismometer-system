"""
    This script provides the EPICS ioc server
"""
import sys, os, traceback as _traceback
from pcaspy import Driver, SimpleServer
from pcaspy.tools import ServerThread
from globalScripts import globalScripts

prefix = f'{globalScripts.getArgs().P}'
pvdb   = {
    'S-Mon': {
        'unit' : 'm/s'
    },
    'Ch-Mon': {
        'type' : 'string'
    },
}

class ioc(Driver):
    def __init__(self):
        super(ioc, self).__init__()
        self.updatePVs()

    def write(self, reason, value):
        self.setParam(reason, value)
        self.updatePVs()
        return True

    def read(self, reason):
        value = self.getParam(reason)
        self.updatePVs()
        return value

try:
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    server_thread = ServerThread(server)
    server_thread.start()
    driver = ioc()

except Exception:
    _traceback.print_exc(file=sys.stdout)
    os._exit(0)