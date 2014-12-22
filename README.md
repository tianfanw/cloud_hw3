# COMS6998 Homework3 Tweet Sentiment Analysis
=============================

## Steps
1. First we use the sample word count mapper on EMR to get a list of words with frequencies.

2. Then we run another map reduce job to sort these words based on their values(frequencies) and from the result we can inspect what words are more popular and manually select a word as the topic for further analysis(we chose the word "school" as our topic).

3. Next we split the original tweet data equally into ten pieces, each representing the tweets for a single day assuming the tweets were delivered uniformly.

4. Then for each piece of data we run a map reduce job to get the word count of all the words that appear in tweets related to the topic "school".

5. Again we sort the result by frequencies.

6. Now we have a list of words sorted by their frequencies for each day, we then look them up in the sentiment dictionary(Downloaded from http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html) to assign the sentiment to those words. We skip those words that don't appear in the dictionary since they're meaningless. For each day we only count the first thirty most frequent meaningful words.

7. We then use wordle applet to generate a wordle graph for each day. We also calculate the overall sentiment by taking the sum of the count of the thirty words multiplied by their sentiment values, and thenuse highcharts.js to display them.
