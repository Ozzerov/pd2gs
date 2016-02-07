pd2gs
===========
[![License](https://img.shields.io/pypi/l/pd2gs.svg)](https://pypi.python.org/pypi/pd2gs/)
[![PyPI version](https://badge.fury.io/py/pd2gs.svg)](https://pypi.python.org/pypi/pd2gs)


pd2gs — Simple tool to export pandas dataframes to google sheets.


Installation
--------
Simply install with pip:  <br>
    <code> $ pip install pd2gs </code>
    
Preparation (get credentials)
--------
This package uses Google Drive API so you need to authenticate yourself via Google:  
1.  Go to Google Console (you should have an acoount) and create a project (or use existing one)  
2.  Enable Google Drive API in API Manager  
3.  Go to Credentials (API Manager) and select New Credentials > Service Account Key  
4.  After creating Service Account Key you download your credentials.json  

Usage
--------
This package is very simple:  
1.  You create your Google Sheet in Google drive and copy its <a href="http://take.ms/JP5iC">Spreadsheet Id</a>
2.  Upload your pandas DataFrame to Google Sheets via ConnectGoogleSheet.write()

Code Example
--------
<code>
import pandas as pd    
from pd2gs.pd2gs import ConnectGoogleSheet    

df = pd.read_csv(path + 'df.csv')       
sh = ConnectGoogleSheet('path/credentials.json', 'spreadsheet_id')  
sh.write(df, 'new_sheet_name')  
</code>
