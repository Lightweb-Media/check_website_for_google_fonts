#!/usr/bin/env python 
from bs4 import BeautifulSoup
import csv
import requests
import sys
import re

REGEX_FONT_DOMAINS = "(fonts.(google|gstatic))|fast.fonts"

def scan_website(domain):
    try: 
                #check http because follow we can follow the redirect if https
                r = requests.get('http://' + domain, allow_redirects=True)
                if (r.status_code == 200):
                    try:
                        soup = BeautifulSoup(r.content, "html.parser")

                        findings = []
                        links = soup.findAll('link',{'href': re.compile(REGEX_FONT_DOMAINS)})
                        for x in links:
                            findings.append(str(x))

                        if (len(findings) > 0):
                            result = {
                                'url' : domain,
                                'links' :  "|".join(findings)
                            }
                            return result
                    except Exception as e:
                        print (e)
    except Exception as e:
                print (e)




if __name__ == "__main__":
    if len(sys.argv) > 2:
        csv_file = sys.argv[1]
        with open(csv_file, 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='|')
            results = []
            for row in reader:
                
                result = scan_website(row[0])
                if result:
                    results.append(result)

        csv_output_file = sys.argv[2]   
        with open(csv_output_file, 'w') as csvfile:
                fieldnames = ['url', 'links']
                writer = csv.DictWriter(csvfile, fieldnames)
                for data in results:
                    writer.writerow(data)

