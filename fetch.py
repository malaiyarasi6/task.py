import requests

def fetch_country_data():
    url = 'https://restcountries.com/v3.1/all'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Parse JSON data
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage
country_data = fetch_country_data()
if country_data:
    print("Data fetched successfully!")
    # You can now work with the data
    for country in country_data:
        print(country['name']['common'])  # Print each country's common name
