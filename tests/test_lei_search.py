from pathlib import Path
from unittest.mock import Mock, patch

import pandas as pd
import pytest
from python_lei.exceptions import NotFound
from python_lei.lei_search import SearchLEI


@pytest.fixture(scope="module")
def lei_search_response():
    return [
        {"LegalName": "Cleantech Benelux SPRL", "LEI": "549300DON6QM36Z6CQ75"},
        {"LegalName": "CLEANTECH EUROPE I (A) LP", "LEI": "2138006HK4WI7O5AZZ55"},
        {"LegalName": "Cleantech Management GmbH", "LEI": "391200V6W1JRTEX52V10"},
        {"LegalName": "Cleantech Treuvermögen GmbH", "LEI": "391200GQTDEQKN7T4U12"},
        {"LegalName": "Cleantech Infrastruktur GmbH", "LEI": "391200NWGDYHODS1IZ56"},
        {
            "LegalName": "CLEANTECH BUILDING MATERIALS PLC",
            "LEI": "213800AF6AQVK2PFVY02",
        },
        {
            "LegalName": "Cleantech Vision PV 10 GmbH & Co KG",
            "LEI": "391200DYVTFX12QHSL88",
        },
        {
            "LegalName": "Cleantech Vision PV 13 GmbH & Co KG",
            "LEI": "391200LFEW46QDOULC94",
        },
        {
            "LegalName": "Cleantech Vision PV 14 GmbH & Co KG",
            "LEI": "3912007UV23HZYGP7P98",
        },
        {
            "LegalName": "CLEANTECH EUROPE II LUXEMBOURG S.À R.L.",
            "LEI": "213800T4PUCAV91BS318",
        },
        {
            "LegalName": "CLEANTECH SOLAR ENERGY (INDIA) PRIVATE LIMITED",
            "LEI": "335800DYTSIUIRGDOY08",
        },
        {
            "LegalName": "Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200BCW28KLMPO7X74",
        },
        {
            "LegalName": "AC Cleantech Growth Fund I Holding AB",
            "LEI": "549300WEAJ76PQLCY106",
        },
        {"LegalName": "KSL CLEANTECH LIMITED", "LEI": "9845006C6DBHCB91TA46"},
        {"LegalName": "SBG CLEANTECH LIMITED", "LEI": "984500BA390DEEC8A198"},
        {"LegalName": "SFN Cleantech Investment Ltd", "LEI": "5299001U27KH2TE1HA16"},
        {
            "LegalName": "SBG CLEANTECH PROJECTCO PRIVATE LIMITED",
            "LEI": "335800L6KBRBMN23G491",
        },
        {
            "LegalName": "SBG CLEANTECH ENERGY EIGHT PRIVATE LIMITED",
            "LEI": "33580025O3MECVXEXN20",
        },
        {
            "LegalName": "SBG CLEANTECH PROJECTCO FIVE PRIVATE LIMITED",
            "LEI": "335800VKNBX6UT5XTA61",
        },
        {"LegalName": "AMPL CLEANTECH PRIVATE LIMITED", "LEI": "3358003BN2TSHLZFK835"},
        {"LegalName": "TATA CLEANTECH CAPITAL LIMITED", "LEI": "335800VHGHY6ACK4EV23"},
        {
            "LegalName": "OPEN CLEANTECH INCOME SECURITIES DAC",
            "LEI": "635400RZAFJOB3F3HO02",
        },
        {
            "LegalName": "ACME CLEANTECH SOLUTIONS PRIVATE LIMITED",
            "LEI": "335800Y9QOUKCKEBDN64",
        },
        {"LegalName": "FFG - CLEANTECH II", "LEI": "549300BOYS2N4DQ86621"},
        {"LegalName": "Ikaros Cleantech AB", "LEI": "529900F3ILO82OOHJ624"},
        {"LegalName": "ARENKO CLEANTECH LIMITED", "LEI": "213800XJAKB99U6GYE81"},
        {
            "LegalName": "CHORUS CleanTech PP Life GmbH & Co. 8. KG",
            "LEI": "39120001P89AEAGP4C95",
        },
        {
            "LegalName": "Vierte Cleantech Infrastrukturgesellschaft mbH",
            "LEI": "391200MHC20BINNZSM38",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Vilseck KG",
            "LEI": "39120001CK4NXMUXLH16",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Vilseck KG",
            "LEI": "39120001CK4NXMUXLH82",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Bockelwitz KG",
            "LEI": "39120001IO1IEBNJB658",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Bockelwitz KG",
            "LEI": "39120001IO1IEBNJB640",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Richelbach KG",
            "LEI": "39120001I4DLSGVIED33",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Richelbach KG",
            "LEI": "39120001I4DLSGVIED65",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarparks Niederbayern KG",
            "LEI": "391200XOFXB6SEDEUE64",
        },
        {
            "LegalName": "Dritte Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200D4IQYJZH3PQV66",
        },
        {
            "LegalName": "Fünfte Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200YSBV1PTJDIVU78",
        },
        {
            "LegalName": "Zweite Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200B0QA2GDAGUWL36",
        },
        {"LegalName": "Kentara Cleantech S.à r.l.", "LEI": "549300O1LH5FYDMNBI61"},
        {
            "LegalName": "TRINITY CLEANTECH PRIVATE LIMITED",
            "LEI": "3358007KMDXWXRDRLJ07",
        },
        {"LegalName": "FUNDO EDP CLEANTECH FCR", "LEI": "529900YNVY87YJXQQL73"},
        {"LegalName": "CAPRICORN CLEANTECH FUND", "LEI": "5493000VTLH53534F243"},
        {
            "LegalName": "SBSR POWER CLEANTECH ELEVEN PRIVATE LIMITED",
            "LEI": "335800PDQXWJSCUT1763",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure Fund SICAV",
            "LEI": "391200IW2I7VHRGVL291",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure (Czech) a.s.",
            "LEI": "391200SNUDPCVPZHNT11",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure Holding GmbH",
            "LEI": "391200RVK5MPKRZEMA60",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure Asia Holding GmbH",
            "LEI": "39120062GAN8OFYXWW72",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure (Liechtenstein) AG",
            "LEI": "391200KABA0XCWJDTK89",
        },
        {
            "LegalName": "Desjardins SocieTerra Cleantech Fund",
            "LEI": "54930032H86FEEE8KT71",
        },
        {
            "LegalName": "INVESCO EXCHANGE-TRADED FUND TRUST - Invesco Cleantech ETF",
            "LEI": "549300O3D3IUFT3CTM23",
        },
    ]


