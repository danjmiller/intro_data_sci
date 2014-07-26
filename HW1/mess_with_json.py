import sys
import json
import urllib


def main():
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi"

    response = urllib.urlopen(url)
    tweet = json.load(response)
    print tweet

if __name__ == '__main__':
    main()
