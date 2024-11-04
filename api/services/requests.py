from api.models.request_model import RequestComponent
from urllib.error import HTTPError

import requests


def fetch(packet: RequestComponent) -> str:

    response = requests.get(**packet.__dict__)

    if response.status != 200:
        raise HTTPError(response.url, response.status_code, "", response.headers, None)

    return response.text
