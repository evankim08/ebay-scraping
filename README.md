# ebay Scraping

## I.  Description

In this project, I created a Python file named `ebay-dl.py` to scrape through ebay . The program utilizes the `bs4`, `argparse`, and `requests` libraries in order to loop through ebay's HTML files for a user-inputted search term. Using CSS selectors, specific pieces of listing information are pulled into dictionary entries. Each respective dictionary is appended into a list denoted as `items`.

Then, the `json` and `csv` libraries are used in order to convert the compiled data into the desired type. 

## II.  How to Run the File

1. Open `ebay-dl.py` in your respective code editor.
2. Run the program using the following command in the terminal:
 ```  
 $ python3 ebay-dl.py 'Xbox Series X' 
 ```  
3. This will generate a **JSON** file that contains the listing information one would obtain by searching _Xbox Series X_ on ebay. To generate a JSON file for a different search term, such as _Szechuan Sauce_, we replace the `search_term` in the command as follows:

```
 $ python3 ebay-dl.py 'Szechuan Sauce'
```
4. Likewise, to generate a JSON file for _Adidas Brazuca_ , we replace the `search_term` once more:

```
 $ python3 ebay-dl.py 'Adidas Brazuca'
```
  
5. By default, `ebay-dl.py` program will loop through and extract data from the first 10 ebay webpages for each inputted `search_term`. To change this, we add a new command line flag `--num_pages`. For example, to loop through the first 20 pages for _Adidas Brazuca_ we adjust the command such that:

```
 $ python3 ebay-dl.py 'Adidas Brazuca' --num_pages=20
```

6. Similarly, to generate a **CSV** file, we add a new command line flag `--csv`. This flag can be used in addition to `--num_pages`, although this is not necessary. For example, to generate a CSV file for the first 20 pages of the `search_term` _Adidas Brazuca_ our command line code should look similar to:

```
 $ python3 ebay-dl.py 'Adidas Brazuca' --num_pages=20 --csv
```
  Alternatively, if we want to return to our default of the first 10 pages, we can omit the `--num_pages` flag such that the command looks like:

```
 $ python3 ebay-dl.py 'Adidas Brazuca' --csv
```

   Again, by default, `ebay-dl.py` will generate a JSON file, so the `--csv` command line flag is only necessary to generate a CSV file. Regardless of the file type    chosen, the newly created file will be stored in your current directory, under the format `search_term.json` or `search_term.csv` . 


##  III. More Information

More information pertaining to the guidelines of this project can be found [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03).



 
