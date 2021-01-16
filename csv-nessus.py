
import csv
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="file", action='store', required=True,
	help="CSV file to load in as in test.csv for example")
parser.add_argument("-s", "--severity", dest="severity", action='store', required=True,
	help="Search severity level of a default CSV export of nessus, using arguments Critical, High, Medium or Low to display rows. Please use corrrect case as this is how it's represented in the fields in the Nessus CSV Export")
	
args = parser.parse_args()

severity = args.severity
file = args.file


def loop():
	with open(file, 'r') as f:
		reader = csv.reader(f, delimiter=',')
		included_cols = [3, 4, 6, 7]
		for row in reader:
			for field in row:
				content = list(row[i] for i in included_cols)
				if field == severity:				
					print (content)				
					break
					return

loop()

	