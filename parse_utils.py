import json
import urllib2
import re

from BeautifulSoup import BeautifulSoup


def parse_web_csv(loc):
    url_list = []
    try:
        response = urllib2.urlopen(loc, timeout=10)
        content = response.read()
        for row in content.split('\n'):
            url_list.append(row.rstrip('\r\n'))
    except urllib2.URLError as e:
        print type(e)
    # print(content)
    return url_list


def get_one_depth_links(url):
    opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor()
    )
    links = []

    try:
        html_page = opener.open(url)
        soup = BeautifulSoup(html_page)
        print ('processing: ' + str(url))
        for link in soup.findAll(
            'a', attrs={'href': re.compile("^https?://")}
        ):
            links.append(link.get('href'))
    except urllib2.HTTPError, e:
        print ('Error code: ', e.code)
    except urllib2.URLError:
        print ('Error code: URLError')

    return links


def write_dict_as_json(data, fullpath):
    with open((fullpath + '.json'), 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)
    print ('successfully wrote to ' + fullpath)


def load_from_json(fullpath):
    with open(fullpath, 'r') as fp:
        data = json.load(fp)
    return data
