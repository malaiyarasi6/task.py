import requests

def display_countries_and_currencies():
    url = 'https://restcountries.com/v3.1/all'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        countries_data = response.json()  # Parse JSON data

        for country in countries_data:
            country_name = country['name']['common']
            currencies = country.get('currencies', {})
            
            if currencies:
                for currency_code, currency_info in currencies.items():
                    currency_name = currency_info.get('name', 'N/A')
                    currency_symbol = currency_info.get('symbol', 'N/A')
                    print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {currency_symbol}")
            else:
                print(f"Country: {country_name}, Currency: N/A, Symbol: N/A")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage
display_countries_and_currencies()