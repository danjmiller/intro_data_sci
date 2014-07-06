import sys
import json



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

        if 'text' in tweet:
            tweets.append(tweet['text'])

    return tweets

#calculate the sentiment of a tweet
def calculate_sentiment(sent_scores, tweets):
    scores = []
    for tweet in tweets:
        score = 0
        words = tweet.split(" ")

        for word in words:
            if word.lower() in sent_scores:
                score += sent_scores[word.lower()]

        scores.append((tweet, score))

    return scores

#helper function that will return 0 if a term isn't known
def get_score(sent_scores, word):
    score = 0;
    if word.lower() in sent_scores:
        score = sent_scores[word.lower()]

    return score

# I'm using a very simple algorithm
# if a term has no score, for every positive tweet it is in, increment a counter, for every negative, decrement
# once this is done for all the tweets, each score is averaged by the number of tweets it appeared in
def findTermSentiment(sent_scores, scored_tweets):
    # the structure of new_terms will be:  {'term', [score, count]}
    new_terms = {}

    for tweet in scored_tweets:
        words = tweet[0].split(" ")

        for word_index in range(len(words)):
            word = words[word_index].lower()  # make lowercase for easier comparison

            if get_score(sent_scores, word) == 0:  # This term is un-scored, try to calculate a sentiment
                if word not in new_terms:
                    new_terms[word] = [0,0] # use a list to represent (score, # of tweets seen in)

                (new_terms[word])[1] += 1 # increment the count because this term has been seen in a tweet
                if tweet[1] > 0:
                    (new_terms[word])[0] += 1
                elif tweet[1] < 0:
                    (new_terms[word])[0] -= 1
                # if the tweet's score is == 0, do nothing
    return new_terms


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_scores = parse_sent_file(sent_file)
    tweets = load_twitter_data(tweet_file)
    scores = calculate_sentiment(sent_scores, tweets)
    new_terms = findTermSentiment(sent_scores, scores)

    for term in new_terms:
        # Take the average of the score/#tweets here
        score = new_terms[term][0] / new_terms[term][1]
        print u"{0} {1}".format(term,score)

if __name__ == '__main__':
    main()
