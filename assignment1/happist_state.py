import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

realStates = {v:k for k, v in states.items()}

stateSent = {
        'AK': [],
        'AL': [],
        'AR': [],
        'AS': [],
        'AZ': [],
        'CA': [],
        'CO': [],
        'CT': [],
        'DC': [],
        'DE': [],
        'FL': [],
        'GA': [],
        'GU': [],
        'HI': [],
        'IA': [],
        'ID': [],
        'IL': [],
        'IN': [],
        'KS': [],
        'KY': [],
        'LA': [],
        'MA': [],
        'MD': [],
        'ME': [],
        'MI': [],
        'MN': [],
        'MO': [],
        'MP': [],
        'MS': [],
        'MT': [],
        'NA': [],
        'NC': [],
        'ND': [],
        'NE': [],
        'NH': [],
        'NJ': [],
        'NM': [],
        'NV': [],
        'NY': [],
        'OH': [],
        'OK': [],
        'OR': [],
        'PA': [],
        'PR': [],
        'RI': [],
        'SC': [],
        'SD': [],
        'TN': [],
        'TX': [],
        'UT': [],
        'VA': [],
        'VI': [],
        'VT': [],
        'WA': [],
        'WI': [],
        'WV': [],
        'WY': []
}

statesList = ["Washington","Wisconsin","West Virginia","Florida","Wyoming","New Hampshire","New Jersey","New Mexico","National","North Carolina","North Dakota","Nebraska","New York","Rhode Island","Nevada","Guam","Colorado","California","Georgia","Connecticut","Oklahoma","Ohio","Kansas","South Carolina","Kentucky","Oregon","South Dakota","Delaware","District of Columbia","Hawaii","Puerto Rico","Texas","Louisiana","Tennessee","Pennsylvania","Virginia","Virgin Islands","Alaska","Alabama","American Samoa","Arkansas","Vermont","Illinois","Indiana","Iowa","Arizona","Idaho","Maine","Maryland","Massachusetts","Utah","Missouri","Minnesota","Michigan","Montana","Northern Mariana Islands","Mississippi"]

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
            tmpLoc_raw = tmpLine["user"]["location"]
	    for st in statesList:
		if st.lower() in tmpLoc_raw.lower():
                    #print(tmpLoc_raw)
                    #print(stateSent[realStates[st]])
                    stateSent[realStates[st]].append(tmpScore)
                    #print(stateSent[realStates[st]])
    stateResult = {}
    for key in stateSent.keys():
        tmpScoreList = stateSent[key]
        if(len(tmpScoreList) > 0):
            tmpAveScore = sum(tmpScoreList) / len(tmpScoreList)
            stateResult[key] = tmpAveScore
            #print(key + " " + str())
            #print(tmpScore)
    sortedResult = sorted(stateResult, key=stateResult.get, reverse = True)
    print(sortedResult[0])

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
