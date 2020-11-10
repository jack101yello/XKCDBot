def search(searchTerm): # Returns the search results for the search term
    term = getFixedString(searchTerm.strip())
    return 'https://cse.google.com/cse?cx=012652707207066138651%3Azudjtuwe28q&ie=UTF-8&q=' + term + '&sa=Search#gsc.tab=0&gsc.q=chicken'

def getFixedString(str): # Converts the string to the searchable form
    return str.replace(' ', '+')