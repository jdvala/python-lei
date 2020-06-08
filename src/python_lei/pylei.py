import logging

import pandas as pd
import requests
from dateutil.parser import parse
from python_lei.exceptions import InvalidLEI
from python_lei.parser import LEIParser

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class pyLEI:
    """
    Main class to handle lei requests and return data
    """

    def __init__(self):
        """
        Initialize API URL
        """
        self.api_url = "https://api.leilex.com/API/LEI/"

    def get_lei_info(self, lei_list, return_dataframe=False):
        """
        Request API and return response
        
        Args:
            lei_list: List of LEIs
            return_dataframe: Whether to return a dataframe or not.
        
        Returns:
            raw_output: List of Dicts with raw API json response
            lei_results: LEI result as class
            dataframe: Pandas dataframe with results.
        """
        if not isinstance(lei_list, list):
            raise AttributeError("Invalid input, please provide LEI in a list")

        if any(lei for lei in lei_list if len(lei) != 20):
            raise InvalidLEI("Invalid LEI number found in the list")

        if len(lei_list) > 20:
            raise ValueError(
                "To respect the free API request quota we have limited the current LEI numbers to 20"
            )

        raw_output = self._request_api(lei_list)

        if not raw_output:
            if return_dataframe:
                return None, None, None
            else:
                return None, None

        lei_results = LEIParser(raw_output)
        if return_dataframe:
            dataframe = pd.DataFrame(
                {
                    "LEI": lei_results.lei_list,
                    "Legal_Name": lei_results.lei_names,
                    "Legal_Jurisdiction": lei_results.lei_legal_jurisdictions,
                    "LegalForm": lei_results.lei_legal_forms,
                    "Other_Legal_Form": lei_results.lei_other_legal_forms,
                    "Entity_Status": lei_results.lei_entity_status,
                    "Entity_Expiration_Date": lei_results.lei_entity_expiration_dates,
                    "Entity_Expiration_Reason": lei_results.lei_entity_expiration_reasons,
                    "Successor_Entity": lei_results.lei_successor_entities,
                    "InitialRegistrationDate": [
                        parse(date)
                        for date in lei_results.lei_initial_registration_dates if date
                    ],
                    "Last_Update_Date": [
                        parse(date) for date in lei_results.lei_last_update_dates if date
                    ],
                    "Registration_Status": lei_results.lei_registration_status,
                    "Next_Renewal_Date": lei_results.lei_next_renewal_dates,
                    "Managing_LOU": lei_results.lei_managing_LOU,
                    "Validation_Sources": lei_results.lei_validation_sources,
                    "Associated_LEI": lei_results.lei_associated_lei,
                    "Associated_Entity_Name": lei_results.lei_associated_entity_names,
                    "Associated_Entity_Type": lei_results.lei_associated_entity_types,
                    "Registration_Authority_ID": lei_results.lei_registration_authority_ids,
                    "Registration_Authority_Entity_ID": lei_results.lei_registration_authority_entite_ids,
                    "Entity_Category": lei_results.lei_entity_categories,
                    "Address_1_Line_1": lei_results.lei_address_1_line_1,
                    "Address_1_Line_2": lei_results.lei_address_1_line_2,
                    "Address_1_Line_3": lei_results.lei_address_1_line_3,
                    "Address_1_Line_4": lei_results.lei_address_1_line_4,
                    "Address_1_city": lei_results.lei_address_1_city,
                    "Address_1_region": lei_results.lei_address_1_region,
                    "Address_1_country": lei_results.lei_address_1_country,
                    "Address_1_postal_code": lei_results.lei_address_1_postal_code,
                    "Address_1_type": lei_results.lei_address_2_address_type,
                    "Address_2_Line_1": lei_results.lei_address_2_line_1,
                    "Address_2_Line_2": lei_results.lei_address_2_line_2,
                    "Address_2_Line_3": lei_results.lei_address_2_line_3,
                    "Address_2_Line_4": lei_results.lei_address_2_line_4,
                    "Address_2_city": lei_results.lei_address_2_city,
                    "Address_2_region": lei_results.lei_address_2_region,
                    "Address_2_country": lei_results.lei_address_2_country,
                    "Address_2_postal_code": lei_results.lei_address_2_postal_code,
                    "Address_2_type": lei_results.lei_address_2_address_type,
                    "Other_Name": lei_results.lei_other_name_name,
                    "Other_Name_Language": lei_results.lei_other_name_language,
                    "Other_Name_Type": lei_results.lei_other_name_type,
                    "Relationship_1_Patrent_LEI": lei_results.lei_relationships_1_parent_lei,
                    "Relationship_1_Relationship_Type": lei_results.lei_relationships_1_parent_relationship_type,
                    "Relationship_1_Relationship_Status": lei_results.lei_relationships_1_parent_relationship_status,
                    "Relationship_1_Initial_Registration_Date": [
                        parse(date)
                        for date in lei_results.lei_relationships_1_parent_initial_registration_date if date
                    ],
                    "Relationship_1_Last_Update_Date": [
                        parse(date)
                        for date in lei_results.lei_relationships_1_parent_last_updated if date
                    ],
                    "Relationship_1_Registration_Status": lei_results.lei_relationships_1_parent_registration_status,
                    "Relationship_1_Next_Renewal_Date": [
                        parse(date)
                        for date in lei_results.lei_relationships_1_parent_next_renewal_date if date
                    ],
                    "Relationship_1_Managing_Lou": lei_results.lei_relationships_1_parent_managing_LOU,
                    "Relationship_1_Validation_Sources": lei_results.lei_relationships_1_parent_validation_sources,
                    "Relationship_1_Validation_Documents": lei_results.lei_relationships_1_parent_validation_documents,
                    "Relationship_1_Validation_Reference": lei_results.lei_relationships_1_parent_validation_reference,
                    "Relationship_2_Patrent_LEI": lei_results.lei_relationships_2_parent_lei,
                    "Relationship_2_Relationship_Type": lei_results.lei_relationships_2_parent_relationship_type,
                    "Relationship_2_Relationship_Status": lei_results.lei_relationships_2_parent_relationship_status,
                    "Relationship_2_Initial_Registration_Date": [
                        parse(date)
                        for date in lei_results.lei_relationships_2_parent_initial_registration_date if date
                    ],
                    "Relationship_2_Last_Update_Date": [
                        parse(date)
                        for date in lei_results.lei_relationships_2_parent_last_updated if date
                    ],
                    "Relationship_2_Registration_Status": lei_results.lei_relationships_2_parent_registration_status,
                    "Relationship_2_Next_Renewal_Date": [
                        parse(date)
                        for date in lei_results.lei_relationships_2_parent_next_renewal_date if date
                    ],
                    "Relationship_2_Managing_Lou": lei_results.lei_relationships_2_parent_managing_LOU,
                    "Relationship_2_Validation_Sources": lei_results.lei_relationships_2_parent_validation_sources,
                    "Relationship_2_Validation_Documents": lei_results.lei_relationships_2_parent_validation_documents,
                    "Relationship_2_Validation_Reference": lei_results.lei_relationships_2_parent_validation_reference,
                    "Reporting_Exceptions_1_LEI": lei_results.lei_reporting_exception_1_lei,
                    "Reporting_Exceptions_1_Category": lei_results.lei_reporting_exception_1_category,
                    "Reporting_Exceptions_2_LEI": lei_results.lei_reporting_exception_2_lei,
                    "Reporting_Exceptions_2_Category": lei_results.lei_reporting_exception_2_category,
                }
            )

            return raw_output, lei_results, dataframe

        return raw_output, lei_results

    def _request_api(self, lei_list):
        """
        Requests LEI api and obtain the response

        Args:
            lei_list: List of LEIs
        
        Returns:
            api_responses: List of Dicts, json response from api
        """
        api_responses = []

        for lei in lei_list:
            try:
                response = requests.get(f"{self.api_url}/{lei}")
            except requests.exceptions.ConnectionError as err:
                logger.error("Error connecting to API host", exc_info=err)
                continue

            if not response.ok:
                logger.warning(f"No response from API for LEI number {lei}")
                continue

            api_responses.append(response.json())

        return api_responses
