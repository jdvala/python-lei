import io
import logging
import os
import shutil
import zipfile
from datetime import date
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


PROJECT_ROOT = Path(__file__).parent.parent.parent
RESOURCE_DIR = os.path.join(PROJECT_ROOT, "resources")
TODAY = date.today().strftime("%Y%m%d")


class Download:
    """
    Download LEI to ISIN mappings
    """

    def __init__(self, _is_actions=False):
        """
        Downloads LEI ISIN mapping 

        Args:
            _is_actions (bool): For setting path of downloaded resources on Github Actions
        """
        self.data_url = "https://www.gleif.org/en/lei-data/lei-mapping/download-isin-to-lei-relationship-files"        
        self._download(_is_actions)

    def _download(self, _is_actions):
        """
        Initiate download into resource folder
        """
        if not os.path.exists(RESOURCE_DIR):
            logger.info(f"No resources directory found, creating resources directory.")
            os.mkdir(RESOURCE_DIR)

        download_link = self._scrape_isin_file()

        if not download_link:
            raise ValueError("Downloading of isin file not available.")

        try:
            response = requests.get(download_link)
        except requests.exceptions as err:
            logger.error(
                "Connection Error, Unable to download data at this time. Please check you have working internet connection or try again later."
            )
        if not response.ok:
            logger.error("No response from GLEIF server.")

        logger.info("The file could be over 50 Mb.")
        zipped_content = zipfile.ZipFile(io.BytesIO(response.content))
        if _is_actions:
            zipped_content.extractall(
                "/home/runner/work/python-lei/python-lei/resources"
            )
        else:
            zipped_content.extractall(RESOURCE_DIR)
            logger.info(f"Extraction complete in {RESOURCE_DIR}")
    
    def _scrape_isin_file(self):
        """
        Scrape the data.
        """
        try:
            response = requests.get(self.data_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text)
        
            # find all the tr and td and get to the href
            download_link = soup.find_all("tr")[1].find_all("td")[1].find("a")["href"]
            return download_link

        except requests.ConnectionError:
            logger.error(f"Error connecting to {self.data_url}")
       

class Update:
    """
    Update the ISIN mapping in the resource folder
    """

    def __init__(self):
        """
        Update the ISIN LEI data
        """
        # Remove the old data and call the download class

        if (
            not os.path.exists(RESOURCE_DIR) or os.listdir(RESOURCE_DIR) == []
        ):  # TODO: use not
            logger.info(
                "Resource directory not found or LEI ISIN mappings not found. Downloading now."
            )
            Download()

        if os.listdir(RESOURCE_DIR) != []:
            shutil.rmtree(RESOURCE_DIR)
            logger.info(f"Downloading Data in {RESOURCE_DIR}")
            Download()


def load_data():
    """
    Loads and Returns the dataframe
    """
    dataframe = pd.read_csv(os.path.join(RESOURCE_DIR, os.listdir(RESOURCE_DIR)[0]))
    return dataframe
