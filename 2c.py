import requests

def fetch_breweries_with_websites(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        breweries = response.json()
        # Filter breweries with non-empty website URLs
        return [brewery for brewery in breweries if brewery.get('website_url')]
    else:
        return []

def main():
    states = ['alaska', 'maine', 'new_york']
    for state in states:
        print(f"Breweries with websites in {state.title()}:")
        breweries_with_websites = fetch_breweries_with_websites(state)
        count = len(breweries_with_websites)
        print(f"  Total count: {count}")
        for brewery in breweries_with_websites:
            print(f"    Name: {brewery['name']}, Website: {brewery['website_url']}")
        print()

if __name__ == "__main__":
    main()
