import requests

class RestCountriesAPI:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch data from the API")

    def get_country_by_name(self, country_name):
        for country in self.data:
            if country_name.lower() in country.get('name', {}).get('common', '').lower():
                return country
        return None

    def get_all_countries(self):
        return [country['name']['common'] for country in self.data]

    def get_population_by_country(self, country_name):
        country = self.get_country_by_name(country_name)
        if country:
            return country.get('population', 'Population data not available')
        return "Country not found"

# Example Usage:
url = "https://restcountries.com/v3.1/all"
rest_countries = RestCountriesAPI(url)

# Get information about a specific country
country_name = "India"
country_info = rest_countries.get_country_by_name(country_name)
print(f"Information about {country_name}: {country_info}")

# Get the population of a specific country
population = rest_countries.get_population_by_country(country_name)
print(f"Population of {country_name}: {population}")

# Get a list of all countries
all_countries = rest_countries.get_all_countries()
print("List of all countries:", all_countries)
