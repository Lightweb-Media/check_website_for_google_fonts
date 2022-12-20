# Check Websites for google Fonts.

```
python check_for_google_fonts.py example.csv output.csv
python check_for_google_fonts.py example.csv > output.txt
```

Read a CSV file and scan for Links to fonts.google

## Installation

```
git clone https://github.com/Lightweb-Media/check_website_for_google_fonts

cd check_website_for_google_fonts

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Usage
python check_for_google_fonts.py [domainlist] [outputfile]
### Example

```
python check_for_google_fonts.py example.csv output.csv
python check_for_google_fonts.py example.csv > output.txt
```

<domainlist> is a list of domains without protocol like example.org

To stripe out the protocol you can use 
https://www.clickminded.com/trim-urls-to-root-domain-standardise-urls-prefixes/
