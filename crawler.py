#!/usr/bin/env python
from validator_collection import checkers
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import os
import time

import gevent


visited = []

def get_url():
    # make sure the user inputs a correct url
    url = input("Please enter the url you wish to spidey crawl: ")
    while not checkers.is_url(url):
        url = input("Please enter a valid url: ")
    return url

def parse_links(current_url, session, limit=False):
    jobs = []
    # get list of urls from the current url
    links = session.get(current_url).html.absolute_links
    filename = f'results.txt'
    with open(filename, 'a') as f:
        # write the link that was fetched
        f.write(current_url + '\n')
        for link in links:
            # make sure url is a vaild one
            if checkers.is_url(link):
                # indent on child links
                f.write('\t' + link + '\n')
            # make sure link is not visted twice
            if link not in visited:
                visited.append(link)
                # geventt jobs are scheduled and ran
                jobs.append(gevent.spawn(parse_links, link, session))
    if limit is True:
        return
    else:
    # wait for jobs to finish
        gevent.joinall(jobs)


def main():
    # delete old result file if there is one
    if(os.path.abspath('results.txt')):
        os.remove(os.path.abspath('results.txt'))
    # Get url from user
    current_url = get_url()
    # iterate over links and write to results.txt
    session = HTMLSession()
    parse_links(current_url, session)

if __name__ == "__main__":
    main()