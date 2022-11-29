"""
    This script processes .atr data sent by atrFileMonitor.py and write processed data into PV.
"""
import iocSeismometer, os, time, sys, traceback as _traceback

class processAtrFile:

    @staticmethod
    def getValue(data):
        option, value = tuple(data.replace(' ','').split('='))
        return value
    
    @staticmethod
    def convertCounts(counts, bitWeight):
        volts = counts * bitWeight
        # Transduction factor: 800 V/(m/s) 
        speed = volts / 800
        return speed
    
    @staticmethod
    def processFile(data, canal):
        try:
            data = data.replace('$', '').split('\n')
            bitWeight = float(processAtrFile.getValue(data[6]))
            # Seismic Data
            for counts in data[10:(len(data)-1)]:
                value = processAtrFile.convertCounts(float(counts), bitWeight)
                iocSeismometer.driver.write('S-Mon', value)
                iocSeismometer.driver.write('Ch-Mon', canal)
                time.sleep(0.0028) #Compensating DAS sampling frequency (100hz divided by 3 generated files =~3ms per file)
        except Exception:
            _traceback.print_exc(file=sys.stdout)
            os._exit(0)