# livecoin

A webcrawler for cryptos using Scrapy.

This package get crypto currencies data from "https://www.livecoinwatch.com".

Input:

![img](screenshots/Screenshot_1.png)

Output:

![img](screenshots/Screenshot_2.png)

## Technologies

- Python
- Scrapy (web scraping python framework)

## Requirements

    - Python 3.x
    - Google Chrome
    - chromedriver

1. Clone this repository and move to root folder.

    git clone https://github.com/Gabriel-Nunes/livecoin.git

2. Download chromedriver on "https://chromedriver.chromium.org/downloads" accordingly to your local Chrome version.

3. Unzip chromedriver to project's root.

## Installation

Create a python environment:

    python3 -m venv venv

Activate the virtual environment and update pip:

    sourve venv/bin/activate
    
    pip install -r requirements.txt

## Running the crawler

On root directory run:

    scrapy crawl coin_selenium -o results.csv

Check your "results.csv".

