# Check Websites for google Fonts.
python check_for_google_fonts.py example.csv output.csv
Read a CSV file and scann for Links to fonts.google

##Installation

git clone https://github.com/Lightweb-Media/check_website_for_google_fonts
cd check_website_for_google_fonts
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

##Usage
python check_for_google_fonts.py <domainlist> <outputfile>
Example:
python check_for_google_fonts.py example.csv output.csv 

<domainlist> is a list of domains without protocol like example.org 
