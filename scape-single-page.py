from bs4 import BeautifulSoup
import requests
from colorama import Back, Fore

# URL to scrape
url = input(Fore.BLACK + Back.WHITE + "Enter the URL to scrape: \n")

# get user input for minimum word length
min_length = int(input(Fore.BLACK + Back.WHITE + "Enter the minimum length of words to keep: "))

# create an empty list to store all the words
all_words = []

# send a request to the webpage and get the HTML content
response = requests.get(url)
html_content = response.text

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# extract all the text from anchor tags, div tags
text = soup.get_text()

# split the text into words
words = text.split()

# add the words to all_words list if they meet the minimum length and are just words
for word in words:
    if len(word) >= min_length and word.isalpha():
        all_words.append(word.lower())

# open the file in append mode
with open('words.txt', 'a') as file:
    for word in all_words:
        file.write(word + '\n')

print(Fore.BLACK + Back.WHITE + f'{len(all_words)} words saved to words.txt')
