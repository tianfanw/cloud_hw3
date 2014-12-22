import urllib2
import sys

positive_words_url = "https://s3.amazonaws.com/cloud-hw3-tweet-analysis/dictionary/positive-words.txt"
negative_words_url = "https://s3.amazonaws.com/cloud-hw3-tweet-analysis/dictionary/negative-words.txt"

positive_wordlist = ()
negative_wordlist = ()

f = urllib2.urlopen(positive_words_url)
for line in f.readlines():
    line = line.strip()
    if len(line) > 0:
        if line[0] == ';':
            continue
        positive_wordlist = positive_wordlist + (line,)

f = urllib2.urlopen(negative_words_url)
for line in f.readlines():
    line = line.strip()
    if len(line) > 0:
        if line[0] == ';':
            continue
        negative_wordlist = negative_wordlist + (line,)

if len(sys.argv) < 3:
    print "Please specify the input and output filename"
    sys.exit(1)

count = 0
overall_sentiment = 0
fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
for line in reversed(fin.readlines()):
    line = line.strip().split()
    word = line[0].lower()
    freq = int(line[1])
    if(word in positive_wordlist):
        # print '%s\t%d\t%d' % (word, freq, 1)
        fout.write('%s:%d:%s\n' % (word, freq, 'FF0000'))
        count += 1
        overall_sentiment += freq
    elif (word in negative_wordlist):
        # print '%s\t%d\t%d' % (word, freq, -1)
        fout.write('%s:%d:%s\n' % (word, freq, '0000FF'))
        count += 1
        overall_sentiment -= freq
    if count > 30:
        break
fout.write('\noverall_sentiment = %d\n' % overall_sentiment)
fin.close()
fout.close()

