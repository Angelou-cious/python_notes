"""
    Multi-line docstring that describes the purpose and functionality of this Python script
    
    This script is designed to:
    - Fetch the latest 5 spaceflight articles from the Spaceflight News API
    - Extract specific data fields from each article (title, news_site, published_date, url)
    - Process and format the publication dates to YYYY-MM-DD format
    - Display summary statistics about the fetched articles
    - Save the processed data to a CSV file for further analysis
"""

# Import the requests library for making HTTP API calls to external web services
import requests
# Import pandas library for data manipulation and CSV file operations
import pandas as pd

# Define the base URL for the Spaceflight News API version 4
base_url = "https://api.spaceflightnewsapi.net/v4/"

# Define the specific API endpoint for fetching articles from the news service
endpoint = "articles/"

# Define a function to make HTTP requests to the API with error handling
def main_request(base_url, endpoint, limit):
    # Start a try block to handle potential network or HTTP errors gracefully
    try:
        # Construct the full API URL by concatenating base_url, endpoint, and limit parameter
        response = requests.get(base_url + endpoint + f'?limit={limit}')
        # Check if the HTTP response status indicates success (raises exception if not 2xx)
        response.raise_for_status()
        # Parse the JSON response body and return it as a Python dictionary
        return response.json()
    # Catch any requests-related exceptions (network errors, timeouts, HTTP errors)
    except requests.RequestException as e:
        # Print the error message to inform the user about the failure
        print(e)
        # Return None to indicate that the request failed
        return None
    
# Define a function to extract and format date strings from the API response
def parse_date(date):
    # Start a try block to handle potential date parsing errors
    try:
        # Extract the first 10 characters (YYYY-MM-DD) from the date string, or return None if date is empty
        return date[:10] if date else None
    # Catch ValueError (invalid date format) and TypeError (date is not a string)
    except (ValueError, TypeError):
        # Print an error message to inform about invalid date format
        print('Invalid Date!')
        # Return None to indicate date parsing failure
        return None

# Define a function to process the API response and extract relevant article data
def parse_data(response):
    # Initialize an empty list to store processed article dictionaries
    res = []
    # Initialize an empty list to store publication dates for finding the oldest date
    list_of_date = []

    # Iterate through each article item in the 'results' array from the API response
    for item in response['results']:

        # Extract the article title, using 'Nothing Found' as default if key doesn't exist
        title = item.get('title', 'Nothing Found')
        # Extract the news site/publisher name, using 'Nothing Found' as default if key doesn't exist
        news_site = item.get('news_site', 'Nothing Found')
        # Extract the publication timestamp, using 'Nothing Found' as default if key doesn't exist
        published_at = item.get('published_at', 'Nothing Found')
        # Extract the article URL, using 'Nothing Found' as default if key doesn't exist
        url = item.get('url', 'Nothing Found')

        # Process the publication date to extract only the date portion (YYYY-MM-DD)
        cleaned_date = parse_date(published_at)

        # Create a dictionary containing all the extracted and processed article data
        res_dict = {
            "title" : title,           # Article headline/title
            "news_site" : news_site,   # Publisher/news source name
            "published_at" : cleaned_date,  # Formatted publication date
            "url" : url,               # Direct link to the full article
        }

        # Add the cleaned date to the list for finding the oldest publication date
        list_of_date.append(cleaned_date)
        # Add the complete article dictionary to the results list
        res.append(res_dict)

    # Count the total number of articles processed from the API response
    counter = len(response['results'])
    # Find the oldest (minimum) publication date from all processed articles
    old_date = min(list_of_date)
    # Return a tuple containing the processed data, count, and oldest date
    return (res, counter, old_date)


# Execute the main API request to fetch 5 articles from the spaceflight news API
response = main_request(base_url, endpoint, 5)

# Process the API response to extract article data, count, and oldest date
res, counter, old_date = parse_data(response)

# Display the total number of articles successfully fetched from the API
print(f'Total articles fetched: {counter}')
# Display the oldest publication date among all fetched articles
print(f'Oldest article date: {old_date}')


# Create a pandas DataFrame from the processed article data (currently commented out)
df = pd.DataFrame(res)

# Save the DataFrame to a CSV file named 'articles.csv' without row indices (currently commented out)
df.to_csv('articles.csv', index=False)