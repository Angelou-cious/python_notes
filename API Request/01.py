import requests  # Import the requests library for making HTTP API calls
import pandas as pd  # Import pandas library for data manipulation and CSV operations

base_url = "https://jsonplaceholder.typicode.com/"  # Define the base URL for the JSONPlaceholder API
end_point = 'photos'  # Define the specific endpoint to fetch photos data

def main_request(base_url, endpoint):  # Define function to make API request with base URL and endpoint parameters
    response = requests.get(base_url + end_point)  # Send GET request to the combined URL (base_url + endpoint)
    return response.json()  # Convert the response to JSON format and return it

def get_numbers(response):  # Define function to count the number of items in the response
    return len(response)  # Return the length/count of items in the response list
   
def parse_data(response):  # Define function to extract and structure specific data from the API response
    res_list = []  # Initialize an empty list to store the parsed data
    for item in response:  # Loop through each item in the response list
        # print(f"{item['id']}: {item['title']}")  # Commented out debug print statement
        res_dict = {  # Create a dictionary with selected fields from each item
            'id': item['id'],  # Extract the 'id' field from the current item
            'title': item['title'],  # Extract the 'title' field from the current item
        }
        res_list.append(res_dict)  # Add the dictionary to the results list
    return res_list  # Return the list of parsed dictionaries


data = main_request(base_url=base_url, endpoint=end_point)  # Call the API and store the JSON response in 'data'

results = parse_data(data)  # Parse the API data to extract only id and title fields

df = pd.DataFrame(results)  # Convert the parsed results list into a pandas DataFrame

print(df.head(), df.tail())  # Display the first 5 and last 5 rows of the DataFrame

df.to_csv('photos.csv', index=False)  # Export the DataFrame to a CSV file without row indices
