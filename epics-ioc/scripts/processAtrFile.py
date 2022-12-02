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
    def processFile(data1, data2, data3):
        try:
            data1 = data1.replace('$', '').split('\n')
            data2 = data2.replace('$', '').split('\n')
            data3 = data3.replace('$', '').split('\n')
            bitWeight1 = float(processAtrFile.getValue(data1[6]))
            bitWeight2 = float(processAtrFile.getValue(data2[6]))
            bitWeight3 = float(processAtrFile.getValue(data3[6]))
            startIndex=10
            endIndex= len(data1)-1 #all three files are the same size
            for index in range(startIndex,endIndex):
                counts1 = data1[index]
                counts2 = data2[index]
                counts3 = data3[index]
                value1 = processAtrFile.convertCounts(float(counts1), bitWeight1)
                value2 = processAtrFile.convertCounts(float(counts2), bitWeight2)
                value3 = processAtrFile.convertCounts(float(counts3), bitWeight3)
                iocSeismometer.driver.write('SZ-Mon', value1)
                iocSeismometer.driver.write('SX-Mon', value2)
                iocSeismometer.driver.write('SY-Mon', value3)
                iocSeismometer.driver.update()
                time.sleep(0.01) #Compensating DAS sampling frequency (100hz = 0.01s)
        except Exception:
            _traceback.print_exc(file=sys.stdout)
            os._exit(0)