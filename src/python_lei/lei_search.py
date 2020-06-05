import requests
from python_lei.exceptions import NotFound
import logging
from texttable import Texttable

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SearchLEI:
    """
    Search LEI number from name
    """

    def __init__(self):
        self.search_url = "https://api.leilex.com/API/LEI/AutoComplete/"

    def search_lei(self, company_name, show_table=False):
        """
        Search LEI numbers with company name

        Args:
            company_name (str): Name of the company to search LEI numbers for
        
        Returns:
            raw_output (List): Raw output from the API

        """
        if not isinstance(company_name, str):
            raise ValueError("Company Name should be a string")

        if not company_name:
            raise NotFound("Company Name not found. Please provide a company name")

        raw_output = self._request_api(company_name)

        if not raw_output:
            logger.info(f"No LEI found for company name {company_name}")

        if not show_table:
            return raw_output

        # Initalize the table
        table = Texttable()
        table.add_row(["Legal Name", "LEI"])

        for legal_entity in raw_output:
            table.add_row([legal_entity.get("LegalName"), legal_entity.get("LEI")])

        return raw_output, table.draw()

    def _request_api(self, company_name):
        """
        Request LEI autocomplete api to obtain possible list of LEI numbers
        """
        try:
            response = requests.get(
                f"{self.search_url}?query={company_name}&filterType=Name"
            )

            if not response.ok:
                logger.info("No response form the API")
                return
            return response.json()
        except requests.exceptions.ConnectionError as err:
            logger.error("Error connecting to API host", exc_info=err)
            return
