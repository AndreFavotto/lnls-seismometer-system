"""
    This file triggers the first script which starts the system
"""
import sys, os, traceback as _traceback
from rawFileMonitor import rawFileMonitor
         
try:
    fileMonitor = rawFileMonitor()
    fileMonitor.start()
except Exception:
    _traceback.print_exc(file=sys.stdout)
    os._exit(0)