import urllib
import urllib.parse as urlparse

from bs4 import BeautifulSoup


def simple_crawler(url: str) -> None:
    """
    Crawls URL input to find on-page links, creates list of those, then visits and scrapes those urls for links.
    """

    urls = [url]  # List of urls to scrape
    visited = [url]  # Record of urls crawled

    # Crawl and build list of urls on a page

    while len(urls) > 0:
        try:
            htmltext = urllib.urlopen(urls[0]).read()
        except:
            print(urls[0])

        soup = BeautifulSoup(htmltext)

        urls.pop(0)
        print(len(urls))

        for tag in soup.findAll("a", href=True):
            tag["href"] = urlparse.urljoin(url, tag["href"])
            if url in tag["href"] and tag["href"] not in visited:
                urls.append(tag["href"])

    visited.append(tag["href"])

    print(visited)

    return None


def main():
    simple_crawler(url="http://www.foundryoutdoors.com")


if __name__ == "__main__":
    main()
