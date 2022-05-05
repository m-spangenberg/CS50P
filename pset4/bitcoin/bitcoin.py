import requests

# let the user specify how many bitcoins with sys.argv
# if the user's input cannot be converted to a float, enforce sys.exit
# query https://api.coindesk.com/v1/bpi/currentprice.json for bitcoin prices
# parse the json returned by requests -- print(f"${amount:,.4f}")
# docs.python-requests.org/en/latest/user/quickstart/#make-a-request
# docs.python-requests.org/en/latest/user/quickstart/#json-response-content
# get the current price of bitcoin as a float from the returned json
# output the cost of n bitcoins in USD to four decimal places using ',' as a thousands seperator
# https://docs.python.org/3/library/string.html#formatspec

# $ python bitcoin.py                                                             
# Missing command-line argument                                                   
# $ python bitcoin.py cat                                                         
# Command-line argument is not a number                                           
# $ python bitcoin.py 1                                                           
# $38,761.0833    


try:
    pass
except requests.RequestException:
    pass