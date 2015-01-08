import sys
import json

def hw(tweet_lines):
    freqs = {} # initialize an empty dictionary
    for line in tweet_lines:
        tmpLine = json.loads(line)
        if "text" in tmpLine.keys():
            tmpHashtags = tmpLine["entities"]["hashtags"]
            for tmpHashtag in tmpHashtags:
                if "text" in tmpHashtag.keys():
                    tmpH = tmpHashtag["text"]
                    if tmpH in freqs.keys():
                        freqs[tmpH] += 1
                    else:
                        freqs[tmpH] = 1
    sortedList = sorted(freqs, key=freqs.get, reverse = True)
    for i in range(10):
        print(sortedList[i] + " " + str(freqs[sortedList[i]]))


def main():
    tweet_file = open(sys.argv[1])
    tweet_lines = tweet_file.readlines()
    tweet_file.close()
    hw(tweet_lines)

if __name__ == '__main__':
    main()
