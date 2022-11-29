"""
    This script monitors the given path in [-p] for new raw data files, then convert it to .atr
"""

import os, sys,threading, shutil, datetime, traceback as _traceback
from atrFileMonitor import atrFileMonitor
from globalScripts import globalScripts

class rawFileMonitor(threading.Thread):
    
    def __init__(self):
        super(rawFileMonitor, self).__init__()
        self.kill = threading.Event()
        self.basePath = globalScripts().getArgs().p
        self.unitId = globalScripts().getArgs().i
        self.dataStream = globalScripts().getArgs().s
        self.pathIn = f'{self.basePath}/archive'
        self.pathCvt = f'{self.basePath}/pas2asc'
        self.atrFileMonitor = atrFileMonitor()
        
    def scanFiles(self):
        today = datetime.datetime.now()
        year = today.year
        dayOfYear = (today - datetime.datetime(year, 1, 1)).days + 1
        filesPath = f'{self.pathIn}/{year}{dayOfYear}/{self.unitId}/{self.dataStream}/'
        arquivos = set(os.listdir(filesPath))
        return (filesPath, arquivos)
    
    def cleanFiles(self):
        try: #delete last month's local files if not deleted yet
            lastMonth = datetime.datetime.now() - datetime.timedelta(days=30)
            lmYear = lastMonth.year
            lmDayOfYear = (lastMonth- datetime.datetime(lmYear, 1, 1)).days + 1
            oldPath = f'{self.pathIn}/{lmYear}{lmDayOfYear}'
            shutil.rmtree(oldPath)
        except FileNotFoundError:
            pass

    def convert(self, filesPath, newFiles):
        for file in newFiles:
            pathIn = filesPath + file
            if '_00000000' not in pathIn: # xxxxxxx_00000000: File is still processing
                os.system(self.pathCvt + ' -ln ' + pathIn + ' 1> /dev/null 2> /dev/null')
                os.remove(pathIn)
                self.atrFileMonitor.run()
        
    def run(self):
        try:
            filesPath, content = self.scanFiles()
            while not self.kill.is_set():
                self.cleanFiles()
                filesPath, newContent = self.scanFiles()
                newFiles = newContent.difference(content)
                # Converts data if new file found
                if newFiles:
                    self.convert(filesPath,newFiles)
                content = newContent
        except Exception:
            _traceback.print_exc(file=sys.stdout)
            os._exit(0)