import requests
import json
import os
# In this version of the app we are introducing logging by use of the logging module for Python.
# In professional settings, it is more common to use logging rather than printing error statements.
import logging

# URL to the api we are using. In this case schools in the Swedish municipality of Tomelilla.
api_url = 'https://data.tomelilla.se/rowstore/dataset/3617552e-4c28-4a46-9b74-ac8bbbfee33f'

# Basic logging configuration
logging.basicConfig(
    # The mininum level of messages to show. From high to low the available levels are: CRITICAL, ERROR, WARNING, INFO, DEBUG.
    # We are setting ours to INFO, which means we will show all messages a part from DEBUG.
    level=logging.INFO,
    # With the format attribute we can decide HOW our messages should look and which info to contain.
    # In our case we chosing to show the time, the level and the actual message.
    # When logging we use percent formatting to interpolate the relevant variables into the log method.
    # The logging module by using percent formatting does "lazy interpolation" and only interpolates the needed variables.
    # If we used f-strings in logging, ALL variables (needed or not) would be interpolated, which could lead to performance issues.
    # Syntax:
    # format = atttribute
    # %() the modulo operator tells Python a value will be inserted here, in our case, a timestamp for instance.
    # s = format as a string
    # d = format as a decimal or integer
    # In this case we are chosing to show:
    # Timestamp, the file and line where the logging happened, the logging level name and the actual message
    format="%(asctime)s | %(filename)s:%(lineno)d | %(levelname)s | %(message)s",
    # We use handlers to tell logging where to send our logging messages
    handlers=[
        # The FileHandler creates and saves logs in a file.
        logging.FileHandler("api_client_log"),
        # The StreamHandler sends logs to the console.
        logging.StreamHandler()
    ]
)

# Initialize logger - the logger will takes it name from the name of the file it is logging.
logger = logging.getLogger(__name__)

def fetch_data(api_url):

    json_stuff = None

    try:
        r = requests.get(api_url, timeout=10)
        r.raise_for_status()
        status_code = r.status_code

        json_stuff = r.json()

        # Show info message of success
        logger.info(f"API request successful. Status code: {status_code}")
        # This will only show when the app is run in debugging mode. In our logging basic config we defined that debug messages would be left out of production.
        logger.debug(f"Response data: {json_stuff}")

        with open("stuff.json", "w", encoding="utf-8") as f:
            json.dump(json_stuff, f, ensure_ascii=False)

        # Log that the data fetched from the API was saved successfully
        logger.info("Response data saved to stuff.json")

    except requests.exceptions.Timeout:
        logger.error("Request timed out - the server took too long to respond")
        
    except requests.exceptions.ConnectionError:
        logger.error("Connection error - couldn't reach the server")
        
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")

    return json_stuff

if __name__ == "__main__":
    result = fetch_data(api_url)
    
    if result is not None:
        logger.info("✅ Data fetched and saved successfully!")
    else:
        logger.warning("❌ Failed to fetch data. No file was created.")