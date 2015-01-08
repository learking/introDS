import sys
import json

def hw(tweet_lines):
    freqs = {} # initialize an empty dictionary
    for line in tweet_lines:
        tmpLine = json.loads(line)
        if "text" in tmpLine.keys():
            tmpTweet = tmpLine["text"]    
            tmpWords = tmpTweet.rstrip().split()
            for tmpW in tmpWords:
                if tmpW in freqs.keys():
                    	freqs[tmpW] += 1
            	else:
			freqs[tmpW] = 1
    allTermsNumber = len(freqs.keys())
    for key in freqs.keys():
	print(key + " " + str(freqs[key]/allTermsNumber))

def main():
    tweet_file = open(sys.argv[1])
    tweet_lines = tweet_file.readlines()
    tweet_file.close()
    hw(tweet_lines)

if __name__ == '__main__':
    main()
