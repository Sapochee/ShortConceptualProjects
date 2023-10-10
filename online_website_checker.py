"""Checks if an inputted website is able to be connected to or not
"""

import urllib.request as urllib

def main(url):
    print("")
    response = urllib.urlopen(url)
    print("Connection to ", url, " successful")
    print("Response code: ", response.getcode())
    
#input as https://www.[insert website].[insert domain]
input_url = input("Input the url of the site to check its connectivity: ")
main(input_url)