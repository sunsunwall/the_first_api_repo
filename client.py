import requests
import json
import os

api_url = 'https://data.tomelilla.se/rowstore/dataset/3617552e-4c28-4a46-9b74-ac8bbbfee33f'

def fetch_data(api_url):

    json_stuff = None

    try:
        r = requests.get(api_url, timeout=10)
        r.raise_for_status()
        status_code = r.status_code

        json_stuff = r.json()

        print(f"Status code: {status_code}")
        print(f"This is a {type(json_stuff)} object. Please see contents below:")
        print(json_stuff)  

        with open("stuff.json", "w", encoding="utf-8") as f:
            json.dump(json_stuff, f, ensure_ascii=False)

    except requests.exceptions.Timeout:
        print("Request timed out - the server took too long to respond")
        
    except requests.exceptions.ConnectionError:
        print("Connection error - couldn't reach the server")
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return json_stuff

if __name__ == "__main__":
    result = fetch_data(api_url)
    
    if result is not None:
        print("✅ Data fetched and saved successfully!")
    else:
        print("❌ Failed to fetch data. No file was created.")