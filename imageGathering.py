import flickr_scraper

if __name__ == '__main__':
    search_term = input("Search term: ")
    image_amount = int(input("Download amount: "))
    download_dir = input("Download Directory: ")
    flickr_scraper.get_urls(search_term, download_dir, image_amount, True)
