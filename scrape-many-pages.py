import requests
from bs4 import BeautifulSoup
import re
import time
from colorama import Fore, Back


def scrapwords():
    starting_url = input(Fore.CYAN + Back.BLACK + 'Enter the starting URL: ')
    word_length = int(input(Fore.CYAN + Back.BLACK +
                            'Enter the word min length to search for: '))
    max_depth = int(input(Fore.CYAN + Back.BLACK +
                    'Enter the maximum depth to crawl: '))
    links_to_crawl = [(starting_url, 1)]
    while links_to_crawl:
        url, depth = links_to_crawl.pop(0)
        if depth > max_depth:
            continue
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            words = []
            for string in soup.stripped_strings:
                words.extend(re.findall(r'\b\w+\b', string.lower()))
            long_words = [word for word in words if len(word) >= word_length]
            print(Fore.GREEN + Back.BLACK +
                  f'Found {len(long_words)} words of length {word_length} on {url}')
            links = []
            for link in soup.find_all('a'):
                href = link.get('href')
                if href and href.startswith('http'):
                    links.append(href)
                    print(Fore.YELLOW + f'Found link: {href}')
            with open('words.txt', 'a') as f:
                f.write('\n'.join(long_words) + '\n')
            links_to_crawl.extend([(link, depth+1) for link in links])
            print(Fore.GREEN + Back.BLACK +
                  f'Added {len(links)} links to crawl from {url}')
        except Exception as e:
            print(Fore.RED + Back.BLACK +
                  f'Error while processing {url}: {e}')
        time.sleep(1)  # add delay to avoid being blocked by the website
    print(Fore.GREEN + Back.BLACK + 'Done crawling.')


if __name__ == "__main__":
    scrapwords()