import requests, bs4, sys, webbrowser

print('Googling...')  # display text while downloading the Google page
res = requests.get('https://search.yahoo.com/search?p=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
file = open('./rawHTML.html', 'wb')

for chunk in res.iter_content():
    file.write(chunk)
soup = bs4.BeautifulSoup(res.text, features="html.parser")
links = soup.select('#results h3 a')

print(links)

numOpen = min(5, len(links))
for i in range(numOpen):
    print(links[i].get('href'))
    webbrowser.open(links[i].get('href'))
