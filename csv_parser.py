import re

"""
Reads the csv dataset available at data-csv and splits it into two files (.pos and .neg) containing the positive and negative tweets.
Does some word preprocessing during the parsing.
"""
try:
	full_dataset = open("data-csv/twitter-raw-data.csv", "r")
	pos_dataset = open("data-csv/tw-data.pos", "w")
	neg_dataset = open("data-csv/tw-data.neg", "w")
	neu_dataset = open("data-csv/tw-data.neu", "w")
except:
	print "Failed to open file"
	quit()

csv_lines = full_dataset.readlines()
i=0.0

for line in csv_lines:
	i += 1.0
	line = line.split(",")
	tweet = line[3].strip()
	new_tweet = ''

	print "{0:.0f}%".format((i/len(csv_lines)) * 100)

	for word in tweet.split():
		# String preprocessing
		if re.match('^.*@.*', word):
			word = '<NAME/>'
		if re.match('^.*http://.*', word):
			word = '<LINK/>'
		word = word.replace('#', '<HASHTAG/> ')
		word = word.replace('&quot;', ' \" ')
		word = word.replace('&amp;', ' & ')
		word = word.replace('&gt;', ' > ')
		word = word.replace('&lt;', ' < ')
		new_tweet = ' '.join([new_tweet, word])

	tweet = new_tweet.strip() + '\n'
	print(i)
	if line[4].strip() == 'positif':
		pos_dataset.write(tweet)
	elif line[4].strip() == 'negatif':
		neg_dataset.write(tweet)
	else:
		neu_dataset.write(tweet)
