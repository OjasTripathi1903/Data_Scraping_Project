import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
from extractor import excel_inserter


def scrape_website(url, symbol):
    # Set up headless Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome(
        options=chrome_options,
    )  # No need for executable_path if ChromeDriver is in your system's PATH

    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load (you might need to adjust the sleep duration)
    driver.implicitly_wait(10)  # Waits for 10 seconds

    # Get the HTML content after the JavaScript has loaded
    html_content = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all <li> elements containing employee data
    li_elements = soup.find_all("li")

    # Extract and print the year and corresponding employee number
    for li_element in li_elements:
        strong_tag = li_element.find("strong")
        if strong_tag:  # Check if <strong> tag exists inside the <li> element
            # Extract the text before the <strong> tag
            text_before_strong = strong_tag.find_previous(text=True).strip()
            # Use regular expression to find the number in the extracted text
            year_match = re.search(r"\b\d+\b", text_before_strong)
            if year_match:
                year = year_match.group()  # Extract the matched number as the year
                employee_number = strong_tag.text.strip()
                output = {year: [employee_number]}
                index = [symbol]
                output = pd.DataFrame(output, index=index)
                excel_inserter(False, output, "Data.xlsx", year, "row")

    # Close the browser
    driver.quit()


def main():
    url = "https://www.macrotrends.net/stocks/charts/AAPL/apple/number-of-employees"
    scrape_website(url, "AAPL")


if __name__ == "__main__":
    main()
