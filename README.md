# Data Wrangler Script

## Introduction
This is a simple script for generating daily and monthy gas prices from Henry Hub gas prices

## Data source
[Henry Hub gas prices](http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm)

## Table of Contents
1. <a href="#tech-stack-used">Tech Stack Used</a>
2. <a href="#dependencies">Dependencies</a>
3. <a href="#how-to-use">How To Use</a>
4. <a href="#author">Author</a>
5. <a href="#license">License</a>


## Tech Stack Used
- [Python3](https://www.python.org/downloads/)

## Dependencies
- [requests](https://requests.readthedocs.io/en/master/)
- [html5lib](https://pypi.org/project/html5lib/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/julietezekwe/data-wrangler.git

# Go into the repository
$ cd data-wrangler

# Install dependencies
$ pip3 install beautifulsoup4
$ pip3 install html5lib
$ pip3 install requests

# Run the script
$ python3 lib/gas_prices.py
```

## Author

Chidimma Juliet Ezekwe

## License

ISC

---
