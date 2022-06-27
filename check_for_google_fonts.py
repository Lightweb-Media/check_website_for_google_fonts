import requests
from bs4 import BeautifulSoup
import csv
import requests
import sys
import re
csv_file = sys.argv[1]
print(csv_file)
results = []
with open(csv_file, 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='|')
    for row in reader:
        #https://lightweb-media.de
        try: 
            r = requests.get('https://' + row[0] )
            if (r.status_code == 200):
                
                try:
                    soup = BeautifulSoup(r.content, "html.parser")
                    links = soup.findAll('link',{'href': re.compile(r'fonts.google')})
                    findings =[]
                    for x in links:
                        findings.append(str(x))
          
                    
                    if (len(links) > 0):
                        result = {
                            'url' : row[0],
                            'links' :  "|".join(findings)
                        }
                        results.append(result)
                      

                except Exception as e:
                    print (e)
        except Exception as e:
            print (e)
    

with open('result.csv', 'w') as csvfile:
        fieldnames = ['url', 'links']
        writer = csv.DictWriter(csvfile, fieldnames)
        for data in results:
            writer.writerow(data)



