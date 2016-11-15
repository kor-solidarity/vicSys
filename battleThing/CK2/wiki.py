import wikipedia

korea = wikipedia.page('List of members of the National Assembly (South Korea), 2016–present')

print(korea.categories)
print(korea.section('Lists of South Korean politicians'))

names = [ tr('td')[2].text for table in soup.find_all('table', 'sortable') for tr in table('tr')[1:] ]