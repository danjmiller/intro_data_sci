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


def get_score(sent_scores, word):
    score = 0;
    if word.lower() in sent_scores:
        score = sent_scores[word.lower()]

    return score

# This method will return the sentiment scores of the words adjacent to the target word, or 0 if they aren't scored
def get_adjacent_scores(sent_scores, words, index):
    adjacents = [0, 0]

    if len(words) > 1:
        if index == 0:  # first element
            adjacents[0] = get_score(sent_scores, words[1])
        if index == (len(words) - 1):  # last element
            adjacents[1] = get_score(sent_scores, words[index - 1])
        else:
            adjacents[0] = get_score(sent_scores, words[index - 1])
            adjacents[1] = get_score(sent_scores, words[index + 1])

    return adjacents


def findTermSentiment(sent_scores, scored_tweets):
    new_terms = {}

    for tweet in scored_tweets:
        words = tweet[0].split(" ")

        for word_index in range(len(words)):
            word = words[word_index].lower()  # make lowercase for easier comparison

            if get_score(sent_scores, word) == 0:  # This term is un-scored, try to calculate a sentiment
                if word not in new_terms:
                    new_terms[word] = 0

                # get the scores for the words adjacent to the word
                adjacent = get_adjacent_scores(sent_scores, words, word_index)

                if adjacent[0] > 0 and adjacent[1] > 0 and tweet[1] > 0:
                    new_terms[word] += 1
                elif adjacent[0] < 0 and adjacent[1] < 0 and tweet[1] < 0:
                    new_terms[word] -= 1

    return new_terms


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_scores = parse_sent_file(sent_file)
    tweets = load_twitter_data(tweet_file)
    scores = calculate_sentiment(sent_scores, tweets)
    new_terms = findTermSentiment(sent_scores, scores)

    for term in new_terms:
        print u"{0} {1}".format(term, new_terms[term])

if __name__ == '__main__':
    main()
