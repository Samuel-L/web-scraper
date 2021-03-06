import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bs4 import BeautifulSoup


def scrape_target_elements(html, target, target_type, specific_tag=''):
    """Scrape target from the html document

    Positional Arguments:
        html (str): standard html document
        target (str): name of tag, id or class
        target_type (str): tag (html element such as <li>, <p>), id or class
    Keyword Arguments:
        specific_tag (str): if target_type is id or class, this keyword argument
            can be used to only scrape targets with this html tag
    Return:
        bs4.element.ResultSet: all scraped targets
    """
    soup = BeautifulSoup(html, 'html.parser')
    if target_type == 'tag':
        return soup.find_all(target)
    else:
        return soup.find_all(specific_tag, attrs={target_type: target})


def scrape_links(domain_name, html):
    """Scrape all links from the html document

    Positional Arguments:
        domain_name (str): the domain name of the website you're scraping
        html (str): standard html document
    Return:
        list: all scraped links
    """
    soup = BeautifulSoup(str(html), 'html.parser')
    link_list = []
    for link in soup.find_all('a'):
        link = link.get('href')

        # If link only includes a path to a page on the website (internal link),
        # add the domain name here.
        if domain_name not in link:
            link = f'{domain_name}{link}'

        link_list.append(link)

    return link_list
