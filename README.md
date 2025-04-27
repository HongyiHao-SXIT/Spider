# Python Web Crawler Learning Repository

## I. Introduction
This repository is created to assist you in systematically learning Python web crawlers. Whether you're a complete beginner or a developer with some programming foundation aiming to delve deeper into web crawling techniques, you'll find suitable learning resources and sample code here. We'll start from the basic syntax of Python and gradually guide you to master the core technologies of web crawling, including web page requests, data parsing, anti - crawling processing, and data storage.

## II. Learning Objectives
By studying the content in this repository, you'll be able to:
1. Master the basic syntax of Python to lay a solid foundation for web crawler development.
2. Understand the HTTP protocol and learn to use the `requests` library to send HTTP requests and obtain web page content.
3. Use libraries such as `BeautifulSoup` and `lxml` to parse HTML and XML documents and extract the required data.
4. Handle dynamic web pages and use `Selenium` to simulate browser operations.
5. Deal with common anti - crawling mechanisms, such as setting request headers, using proxy IPs, and controlling request frequencies.
6. Store the crawled data in files (e.g., CSV, JSON) or databases (e.g., MySQL, MongoDB).
7. Use the `Scrapy` framework to build efficient distributed web crawlers.

## III. Learning Path

### (I) Basic Introduction
1. **Python Basic Syntax**: Learn the basic data types, control structures, functions, classes, and other knowledge of Python. Refer to the code examples and comments in the `python_basics` folder.
2. **HTML and CSS Basics**: Understand the structure and styles of web pages and be able to read HTML tags and CSS selectors. You can refer to relevant front - end tutorials.

### (II) Web Crawler Basics
1. **HTTP Protocol**: Learn the principles of HTTP requests and responses, and master common request methods (GET, POST, etc.) and status codes. Read the documents in the `http_protocol` folder.
2. **`requests` Library**: Learn to use the `requests` library to send HTTP requests and obtain web page content. Refer to the code examples in the `requests_demo` folder.
3. **`BeautifulSoup` Library**: Master the basic usage of the `BeautifulSoup` library to parse HTML or XML documents and extract the required information. Check the sample code in the `beautifulsoup_demo` folder.
4. **Regular Expressions**: Learn the basic syntax of regular expressions to match and extract specific strings in text. Refer to the code and comments in the `regex_demo` folder.

### (III) Advanced Learning
1. **Dynamic Web Page Handling**: Use the `Selenium` library to simulate browser operations and handle web pages with content dynamically loaded by JavaScript. Refer to the examples in the `selenium_demo` folder.
2. **Data Storage**: Store the crawled data in files (e.g., CSV, JSON) or databases (e.g., MySQL, MongoDB). Check the code examples in the `data_storage` folder.
3. **Anti - Crawling Strategy Handling**: Understand common anti - crawling mechanisms and learn how to set request headers, use proxy IPs, and control request frequencies. Refer to the code and documents in the `anti_spider` folder.

### (IV) Advanced Applications
1. **`Scrapy` Framework**: Learn to use the `Scrapy` framework to build distributed web crawlers and improve crawling efficiency. Refer to the project examples in the `scrapy_project` folder.
2. **Asynchronous Web Crawlers**: Master the `aiohttp` library to implement asynchronous crawling and further improve the crawling speed. Check the code examples in the `asyncio_demo` folder.

## IV. Repository Structure
```
Spider/
├── python_basics/         # Python basic syntax examples
├── http_protocol/         # HTTP protocol - related documents
├── requests_demo/         # Examples of using the requests library
├── beautifulsoup_demo/    # Examples of using the BeautifulSoup library
├── regex_demo/            # Regular expression examples
├── selenium_demo/         # Examples of using the Selenium library
├── data_storage/          # Data storage examples
├── anti_spider/           # Anti - crawling strategy examples
├── scrapy_project/        # Scrapy framework project examples
├── asyncio_demo/          # Asynchronous web crawler examples
└── README.md              # This instruction document
```

## V. Environment Setup

### (I) Install Python
It is recommended to install Python 3.7 or a higher version. You can download the installation package from the [Python official website](https://www.python.org/downloads/) and install it.

### (II) Install Dependent Libraries
Use the `pip` command to install the required libraries:
```bash
pip install requests beautifulsoup4 lxml selenium scrapy aiohttp pymysql pymongo
```

### (III) Install Browser Drivers
If you use `Selenium`, you need to install the corresponding browser driver, such as ChromeDriver. You can download the driver that matches your Chrome browser version from the [ChromeDriver official website](https://sites.google.com/chromium.org/driver/) and add it to the system's environment variables.

## VI. Usage
1. Clone this repository to your local machine:
```bash
git clone https://github.com/HongyiHao-SXIT/Spider.git
```
2. Enter the corresponding folder and view the code examples and documents.
3. Follow the learning path to learn step by step and run the code examples for practice.

## VII. Contribution Guidelines
If you find errors in the code or have better implementation methods, welcome to submit a Pull Request. Before submitting, please ensure that your code complies with the PEP 8 coding specification and add necessary comments.

## VIII. Copyright Statement
The code and documents in this repository are for learning and reference purposes only. Do not use them for commercial purposes without authorization.

## IX. Contact Information
If you encounter problems or have any suggestions during the learning process, welcome to submit an Issue on GitHub or contact me at [your email address].

I hope this repository can help you learn Python web crawler technology smoothly! Happy learning! 