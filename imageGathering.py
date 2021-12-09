import flickr_scraper

if __name__ == '__main__':
    search_term = input("Search term: ")
    image_amount = int(input("Download amount: "))
    flickr_scraper.get_urls(search_term, n=image_amount, download=True)
