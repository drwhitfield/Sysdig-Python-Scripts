
__author__    = 'Donald Whitfield'
__copyright__ = 'Johnson Controls International'
__email__     = 'donald.r.whitfield@jci.com'
__satus__     = 'Development Version'

'''
One of the Qolsys K8s clusters
Does not have a name entry in the
Field. Look into whether this was 
Due to bad onboarding or misconfig
'''

import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None, "display.max_columns", None) 
pd.set_option('display.width', None, 'display.max_colwidth', None)

sysdig_vuln_report = pd.read_csv('severe-vulnerabilities-2022-05-17.csv')
#sysdig_vuln_report.head()
#sysdig_vuln_report.groupby(["Image name", "Vulnerability ID"])["Severity"].count()
#df = sysdig_vuln_report.groupby(["Cluster Name", "Vulnerability ID"])["Severity"].value_counts().sort_values(ascending=False)

df = pd.DataFrame(sysdig_vuln_report.groupby(["Cluster Name", "Image name", "Image ID", "Vulnerability ID"])["Severity"].value_counts().sort_values(ascending=False))
print(df)

df.to_csv('SummarizedSysDigReport.csv')