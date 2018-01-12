import requests


def get_data_from_enre():
    raw = requests.get(
        "http://www.enre.gov.ar/web/web.nsf/inicio_Edesur?openform"
    )
    if raw.status_code == 200:
        return raw.text
    else:
        return None
