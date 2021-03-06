import sys
import json

def hw(sent_lines, tweet_lines):
    scores = {} # initialize an empty dictionary
    for line in sent_lines:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_lines:
        tmpLine = json.loads(line)
        if "text" in tmpLine.keys():
            tmpTweet = tmpLine["text"]    
            tmpWords = tmpTweet.rstrip().split()
            tmpScore = 0
            for tmpW in tmpWords:
                if tmpW in scores.keys():
                    tmpScore += scores[tmpW]
	    for tmpW in tmpWords:
		if tmpW not in scores.keys():
	            print(tmpW + " " + str(tmpScore))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_lines = sent_file.readlines()
    tweet_lines = tweet_file.readlines()
    sent_file.close()
    tweet_file.close()
    hw(sent_lines, tweet_lines)

if __name__ == '__main__':
    main()
