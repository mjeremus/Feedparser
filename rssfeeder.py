import feedparser

def parseRSS(rss_url):
    return feedparser.parse(rss_url)

def getHeadlines(rss_url):
    headlines = []

    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines

allheadlines = []

newsurls = {"CNN": 'http://rss.cnn.com/rss/edition.rss',
            "CNN World": 'http://rss.cnn.com/rss/edition_world.rss',
            "CNN Americas": 'http://rss.cnn.com/rss/edition_americas.rss'}

for key, url in newsurls.items():
    
    allheadlines.extend(getHeadlines(url))

for hl in allheadlines:
    print(hl)