def test_search_lei(lei_search_response):
    possible_lei = SearchLEI()
    with patch.object(SearchLEI, "_request_api", return_value=lei_search_response):
        raw_output = possible_lei.search_lei("CleanTech")

    assert raw_output == [
        {"LegalName": "Cleantech Benelux SPRL", "LEI": "549300DON6QM36Z6CQ75"},
        {"LegalName": "CLEANTECH EUROPE I (A) LP", "LEI": "2138006HK4WI7O5AZZ55"},
        {"LegalName": "Cleantech Management GmbH", "LEI": "391200V6W1JRTEX52V10"},
        {"LegalName": "Cleantech Treuvermögen GmbH", "LEI": "391200GQTDEQKN7T4U12"},
        {"LegalName": "Cleantech Infrastruktur GmbH", "LEI": "391200NWGDYHODS1IZ56"},
        {
            "LegalName": "CLEANTECH BUILDING MATERIALS PLC",
            "LEI": "213800AF6AQVK2PFVY02",
        },
        {
            "LegalName": "Cleantech Vision PV 10 GmbH & Co KG",
            "LEI": "391200DYVTFX12QHSL88",
        },
        {
            "LegalName": "Cleantech Vision PV 13 GmbH & Co KG",
            "LEI": "391200LFEW46QDOULC94",
        },
        {
            "LegalName": "Cleantech Vision PV 14 GmbH & Co KG",
            "LEI": "3912007UV23HZYGP7P98",
        },
        {
            "LegalName": "CLEANTECH EUROPE II LUXEMBOURG S.À R.L.",
            "LEI": "213800T4PUCAV91BS318",
        },
        {
            "LegalName": "CLEANTECH SOLAR ENERGY (INDIA) PRIVATE LIMITED",
            "LEI": "335800DYTSIUIRGDOY08",
        },
        {
            "LegalName": "Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200BCW28KLMPO7X74",
        },
        {
            "LegalName": "AC Cleantech Growth Fund I Holding AB",
            "LEI": "549300WEAJ76PQLCY106",
        },
        {"LegalName": "KSL CLEANTECH LIMITED", "LEI": "9845006C6DBHCB91TA46"},
        {"LegalName": "SBG CLEANTECH LIMITED", "LEI": "984500BA390DEEC8A198"},
        {"LegalName": "SFN Cleantech Investment Ltd", "LEI": "5299001U27KH2TE1HA16"},
        {
            "LegalName": "SBG CLEANTECH PROJECTCO PRIVATE LIMITED",
            "LEI": "335800L6KBRBMN23G491",
        },
        {
            "LegalName": "SBG CLEANTECH ENERGY EIGHT PRIVATE LIMITED",
            "LEI": "33580025O3MECVXEXN20",
        },
        {
            "LegalName": "SBG CLEANTECH PROJECTCO FIVE PRIVATE LIMITED",
            "LEI": "335800VKNBX6UT5XTA61",
        },
        {"LegalName": "AMPL CLEANTECH PRIVATE LIMITED", "LEI": "3358003BN2TSHLZFK835"},
        {"LegalName": "TATA CLEANTECH CAPITAL LIMITED", "LEI": "335800VHGHY6ACK4EV23"},
        {
            "LegalName": "OPEN CLEANTECH INCOME SECURITIES DAC",
            "LEI": "635400RZAFJOB3F3HO02",
        },
        {
            "LegalName": "ACME CLEANTECH SOLUTIONS PRIVATE LIMITED",
            "LEI": "335800Y9QOUKCKEBDN64",
        },
        {"LegalName": "FFG - CLEANTECH II", "LEI": "549300BOYS2N4DQ86621"},
        {"LegalName": "Ikaros Cleantech AB", "LEI": "529900F3ILO82OOHJ624"},
        {"LegalName": "ARENKO CLEANTECH LIMITED", "LEI": "213800XJAKB99U6GYE81"},
        {
            "LegalName": "CHORUS CleanTech PP Life GmbH & Co. 8. KG",
            "LEI": "39120001P89AEAGP4C95",
        },
        {
            "LegalName": "Vierte Cleantech Infrastrukturgesellschaft mbH",
            "LEI": "391200MHC20BINNZSM38",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Vilseck KG",
            "LEI": "39120001CK4NXMUXLH16",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Vilseck KG",
            "LEI": "39120001CK4NXMUXLH82",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Bockelwitz KG",
            "LEI": "39120001IO1IEBNJB658",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Bockelwitz KG",
            "LEI": "39120001IO1IEBNJB640",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Richelbach KG",
            "LEI": "39120001I4DLSGVIED33",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarpark Richelbach KG",
            "LEI": "39120001I4DLSGVIED65",
        },
        {
            "LegalName": "CHORUS CleanTech GmbH & Co. Solarparks Niederbayern KG",
            "LEI": "391200XOFXB6SEDEUE64",
        },
        {
            "LegalName": "Dritte Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200D4IQYJZH3PQV66",
        },
        {
            "LegalName": "Fünfte Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200YSBV1PTJDIVU78",
        },
        {
            "LegalName": "Zweite Cleantech Infrastrukturgesellschaft mbH & Co. KG",
            "LEI": "391200B0QA2GDAGUWL36",
        },
        {"LegalName": "Kentara Cleantech S.à r.l.", "LEI": "549300O1LH5FYDMNBI61"},
        {
            "LegalName": "TRINITY CLEANTECH PRIVATE LIMITED",
            "LEI": "3358007KMDXWXRDRLJ07",
        },
        {"LegalName": "FUNDO EDP CLEANTECH FCR", "LEI": "529900YNVY87YJXQQL73"},
        {"LegalName": "CAPRICORN CLEANTECH FUND", "LEI": "5493000VTLH53534F243"},
        {
            "LegalName": "SBSR POWER CLEANTECH ELEVEN PRIVATE LIMITED",
            "LEI": "335800PDQXWJSCUT1763",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure Fund SICAV",
            "LEI": "391200IW2I7VHRGVL291",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure (Czech) a.s.",
            "LEI": "391200SNUDPCVPZHNT11",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure Holding GmbH",
            "LEI": "391200RVK5MPKRZEMA60",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure Asia Holding GmbH",
            "LEI": "39120062GAN8OFYXWW72",
        },
        {
            "LegalName": "ThomasLloyd Cleantech Infrastructure (Liechtenstein) AG",
            "LEI": "391200KABA0XCWJDTK89",
        },
        {
            "LegalName": "Desjardins SocieTerra Cleantech Fund",
            "LEI": "54930032H86FEEE8KT71",
        },
        {
            "LegalName": "INVESCO EXCHANGE-TRADED FUND TRUST - Invesco Cleantech ETF",
            "LEI": "549300O3D3IUFT3CTM23",
        },
    ]
