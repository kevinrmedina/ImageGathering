import flickr_scraper
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', type=str, help='flickr search term') 
    parser.add_argument('-n', type=int, help='number of images')
    parser.add_argument('-d', type=str)
    opt = parser.parse_args()

    if(opt.search == None):
        search_term = input("Search term: ")
    else:
        search_term = opt.search

    if(opt.n == None):
        image_amount = int(input("Download amount: "))
    else:
        image_amount = int(opt.n)

    if(opt.d == None):
        download_dir = input("Download Directory: ")
    else:
        download_dir = opt.d
    
    flickr_scraper.download_images(search_term, download_dir, image_amount)
