# python-lei

[![python](https://img.shields.io/pypi/pyversions/python-lei?logo=python&logoColor=white&style=plastic)](https://www.python.org)
[![codecov](https://codecov.io/gh/jdvala/python-lei/branch/master/graph/badge.svg)](https://codecov.io/gh/jdvala/python-lei)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
![Python LEI](https://github.com/jdvala/python-lei/workflows/Python%20LEI/badge.svg)
[![pypi Version](https://img.shields.io/pypi/v/python-lei.svg?logo=pypi&logoColor=white)](https://pypi.org/project/python-lei/)
[![downloads](https://pepy.tech/badge/python-lei)](https://pepy.tech/project/python-lei)


This project is wraper for Leilex, legal entity identifier API. Includes ISIN-LEI conversion. Search LEI number using company name. 

## Dependencies

1. [Python](https://www.python.org/) >= 3.4
2. [requests](http://docs.python-requests.org/en/master/)
3. [dateutils](https://dateutil.readthedocs.io/en/stable/)
4. [pandas](https://pandas.pydata.org/)

## Installation
```bash
pip install python-lei
```

## Usage

After installing the module, first step is to download the data for ISIN and LEI mappings

```python
>>> from python_lei.utils import Download

>>> Download()
```

This will download latest ISIN LEI mappings into resources directory. This is only necessary if you want to use ISIN LEI conversion.

### Get LEI information

```python
>>> from python_lei.pylei import pyLEI

>>> getinfo = pyLEI()

>>> raw_output, lei_results, dataframe = getinfo.get_lei_info(["A23RUXWKASG834LTMK28"], return_dataframe=True)

>>> print(raw_output)

[{'total_record_count': 1,
  'page_number': 1,
  'page_size': 100,
  'total_pages': 1,
  'has_more': False,
  'records': [{'LEI': 'A23RUXWKASG834LTMK28',
    'LegalName': 'AUTOLIV, INC.',
    'LegalJurisdiction': 'US-DE',
    'LegalForm': 'XTIQ',
    'OtherLegalForm': '',
    'EntityStatus': 'ACTIVE',
    'EntityExpirationDate': None,
    'EntityExpirationReason': '',
    'SuccessorEntity': '',
    'InitialRegistrationDate': '2012-06-06T03:52:00.000 +00:00',
    'LastUpdateDate': '2019-12-18T03:32:00.000 +00:00',
    'RegistrationStatus': 'ISSUED',
    'NextRenewalDate': '2020-12-15T10:15:00.000 +00:00',
    'ManagingLOU': 'EVK05KS7XY1DEII3R011',
    'ValidationSources': 'FULLY_CORROBORATED',
    'AssociatedLEI': '',
    'AssociatedEntityName': '',
    'AssociatedEntityType': '',
    'RegistrationAuthorityID': 'RA000602                                ',
    'OtherRegistrationAuthorityID': '',
    'RegistrationAuthorityEntityID': '2155072',
    'EntityCategory': '',
    'Addresses': [{'Line1': 'Box 70381',
      'Line2': '',
      'Line3': '',
      'Line4': '',
      'City': 'Stockholm',
      'Region': 'SE-AB',
      'Country': 'SE',
      'PostalCode': '107 24',
      'OtherType': '',
      'AddressType': 'HEADQUARTERS_ADDRESS'},
     {'Line1': 'C/O THE CORPORATION TRUST COMPANY',
      'Line2': 'CORPORATION TRUST CENTER 1209 ORANGE ST',
      'Line3': '',
      'Line4': '',
      'City': 'WILMINGTON',
      'Region': 'US-DE',
      'Country': 'US',
      'PostalCode': '19801',
      'OtherType': '',
      'AddressType': 'LEGAL_ADDRESS'}],
    'OtherNames': [],
    'ValidationAuthorities': [{'ValidationAuthorityID': 'RA000602',
      'OtherValidationAuthorityID': '',
      'ValidationAuthorityEntityID': '2155072'}],
    'Relationships': [],
    'ReportingExceptions': [{'LEI': 'A23RUXWKASG834LTMK28',
      'ExceptionCategory': 'DIRECT_ACCOUNTING_CONSOLIDATION_PARENT',
      'ExceptionReasons': [{'Reason': 'NON_CONSOLIDATING'}],
      'ExceptionReferences': []},
     {'LEI': 'A23RUXWKASG834LTMK28',
      'ExceptionCategory': 'ULTIMATE_ACCOUNTING_CONSOLIDATION_PARENT',
      'ExceptionReasons': [{'Reason': 'NON_CONSOLIDATING'}],
      'ExceptionReferences': []}]}]}]


# Class based retrieval
>>> print(lei_results.lei_names)
['AUTOLIV, INC.']

>>> print(lei_results.lei_list)
['A23RUXWKASG834LTMK28']

# Dataframe
>>> print(dataframe[["LEI", "Legal_Name"]])
|    | LEI                  | Legal_Name    |
|---:|:---------------------|:--------------|
|  0 | A23RUXWKASG834LTMK28 | AUTOLIV, INC. |
```

### Get LEI-ISIN information

```python
# LEI TO ISIN
>>> from python_lei.isin_lei import ISINtoLEI, LEItoISIN

>>> lei_to_isin = LEItoISIN()

>>> isin_list, dataframe = lei_to_isin.get_isin("A23RUXWKASG834LTMK28", return_dataframe=True)

>>> print(isin_list)
['SE0000382335',
 'US052800AB59',
 'US0528002084',
 'US0528003074',
 'US0528001094',
 'US0528001177']

>>> print(dataframe)
|         | LEI                  | ISIN         |
|--------:|:---------------------|:-------------|
| 1858574 | A23RUXWKASG834LTMK28 | SE0000382335 |
| 2141681 | A23RUXWKASG834LTMK28 | US052800AB59 |
| 2990824 | A23RUXWKASG834LTMK28 | US0528002084 |
| 3450877 | A23RUXWKASG834LTMK28 | US0528003074 |
| 3766379 | A23RUXWKASG834LTMK28 | US0528001094 |
| 4442500 | A23RUXWKASG834LTMK28 | US0528001177 |

# ISIN TO LEI
>> isin_to_lei = ISINtoLEI()

>> lei_number = isin_to_lei.get_lei("US0528003074")

>> print(lei_number)
['A23RUXWKASG834LTMK28']
```

### Search LEI using company name

You can also search for possible LEI numbers for a given company name.

```python
>>> from python_lei.lei_search import SearchLEI
>>> search_possible_lei = SearchLEI()
>>> raw_data, table = search_possible_lei.search_lei("Apple INC.", show_table=True)
>>> print(table)
+------------+----------------------+
| Legal Name | LEI                  |
+------------+----------------------+
| APPLE INC. | HWUPKR0MPOU8FGXBT394 |
+------------+----------------------+
 
>>> print(raw_data)
[{'LegalName': 'APPLE INC.', 'LEI': 'HWUPKR0MPOU8FGXBT394'}]
