import requests
from requests.exceptions import ConnectionError, MissingSchema

def return_html(url):
    """Fetch html from url and return html

    :param str url: an address to a resource on the Internet
    :return: the html fetched from the url
    :rtype: str
    """
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            return res.text # html
        else:
            return res.status_code
    except Exception as err:
        return err


if __name__ == '__main__':
    pass
