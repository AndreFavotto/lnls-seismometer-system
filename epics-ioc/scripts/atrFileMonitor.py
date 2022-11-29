"""
    This script monitors the current folder for .atr files and send it to processing when found.
"""

import os, sys, traceback as _traceback
from processAtrFile import processAtrFile as pdf    

class atrFileMonitor():
    
    def __init__(self):
        super(atrFileMonitor, self).__init__()
        self.path_in = './'
                        
    def searchFiles(self):
        arquivos = set(os.listdir(self.path_in))
        return arquivos
                
    def run(self):
        try:
            content = self.searchFiles()
            for filename in content:
                if '.atr' in filename:
                    file = open(self.path_in + filename, 'r')
                    data = file.read()
                    file.close()
                    pdf.processFile(data, filename[-5])
                    os.remove(self.path_in + filename)        
        except Exception:
            _traceback.print_exc(file=sys.stdout)
            os._exit(0)