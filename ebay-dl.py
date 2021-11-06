import requests
import argparse
from bs4 import BeautifulSoup
import json
import csv

def parse_itemssold(text):
    
    '''
    Takes as input a string and return the number of items sold, as specified in the string.

    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return None

def parse_price(text):

    '''
    >>> parse_price('$3.00 to $5.39')
    300
    >>> parse_price('$123.40')
    12340
    >>> parse_price('$23.46')
    2346
    '''
    newtext = ''
    newprice = ''

    if 'to' in text:
        splittext = text.split('to', 1)
        newprice = splittext[0]
    
        for char in newprice:
            if char == '.':
                newtext += ''
            elif char == ',':
                newtext += ''
            else:
                newtext += char
    else:
        for char in text:
            if char == '.':
                newtext += ''
            elif char == ',':
                newtext += ''
            else:
                newtext += char
    
    return int(newtext[1:])

def parse_shipping(text):
    '''
    >>> parse_shipping('+$15.95 shipping estimate')
    1595
    >>> parse_shipping('Free shipping')
    0
    >>> parse_shipping('+$9.35 shipping')
    935
    '''

    if 'Free' in text:
        return 0

    if 'not specified' in text:
        return None

    else:
        newtext = ''
        for char in text:
            if char == '.':
                newtext += ''
            elif char == '+':
                newtext += ''
            else:
                newtext += char
        newtext = newtext.replace('shipping','')
        newtext = newtext.replace('estimate','')

    return int(newtext[1:])

# This if statement says only run the code below when the python file is run "normally"
if __name__ == '__main__':

    # ----- PART I -----

    # 1. Use the argparse library to get a search term from the command line

    # Get command line arguments
    parser = argparse.ArgumentParser(description = 'Download information from eBay and conver to JSON.')
    parser.add_argument('search_term', help = 'Search term inputted into eBay search bar.')
    parser.add_argument('--num_pages', default = 10)
    parser.add_argument('--csv', action = 'store_true')
    args = parser.parse_args()
    print('args.search_term =', args.search_term)

    # 2. Use the requests library to download the first 10 webpage results for your search term

    # List of all items found in all eBay webpages
    items = []

    # Loop over the eBay webpages
    for page_number in range(1,int(args.num_pages)+1):

        # Build the URL
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
        url += args.search_term
        url +='&_sacat=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
    #    print('url=', url)

        # Download the HTML (recall that status = 200 is a success)
        r = requests.get(url)
        status = r.status_code
    #    print('status=', status)
        html = r.text

    # 3. Use bs4 to extract all of the items returned in the search results
    # 4. Create a python list of the extracted items, where each entry in the list is a dictionary.

        # Process the HTML
        soup = BeautifulSoup(html, 'html.parser')

        #Loop over the items in the page
        tags_items = soup.select('.s-item')

        for tag_item in tags_items:

            # To get each tag (containing item title) on its own line, to get content of the HTML tag we use tag.text
            
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)

            price = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                price = parse_price(tag.text)

            status = None
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text

            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)

            item = {
                'name' : name,
                'price' : price,
                'status' : status,
                'shipping' : shipping,
                'free_returns' : freereturns,
                'items_sold' : items_sold,
            }
            items.append(item)

    #print('len(tags_items)=', len(tags_items))
    #print('len(items)=', len(items))

 # 5. Use the JSON library to save the list as a JSON file named search_term.json, where search_term should be replaced by the term passed in on the command line
 # -----EXTRA CREDIT----- Generate CSV files when the command line flag is specified
 
    if args.csv == True:
        filename = args.search_term +'.csv'
        with open(filename,'w', newline ='') as f:
            fieldnames = ['price', 'status', 'items_sold', 'shipping', 'name', 'free_returns']
            csvwriter = csv.DictWriter(f, fieldnames = fieldnames)
            csvwriter.writeheader()
            for element in items:
                csvwriter.writerow(element)

    else:
        filename = args.search_term +'.json'
        with open(filename, 'w', encoding = 'ascii') as f:
            f.write(json.dumps(items))