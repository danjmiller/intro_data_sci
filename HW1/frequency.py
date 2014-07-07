import sys
import json

def load_twitter_data(tweet_file):
    tweets = []

    for line in tweet_file:
        tweet = json.loads(line)

        if 'text' in tweet:
            tweets.append(tweet['text'])

    return tweets

def calculate_term_freq(tweets):
    counts = {}
    total_terms = 0

    for tweet in tweets:
        words = tweet.split(" ")
        total_terms += len(words)

        for word in words:
            word = word.replace("\n"," ")  # Need to do this because the newlines in some tweets messed up printing
            if word.lower() not in counts:
                counts[word.lower()] = 1
            else:
                counts[word.lower()] += 1

    freqs = []
    for term in counts:
        freqs.append((term, float(float(counts[term])/float(total_terms))))

    return freqs

def main():

    tweet_file = open(sys.argv[1])
    tweets = load_twitter_data(tweet_file)

    freqs = calculate_term_freq(tweets)

    for term in freqs:
        print u"{:s} {:03.4f}".format(term[0].strip(), term[1])



if __name__ == '__main__':
    main()
