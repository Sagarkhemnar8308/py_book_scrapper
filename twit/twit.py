import snscrape.modules.twitter as sntwitter

# Create a scraper for the hashtag
scraper = sntwitter.TwitterSearchScraper('#flutter')

# Iterate through the scraped tweets
for tweet in scraper.get_items():
    # Just break after the first tweet to test if it's working
    print(tweet)
    break
