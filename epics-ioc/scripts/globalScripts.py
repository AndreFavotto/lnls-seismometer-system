"""
    This script is for functions that all scripts may use
"""

import argparse

class globalScripts:

    @staticmethod
    def getArgs():
        parser = argparse.ArgumentParser(description='Define environment variables')
        parser.add_argument('-p', required=True, help="Path to DAS-130 files")
        parser.add_argument('-P', required=True, help="Seismometer's PV prefix")
        parser.add_argument('-i', required=True, help="Unit ID (e.g.: B67D)")
        parser.add_argument('-s', required=True, help="Unit's data stream to hear data")
        args = parser.parse_args()
        return args