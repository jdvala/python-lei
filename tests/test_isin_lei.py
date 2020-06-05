from pathlib import Path

import pandas as pd
import pytest
from python_lei.exceptions import InvalidISIN, InvalidLEI
from python_lei.isin_lei import ISINtoLEI, LEItoISIN
from python_lei.utils import PROJECT_ROOT


@pytest.fixture(scope="module")
def get_isin_response():
    return [
        "SE0000382335",
        "US052800AB59",
        "US0528002084",
        "US0528003074",
        "US0528001094",
        "US0528001177",
    ]


def test_get_isin(get_isin_response):
    leitoisin = LEItoISIN()
    isin_list, isin_dataframe = leitoisin.get_isin(
        "A23RUXWKASG834LTMK28", return_dataframe=True
    )
    assert isin_list == get_isin_response

    df_isin = pd.read_csv(f"{PROJECT_ROOT}/tests/assets/isin_response.csv")
    # TODO: Use pandas to test the dataframes
    assert isin_dataframe["ISIN"].tolist() == df_isin["ISIN"].tolist()
    assert isin_dataframe["LEI"].tolist() == df_isin["LEI"].tolist()

    isin_list = leitoisin.get_isin("A23RUXWKASG834LTMK28")
    assert isin_list == get_isin_response


def test_get_isin_incorrect_lei():
    leitoisin = LEItoISIN()
    with pytest.raises(InvalidLEI) as exc_info:
        isin_list = leitoisin.get_isin("A23RUXWKASG834LTMK2")
    assert str(exc_info.value) == "Invalid LEI number"


def test_get_lei():
    isintolei = ISINtoLEI()
    lei_list = isintolei.get_lei("SE0000382335")
    assert lei_list == ["A23RUXWKASG834LTMK28"]


def test_get_lei_incorrect_isin():
    isintolei = ISINtoLEI()
    with pytest.raises(InvalidISIN) as exc_info:
        lei_list = isintolei.get_lei("SE000038233")
    assert str(exc_info.value) == "Invalid ISIN number"
