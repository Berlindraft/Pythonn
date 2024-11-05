import re
import requests
from bs4 import BeautifulSoup


# Function to extract emails from a given URL
def get_emails_from_url(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Convert the parsed content to a string
    page_text = soup.get_text()

    # Regex pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find all email addresses in the page text
    emails = re.findall(email_pattern, page_text)

    # Remove duplicates by converting the list to a set
    return list(set(emails))


# Example usage
url = 'https://example.com'  # Replace with the target URL
emails = get_emails_from_url(url)

print("Found emails:", emails)
