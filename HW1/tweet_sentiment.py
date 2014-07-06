import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def parse_sent_file(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    return scores

def load_twitter_data(tweet_file):
    tweets = []

    for line in tweet_file:
        tweet = json.loads(line)

        if tweet.has_key('text'):
            tweets.append(tweet['text'])

    return tweets


def calculate_sentiment(sent_scores, tweets):

    scores = []
    for tweet in tweets:
        score = 0
        words = tweet.split(" ")

        for word in words:
            if sent_scores.has_key(word.lower):
                score += sent_scores[word.lower]

        scores.append(score)


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_scores = parse_sent_file(sent_file)
    tweets = load_twitter_data(tweet_file)

    print "Got %d tweets",len(tweets)
    print scores

if __name__ == '__main__':
    main()
