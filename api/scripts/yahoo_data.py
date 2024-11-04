from bs4 import BeautifulSoup

import json
import re


def parse_financial(text: str) -> dict:
    """
    Takes an html text financial webpage from the yahoo finance
    parse the text to grab the financial statements of the stock.

    @param text: HTML text from yahoo finance.
    @return: json data from the html text website.
    """

    soup = BeautifulSoup(text, "html.parser")

    # Parsing the html text to find the data.
    pattern = re.compile(r'\broot.App.main\s*=\s*(\{.*?\})\s*;\s*\n')
    script = soup.find(text=pattern)
    match_string = pattern.search(script).group(1)
    json_value = json.loads(match_string)

    # Parsing the years from the table.
    years_date = soup.find("div", {"class" : "D(tbhg)"}).find_all("span")[2:]   # Remove the first two item

    # Place the list of years in the data.
    format_year_data = json_value
    format_year_data['years_date'] = years_date

    return format_year_data


def extract_value_data(data: dict) -> dict:
    """
    Takes the unstructured data and format to a usable dict object.

    @param data: the parse value from the yahoo finance.
    @return: formatted json object.
    """

    # Get the finacial report records of Income Statement, Balance Sheet, Cash Flow
    income_statement = data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
    balance_statement = data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']
    cash_statement = data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
    years_date = data['years_date']

    extracted_data = {'income-statement' : {}, 'balance-statement' : {}, 'cash-statement' : {}}
    for year, income, balance, cash in zip(years_date, income_statement, balance_statement, cash_statement):
        text_year = year.text

        # Income statement.
        income_norm = {key : (value['raw'] if value and isinstance(value, dict) else value) for key, value in income.items()}
        extracted_data['income-statement'].update({text_year : income_norm})

        # Balance statement.
        balance_norm = {key : (value['raw'] if value and isinstance(value, dict) else value) for key, value in balance.items()}
        extracted_data['balance-statement'].update({text_year : balance_norm})

        # Cash statement.
        cash_norm = {key : (value['raw'] if value and isinstance(value, dict) else value) for key, value in cash.items()}
        extracted_data['cash-statement'].update({text_year : cash_norm})

    return extracted_data
