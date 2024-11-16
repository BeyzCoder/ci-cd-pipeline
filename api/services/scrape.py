from api.services.requests import fetch
from api.scripts.macrotrend_data import parse, cleanse
from api.models.request_model import RequestComponent


def scrape_statement(symbol: str, website: str) -> dict:
    """

    """

    if website == "macrotrend":
        url = "https://www.macrotrends.net/stocks/charts/{}//financial-statements".format(symbol)
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
        params = {}
        packet = RequestComponent(url=url, headers=headers, params=params)

        html_text = fetch(packet)
        raw_data = parse(html_text)
        formatted_object = cleanse(raw_data)

        return formatted_object

    return {"Message": "The website input have no scraping script for it."}
