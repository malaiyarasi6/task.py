import requests

def fetch_breweries(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return [brewery['name'] for brewery in response.json()]
    else:
        return []

def main():
    states = ['alaska', 'maine', 'new_york']
    for state in states:
        print(f"Breweries in {state.title()}:")
        breweries = fetch_breweries(state)
        if breweries:
            for name in breweries:
                print(f" - {name}")
        else:
            print(" No breweries found.")
        print()

if __name__ == "__main__":
    main()
