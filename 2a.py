import requests

def fetch_breweries_count(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        return len(response.json())
    else:
        return 0

def main():
    states = ['alaska', 'maine', 'new_york']
    for state in states:
        count = fetch_breweries_count(state)
        print(f"Number of breweries in {state.title()}: {count}")

if __name__ == "__main__":
    main()
