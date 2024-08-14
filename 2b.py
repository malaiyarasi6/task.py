import requests
from collections import defaultdict

def fetch_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def count_breweries_by_type_and_city(breweries):
    city_types = defaultdict(lambda: defaultdict(int))
    for brewery in breweries:
        city = brewery.get('city', 'Unknown City')
        brew_type = brewery.get('brewery_type', 'Unknown Type')
        city_types[city][brew_type] += 1
    return city_types

def main():
    states = ['alaska', 'maine', 'new_york']
    for state in states:
        print(f"Breweries in {state.title()}:")
        breweries = fetch_breweries_by_state(state)
        city_types = count_breweries_by_type_and_city(breweries)
        
        for city, types in city_types.items():
            print(f"  City: {city}")
            for brew_type, count in types.items():
                print(f"    Type: {brew_type}, Count: {count}")
        print()

if __name__ == "__main__":
    main()

