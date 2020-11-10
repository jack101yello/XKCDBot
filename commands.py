import requests
from search import *

def get_response(contents): # Determines what response to send
    if contents.strip().isnumeric(): # Runs if a number has been provided
        return getImage(contents.strip())
    elif contents.strip() == 'help': # Runs if the help command is run
        return 'Here are the commands you can use:\n' + 'help - this page\n' + 'current - the most recent XKCD\n' + '<number> - this number XKCD comic\n' + '.search <search term> - searches for a relevant XKCD'
    elif contents.strip() == 'current': # Runs if the current command is run
        return getImage(0)
    elif contents.strip().startswith('.search'): # Runs if the search command is run
        return search(contents[7:])
    else: # Runs if no known command is run
        return 'Sorry, I don\'t know that command. Use !XKCD help to see a list of commands.\nIf you\'re looking for a particular comic, try searching for it on relevant-xkcd.github.io'


def getImage(number): # Returns the URL for the desired comic
    if number == 0:
        downloadFileFrom('https://xkcd.com')
    else:
        downloadFileFrom('https://xkcd.com/' + number)
    return getURLFromHTML()

def downloadFileFrom(URL): # Downloads the HTML file for the webpage for the desired comic
    r = requests.get(URL, allow_redirects=True)
    open('webpage.html', 'wb').write(r.content)

def getURLFromHTML(): # Returns the URL for the image from the HTML webpage for the comic
    f=open('webpage.html')
    lines = f.readlines()
    line = lines[68]
    begin = line.index('"')+3
    end = line.index('"', line.index('"')+1, len(line))
    return "https://" + line[begin:end]
