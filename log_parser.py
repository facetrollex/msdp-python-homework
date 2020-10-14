import argparse
import os.path
from os import path
import re

parser = argparse.ArgumentParser(description='Logs parser')
parser.add_argument("logPath", type=str, help="Path to apache log file")
args = parser.parse_args()

ipsDict = {}
if (path.exists(args.logPath)):
    f = open(args.logPath, "r")
    for line in f:
        reObject = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
        if reObject:
            ipAddress = reObject.group()
            ipsDict[ipAddress] = ipsDict.get(ipAddress)+1 if ipsDict.get(ipAddress) else 1
    if ipsDict:
        sortedIps = sorted(ipsDict.items(), key=lambda x: x[1], reverse=True)
        firstTenIps = sortedIps[:10]
        for i in firstTenIps:
	        print(i[0], i[1])
else:
    print(args.logPath + " does not exist")
