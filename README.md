# Receipts-dates-extractor

* Expense date (also called spend date) is the exact date on which a financial transaction or operation has happened and must be recognized in the accounting system.

* The format of expense dates vary across merchants and the country of issue. In a few cases, the expense date may not be present in the receipt.

* In this project, built a RESTful API using Flask. This repo contain preprocess.py file used to preprocess images for better optical recognition task like convert images to DPI of (300,300) & extract_dates.py convert images of receipts to text using google vision api and then by some preprocess steps extract date from text given by vision api and stores in pandas DataFrame.

* Finally build a RESTful API using flask - See script.py file for more API details.

## API Link : https://receipts-info.herokuapp.com/

* This API takes single or multiple images of receipts, bills, tax-invoice as input and return a pandas DataFrame contain dates of input images.
* You can give maximum of 100 images at a time.
