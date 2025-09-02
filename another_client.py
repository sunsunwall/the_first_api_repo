import requests
import json
import os
import logging

api_url = "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/17.9070/lat/59.3516/data.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(filename)s:%(lineno)d | %(levelname)s | %(message)s", # 59.35167827164732, 17.907036519914694
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("api_client_log.log")
    ]
)

logger = logging.getLogger(__name__)

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        smhi_data = response.json()
        
        logger.info("Data fetched successfully.")

        with open("smhi_data.json", "w", encoding="utf-8") as f:
            json.dump(smhi_data, f, ensure_ascii=False)

        return smhi_data
        
    except requests.exceptions.Timeout:
        logger.error("Request timed out - the server took too long to respond")
        
    except requests.exceptions.ConnectionError:
        logger.error("Connection error - couldn't reach the server")
        
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":

    result = fetch_data(api_url)

    if result is not None:
        logger.info("✅ SUCCESS: Data fetched - writing data to smhi_data.json")
    else:
        logger.error("❌ FAILED: No data fetched - not writing to file")