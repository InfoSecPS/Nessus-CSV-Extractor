# Nessus-CSV-Extractor
A script that takes input of a default Nessus CSV output from a scan, and depending on the severity you search for, will pull all the rows for that severity. You can have a play with the columns that it pulls data from by editing the numbers in the `included_cols` variable. The default is pulling `Risk[3], Host[4], Port[6], Name[7]` from a default CSV export. The only failure point is potentially, if you start ticking and unticking boxes on the Nessus CSV export feature. 

`python3 csv-nessus.py -f input-file.csv -s Critical` 

This will pull out all the Critical findings from the CSV like below: 
```
['Critical', '192.168.1.254', '445', 'Mozilla Firefox < 84.0']
['Critical', '192.168.1.254', '445', 'Mozilla Firefox < 84.0']
['Critical', '192.168.1.47', '445', 'Adobe Flash Player Unsupported Version Detection']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
['Critical', '192.168.1.47', '445', 'Adobe Reader <= 2015.006.30498 / 2017.011.30143 / 2019.012.20035 Multiple Vulnerabilities (APSB19-41)']
['Critical', '192.168.1.47', '445', 'Adobe Reader <= 2015.006.30498 / 2017.011.30143 / 2019.012.20035 Multiple Vulnerabilities (APSB19-41)']
['Critical', '192.168.1.47', '445', 'Adobe Reader <= 2015.006.30498 / 2017.011.30143 / 2019.012.20035 Multiple Vulnerabilities (APSB19-41)']
```
## Usage
```
usage: csv-nessus.py [-h] -f FILE -s SEVERITY

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  CSV file to load in as in test.csv for example
  -s SEVERITY, --severity SEVERITY
                        Search severity level of a default CSV export of nessus, using arguments Critical, High, Medium or Low to display rows. Please use corrrect case as this is how it's represented in the
                        fields in the Nessus CSV Export
```
It's a pretty basic script that solved an issue for me on a time limited job, and the beauty of it is that you can grep and sort the output to search only unique IP addresses or issues by IP. Like this:
`python3 csv-nessus.py -f input-file.csv -s Critical | grep 192.168.1.63 | sort -u`

```
['Critical', '192.168.1.63', '445', 'Adobe Flash Player <= 32.0.0.371 (APSB20-30)']
['Critical', '192.168.1.63', '445', 'Adobe Flash Player Unsupported Version Detection']
['Critical', '192.168.1.63', '445', 'Adobe Photoshop < CS5 / CS5.1 Multiple Arbitrary Code Execution Vulnerabilities (APSB12-11)']
['Critical', '192.168.1.63', '445', 'Adobe Photoshop Unsupported Version Detection']
['Critical', '192.168.1.63', '445', 'KB4561600: Security update for Adobe Flash Player (June 2020)']
['Critical', '192.168.1.63', '445', 'KB4586781: Windows 10 Version 2004 November 2020 Security Update']
['Critical', '192.168.1.63', '445', 'Microsoft Office 365 Unsupported Channel Version Detection']
['Critical', '192.168.1.63', '445', 'MS16-120: Security Update for Microsoft Graphics Component (3192884)']
```
## Things to do
Sort out being able to write out to another CSV file. You can write out to a file using `> out.csv` but it includes the `[] ` & `'` chars. 
