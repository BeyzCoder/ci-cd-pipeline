from bs4 import BeautifulSoup
from typing import Dict, List
from decimal import Decimal
import ast
import re

# Constant variable.
CONVERSION_MILLION = (10 ** 6)
MAX_YEAR = 10


def parse(text: str) -> List[Dict]:
    """
    Grab the json data from the web page that was dynamically loaded from
    the javascript function.

    Read html parser only and gives raw data.

    @param text: The HTML text from an HTTP requests get.
    @return: Raw data from the HTML text website.
    """
    soup = BeautifulSoup(text, "html.parser")

    # Create a regular expression to search the variable that holds the data.
    search_pattern = re.compile(r'\boriginalData\s*=\s*(\[\{.*?\}\])\s*;\s*\n')

    # Find the data from the HTML script tag.
    script = soup.find(text=search_pattern)
    if script is None:
        raise ValueError("The web page text does not have the source.")

    # Grab the string and convert it into python collection data type.
    matched = search_pattern.search(script).group(1)
    convert_value = ast.literal_eval(matched)

    return convert_value


# TODO: Must not just depend on parse() return value.
# args* the un-needed key-value pair.
# kwargs* different number conversion.
# - what would be the placeholder for empty value.
def cleanse(raw_data: List[Dict]) -> Dict:
    """
    Remove unecessary data and fixed the field_name value and change the data type
    of value to arithematic type.

    Change the format of the raw_data for analytics and logical problem.

    @param raw_data: A raw data that came return value of parse() function.
    @raise KeyError: If ever the criteria_info does not have field_name.
    @return: dict data that are only key-value pair needed.
    """
    clean_data = {}

    # To be use in mapping.
    def convert_type(value: str) -> int:
        if value != "":
            return Decimal(str(round(float(value) * CONVERSION_MILLION, 2)))
        return 0

    for criteria_info in raw_data:
        try:
            # Grab the label in html skeleton.
            name = criteria_info.pop("field_name").replace("<\\/a>", "").replace(r"<\/span>", "").split(">")[-1].replace(" ", "-").replace("\\/", "/")

            # Remove uncessary data.
            del criteria_info['popup_icon']

            # Split the key and value.
            keys_year = list(criteria_info.keys())
            values_cash = list(criteria_info.values())

            # Shorten the years to 10.
            if (len(values_cash) >= MAX_YEAR) and (len(keys_year) >= MAX_YEAR):
                keys_year = keys_year[:MAX_YEAR]
                values_cash = values_cash[:MAX_YEAR]

            # Turn string number to float type and combine the year and cash.
            fixed_number = list(map(convert_type, values_cash))
            years_data = dict(zip(keys_year, fixed_number))

            clean_data[name] = years_data

        except KeyError:
            raise KeyError("The criteria_info might not have one of these key [field_name, popup_icon]")

    return clean_data
