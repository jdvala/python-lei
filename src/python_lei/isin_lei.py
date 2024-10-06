from python_lei.exceptions import InvalidISIN, InvalidLEI
from python_lei.utils import load_data


class LEItoISIN:
    """
    Get ISIN from corresponding LEI
    """

    def __init__(self):
        self.dataframe = load_data()

    def get_isin(self, lei, return_dataframe=False):
        """
        Get all the possible ISIN numbers for a LEI
        """
        if len(lei) != 20:
            raise InvalidLEI("Invalid LEI number")

        isin_dataframe = self.dataframe[self.dataframe["LEI"] == lei]

        isin_list = isin_dataframe["ISIN"].tolist()

        if return_dataframe:
            return isin_list, isin_dataframe

        return isin_list


class ISINtoLEI:
    """
    Get LEI from corresponding ISIN
    """

    def __init__(self):
        self.dataframe = load_data()

    def get_lei(self, isin):
        """
        Get all the possible ISIN numbers for a LEI
        """
        if len(isin) != 12:
            raise InvalidISIN("Invalid ISIN number")

        lei_dataframe = self.dataframe[self.dataframe["ISIN"] == isin]

        lei_list = lei_dataframe["LEI"].tolist()

        return lei_list
