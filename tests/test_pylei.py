from unittest.mock import patch

import pandas as pd
import pytest
from python_lei.exceptions import InvalidLEI
from python_lei.pylei import pyLEI
from python_lei.utils import PROJECT_ROOT


@pytest.fixture(scope="module")
def lei_api_response():
    return [
        {
            "total_record_count": 1,
            "page_number": 1,
            "page_size": 100,
            "total_pages": 1,
            "has_more": False,
            "records": [
                {
                    "LEI": "A23RUXWKASG834LTMK28",
                    "LegalName": "AUTOLIV, INC.",
                    "LegalJurisdiction": "US-DE",
                    "LegalForm": "XTIQ",
                    "OtherLegalForm": "",
                    "EntityStatus": "ACTIVE",
                    "EntityExpirationDate": None,
                    "EntityExpirationReason": "",
                    "SuccessorEntity": "",
                    "InitialRegistrationDate": "2012-06-06T03:52:00.000 +00:00",
                    "LastUpdateDate": "2019-12-18T03:32:00.000 +00:00",
                    "RegistrationStatus": "ISSUED",
                    "NextRenewalDate": "2020-12-15T10:15:00.000 +00:00",
                    "ManagingLOU": "EVK05KS7XY1DEII3R011",
                    "ValidationSources": "FULLY_CORROBORATED",
                    "AssociatedLEI": "",
                    "AssociatedEntityName": "",
                    "AssociatedEntityType": "",
                    "RegistrationAuthorityID": "RA000602                                ",
                    "OtherRegistrationAuthorityID": "",
                    "RegistrationAuthorityEntityID": "2155072",
                    "EntityCategory": "",
                    "Addresses": [
                        {
                            "Line1": "Box 70381",
                            "Line2": "",
                            "Line3": "",
                            "Line4": "",
                            "City": "Stockholm",
                            "Region": "SE-AB",
                            "Country": "SE",
                            "PostalCode": "107 24",
                            "OtherType": "",
                            "AddressType": "HEADQUARTERS_ADDRESS",
                        },
                        {
                            "Line1": "C/O THE CORPORATION TRUST COMPANY",
                            "Line2": "CORPORATION TRUST CENTER 1209 ORANGE ST",
                            "Line3": "",
                            "Line4": "",
                            "City": "WILMINGTON",
                            "Region": "US-DE",
                            "Country": "US",
                            "PostalCode": "19801",
                            "OtherType": "",
                            "AddressType": "LEGAL_ADDRESS",
                        },
                    ],
                    "OtherNames": [],
                    "ValidationAuthorities": [
                        {
                            "ValidationAuthorityID": "RA000602",
                            "OtherValidationAuthorityID": "",
                            "ValidationAuthorityEntityID": "2155072",
                        }
                    ],
                    "Relationships": [],
                    "ReportingExceptions": [
                        {
                            "LEI": "A23RUXWKASG834LTMK28",
                            "ExceptionCategory": "DIRECT_ACCOUNTING_CONSOLIDATION_PARENT",
                            "ExceptionReasons": [{"Reason": "NON_CONSOLIDATING"}],
                            "ExceptionReferences": [],
                        },
                        {
                            "LEI": "A23RUXWKASG834LTMK28",
                            "ExceptionCategory": "ULTIMATE_ACCOUNTING_CONSOLIDATION_PARENT",
                            "ExceptionReasons": [{"Reason": "NON_CONSOLIDATING"}],
                            "ExceptionReferences": [],
                        },
                    ],
                }
            ],
        }
    ]


