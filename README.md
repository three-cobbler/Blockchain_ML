# Blockchain_ML

## Scrape data
  - scrapy package has been used for scraping [neurips schedule data](https://neurips.cc/Conferences/2019/Schedule)
  - created spider for scraping data
  - scraped data will be exposed in JSON format(`neruips_schedule.json` file will be generated)

### Usage
  - Use below command install scrapy package
  ```
  pip install scrapy
  ```
  - To scrape schedule data
  ```
  scrapy crawl neruips_schedule
  ```
