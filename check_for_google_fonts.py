#!/usr/bin/env python 
from bs4 import BeautifulSoup
import csv
import requests
import sys
import re

def scan_website(domain):
    errors = []
    try: 
                #check http because follow we can follow the redirect if https
                r = requests.get('http://' + domain, allow_redirects=True ,verify=False)
                if (r.status_code == 200):       
                    try:
                        soup = BeautifulSoup(r.content, "html.parser")
                        links = soup.findAll('link',{'href': re.compile(r'fonts.google')})
                        print (links)
                        findings =[]
                        result = []
                        for x in links:
                            findings.append(str(x))
                            result = {
                                'url' : domain,
                                'links' :  "|".join(findings)
                            }
                        #if (len(links) > 0):
                        
                        return result
                    except Exception as e:
                        print (e)
    except Exception as e:
        print (e)
            





if __name__ == "__main__":
    if len(sys.argv) > 2:
        results = []
        csv_file = sys.argv[1]
        with open(csv_file, 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='|')
            for row in reader:
                
                result = scan_website(row[0])
                print (result)
                if result:
                    print (result)
                    results.append(result)

    print (results)
    csv_output_file = sys.argv[2]   
    with open(csv_output_file, 'w') as csvfile:
            fieldnames = ['url', 'links']
            writer = csv.DictWriter(csvfile, fieldnames)
            for data in results:
        #          print (data)
                writer.writerow(data)