def test_get_lei_info(lei_api_response):
    getleiinfo = pyLEI()
    with patch.object(pyLEI, "_request_api", return_value=lei_api_response):
        raw_output, lei_results = getleiinfo.get_lei_info(["A23RUXWKASG834LTMK28"])

    assert raw_output == [
        {
            "total_record_count": 1,
            "page_number": 1,
            "page_size": 100,
            "total_pages": 1,
            "has_more": False,
            "records": [
                {
                    "LEI": "A23RUXWKASG834LTMK28",
                    "LegalName": "AUTOLIV, INC.",
                    "LegalJurisdiction": "US-DE",
                    "LegalForm": "XTIQ",
                    "OtherLegalForm": "",
                    "EntityStatus": "ACTIVE",
                    "EntityExpirationDate": None,
                    "EntityExpirationReason": "",
                    "SuccessorEntity": "",
                    "InitialRegistrationDate": "2012-06-06T03:52:00.000 +00:00",
                    "LastUpdateDate": "2019-12-18T03:32:00.000 +00:00",
                    "RegistrationStatus": "ISSUED",
                    "NextRenewalDate": "2020-12-15T10:15:00.000 +00:00",
                    "ManagingLOU": "EVK05KS7XY1DEII3R011",
                    "ValidationSources": "FULLY_CORROBORATED",
                    "AssociatedLEI": "",
                    "AssociatedEntityName": "",
                    "AssociatedEntityType": "",
                    "RegistrationAuthorityID": "RA000602                                ",
                    "OtherRegistrationAuthorityID": "",
                    "RegistrationAuthorityEntityID": "2155072",
                    "EntityCategory": "",
                    "Addresses": [
                        {
                            "Line1": "Box 70381",
                            "Line2": "",
                            "Line3": "",
                            "Line4": "",
                            "City": "Stockholm",
                            "Region": "SE-AB",
                            "Country": "SE",
                            "PostalCode": "107 24",
                            "OtherType": "",
                            "AddressType": "HEADQUARTERS_ADDRESS",
                        },
                        {
                            "Line1": "C/O THE CORPORATION TRUST COMPANY",
                            "Line2": "CORPORATION TRUST CENTER 1209 ORANGE ST",
                            "Line3": "",
                            "Line4": "",
                            "City": "WILMINGTON",
                            "Region": "US-DE",
                            "Country": "US",
                            "PostalCode": "19801",
                            "OtherType": "",
                            "AddressType": "LEGAL_ADDRESS",
                        },
                    ],
                    "OtherNames": [],
                    "ValidationAuthorities": [
                        {
                            "ValidationAuthorityID": "RA000602",
                            "OtherValidationAuthorityID": "",
                            "ValidationAuthorityEntityID": "2155072",
                        }
                    ],
                    "Relationships": [],
                    "ReportingExceptions": [
                        {
                            "LEI": "A23RUXWKASG834LTMK28",
                            "ExceptionCategory": "DIRECT_ACCOUNTING_CONSOLIDATION_PARENT",
                            "ExceptionReasons": [{"Reason": "NON_CONSOLIDATING"}],
                            "ExceptionReferences": [],
                        },
                        {
                            "LEI": "A23RUXWKASG834LTMK28",
                            "ExceptionCategory": "ULTIMATE_ACCOUNTING_CONSOLIDATION_PARENT",
                            "ExceptionReasons": [{"Reason": "NON_CONSOLIDATING"}],
                            "ExceptionReferences": [],
                        },
                    ],
                }
            ],
        }
    ]

    assert lei_results.lei_names == ["AUTOLIV, INC."]
    assert lei_results.lei_list == ["A23RUXWKASG834LTMK28"]

    with patch.object(pyLEI, "_request_api", return_value=lei_api_response):
        raw_output, lei_results, dataframe = getleiinfo.get_lei_info(
            ["A23RUXWKASG834LTMK28"], return_dataframe=True
        )

    df_lei_info = pd.read_csv(f"{PROJECT_ROOT}/tests/assets/dataframe_getleiinfo.csv")
    # TODO: Check with pandas
    # pd.testing.assert_frame_equal(df_lei_info, dataframe, check_dtype = False)

    assert df_lei_info["LEI"].tolist() == dataframe["LEI"].tolist()
    assert df_lei_info["Legal_Name"].tolist() == dataframe["Legal_Name"].tolist()


def test_get_lei_info_not_list():
    getleiinfo = pyLEI()
    with pytest.raises(AttributeError) as exc_info:
        getleiinfo.get_lei_info("A23RUXWKASG834LTMK2")
    assert str(exc_info.value) == "Invalid input, please provide LEI in a list"


def test_get_lei_info_invalid_lei():
    getleiinfo = pyLEI()
    with pytest.raises(InvalidLEI) as exc_info:
        getleiinfo.get_lei_info(["A23RUXWKASG834LTK2"])
    assert str(exc_info.value) == "Invalid LEI number found in the list"


def test_get_lei_info_lei_list_long():
    getleiinfo = pyLEI()
    with pytest.raises(ValueError) as exc_info:
        getleiinfo.get_lei_info(["A23RUXWKASG834LTMK28"] * 25)
    assert (
        str(exc_info.value)
        == "To respect the free API request quota we have limited the current LEI numbers to 20"
    )
