from api.services.requests import fetch
from api.scripts.yahoo_data import parse_financial, extract_value_data
from api.models.request_model import RequestComponent


def scrape_statement(symbol: str, website: str) -> dict:
    """

    """

    if website == "yahoo":
        url = "https://ca.finance.yahoo.com/quote/{}/financials?p={}".format(symbol, symbol)
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
        params = {}
        packet = RequestComponent(url=url, headers=headers, params=params)

        html_text = fetch(packet)
        unstructured_object = parse_financial(html_text)
        formatted_object = extract_value_data(unstructured_object)

        return formatted_object

    return {"Message": "The website input have no scraping script for it."}
