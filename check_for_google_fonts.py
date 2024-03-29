#!/usr/bin/env python 
from bs4 import BeautifulSoup
import csv
import requests
import sys
import re
from urllib.parse import urlparse

REGEX_FONT_DOMAINS = "(fonts.(google|gstatic))|fast.fonts"


def add_external_links(scheme, domain, links, findings):
    for x in links:
        # css
        if x.get('href'):
            link = x['href']
        # javascript
        elif x.get('src'):
            link = x['src']
        else:
            continue

        # get the full url
        if link.startswith('//'):
            link = scheme + ':' + link
        elif link.startswith('/'):
            link = scheme + '://' + domain + link

        # complain about any links to external files
        if link.startswith('http') and not link.startswith(scheme + '://' + domain + '/'):
            if not str(x) in findings:
                findings.append(str(x))

    return findings


def scan_website(domain):
    try: 
                #check http because follow we can follow the redirect if https
                r = requests.get('http://' + domain, allow_redirects=True)
                if (r.status_code == 200):
                    try:
                        parsed_uri = urlparse(r.url)
                        scheme = parsed_uri.scheme
                        domain = parsed_uri.netloc
                        soup = BeautifulSoup(r.content, "html.parser")

                        findings = []
                        links = soup.findAll('link',{'href': re.compile(REGEX_FONT_DOMAINS)})
                        for x in links:
                            findings.append(str(x))

                        csslinks = soup.findAll('link', {'type': 'text/css'})
                        findings = add_external_links(scheme, domain, csslinks, findings)
                        csslinks2 = soup.findAll('link', {'rel': 'stylesheet'})
                        findings = add_external_links(scheme, domain, csslinks2, findings)
                        jslinks = soup.findAll('script', {'src': re.compile('.*')})
                        findings = add_external_links(scheme, domain, jslinks, findings)

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
                
                if not row or row[0].startswith('#'):
                    continue
                result = scan_website(row[0])
                if result:
                    results.append(result)

        csv_output_file = sys.argv[2]   
        with open(csv_output_file, 'w') as csvfile:
                fieldnames = ['url', 'links']
                writer = csv.DictWriter(csvfile, fieldnames)
                for data in results:
                    writer.writerow(data)

