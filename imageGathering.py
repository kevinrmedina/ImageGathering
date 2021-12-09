import flickr_scraper

if __name__ == '__main__':
    search_term = input("Search term: ")
    print(search_term)
    flickr_scraper.get_urls(search_term, n=1, download=True)
