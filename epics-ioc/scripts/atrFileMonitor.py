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
        return sorted(arquivos)
                
    def run(self):
        try:
            content = self.searchFiles()
            for filename in content:
                if '1.atr' in filename:
                    with open(self.path_in + filename, 'r') as file:
                        data1 = file.read()
                        os.remove(self.path_in + filename)
                elif '2.atr' in filename:
                    with open(self.path_in + filename, 'r') as file:
                        data2 = file.read()
                        os.remove(self.path_in + filename)
                elif '3.atr' in filename:
                    with open(self.path_in + filename, 'r') as file:
                        data3 = file.read()
                        os.remove(self.path_in + filename)
            pdf.processFile(data1, data2, data3) 
        except Exception:
            _traceback.print_exc(file=sys.stdout)
            os._exit(0)