import datetime
import alphaweight
import string
from twitter_bot import weight_value


def parse_tweets(alltweets):
    if alltweets:
        elontweets = open('2021UTF8.csv', 'r', encoding='cp1252').readlines()[1:] # [1:9173]
    else:
        elontweets = open('2021UTF8.csv', 'r', encoding='cp1252').readlines()[1:9173]
    tweet_list = []
    for line in elontweets:
        # line = line.split(',')
        # print(line[34][0:3])
        # if "[{" not in line:
            line = line.split(',')
            # print(line[7].encode('utf8'))
            date_time = line[4]

            if "\"\"" in line[7]:
                tweet = []
                merge = 7
                while "\"\"" not in line[merge][-4:]:
                    tweet.append(line[merge])
                    merge += 1
                tweet.append(line[merge])
                tweet_list.append([toUnix(date_time), " ".join(tweet)])
            else:
                tweet_list.append([toUnix(date_time), line[7]])
            # print(tweet_list[-1])
    return(tweet_list)


def toUnix(date_time):
    # print(date_time)
    date_time = date_time.rsplit(":", 2)[0]
    date_object = datetime.datetime.strptime(date_time, "%Y-%m-%d %H")
    # date_object = date_object + datetime.timedelta(hours=1)
    unix_seconds = int((date_object - datetime.datetime(1970, 1, 1)).total_seconds())
    return(unix_seconds)


def find_btcbalance(unix_timestamp, bitstamp_dict, start, end, hourshift):
    beginvalue = bitstamp_dict[unix_timestamp][start]
    if hourshift:
        unix_timestamp += 3600
    finalvalue = bitstamp_dict[unix_timestamp][end]
    difference = 100 * ((float(finalvalue) - float(beginvalue)) / float(beginvalue))
    return(difference)


def adjust_weights(weightdict, number_of_tweets):
    for i in weightdict.keys():
        weightdict[i] = weightdict[i] / number_of_tweets
    return(weightdict)


def add_weights_to_list(tweet_list, bitstamp_dict, start, end, hourshift):
    weightdict = alphaweight.initialize_weightdict()
    weightkeys = weightdict.keys()
    timestamps = bitstamp_dict.keys()
    # biggest_tweet = 0
    for tweet in tweet_list:
        if tweet[0] in timestamps and tweet[0] + 3600 in timestamps:
            btcdifference = find_btcbalance(tweet[0], bitstamp_dict, start, end, hourshift)
            # print(tweet, btcdifference, flush=True)
            # if abs(btcdifference) > biggest_tweet:
                # print(btcdifference, end=" ")
                # print(tweet[1], flush=True)
                # print()
                # biggest_tweet = abs(btcdifference)
            for letter in tweet[1]:
                if letter in weightkeys:
                    weightdict = alphaweight.addweight(weightdict, tweet[1], btcdifference)
    return(weightdict)


def total_from_dict(weightdict):
    return(sum(list(weightdict.values())))


# bitstamp_start = 1325317920
bitcoin = open('Binanceproper.csv').readlines()[2:]
# print(bitcoin[1].split(',', 3)[3].split(','))
bitstamp_dict = {int(x.split(',', 1)[0]): x.split(',', 3)[3].split(',') for x in bitcoin}

# tweet_list = parse_tweets()
# weightdict = add_weights_to_list(tweet_list, bitstamp_dict)
iterations_alltweets = {"Including 2017": True, "Excluding 2017": False}
iterations_start = {"open": 0, "close": 3}
iterations_end = {"open": 0, "close": 3}
iterations_hour = {"No hour": False, "Add hour": True}

fun_words = ["Bitcoin", "bitcoin", "Elon Musk", "To the moon!", "Dogecoin",
             "Cryptocurrency", "SpaceX", "In retrospect, it was inevitable"]

testword = ""
frequency_list = [82, 15, 28, 43, 13, 22, 2, 61, 70, 2, 8, 40, 24, 67, 75, 19, 1, 60, 63, 91, 28, 10, 24, 2, 20, 1]
for letterindex in range(0, len(string.ascii_lowercase)):
    testword = testword + string.ascii_lowercase[letterindex] * frequency_list[letterindex]

for alltweets in iterations_alltweets.keys():
    tweet_list = parse_tweets(iterations_alltweets[alltweets])
    for start in iterations_start.keys():
        for end in iterations_end.keys():
            for hourshift in iterations_hour.keys():
                print(f"{alltweets, start, end, hourshift}")
                weight_dict = adjust_weights(add_weights_to_list(tweet_list, bitstamp_dict, iterations_start[start], iterations_end[end], iterations_hour[hourshift]), len(tweet_list))
                print(total_from_dict(weight_dict))
                for word in fun_words:
                    print(word, weight_value(word, weight_dict))
                print(f"Testword: {weight_value(testword, weight_dict)}")
                print(f"\n\n", flush=True)
"""
fun_words = ["Bitcoin", "bitcoin", "Elon Musk", "To the moon!", "Dogecoin",
             "Cryptocurrency", "SpaceX", "In retrospect, it was inevitable"]
testword = ""
frequency_list = [82, 15, 28, 43, 13, 22, 2, 61, 70, 2, 8, 40, 24, 67, 75, 19, 1, 60, 63, 91, 28, 10, 24, 2, 20, 1]

for letterindex in range(0, len(string.ascii_lowercase)):
    testword = testword + string.ascii_lowercase[letterindex] * frequency_list[letterindex]
tweet_list = parse_tweets(True)
weightdict = add_weights_to_list(tweet_list, bitstamp_dict, 3, 0, True)
weightdict = adjust_weights(weightdict, len(tweet_list))

output_file = open("output_weight.txt", 'w')
for i in weightdict.keys():
    output_file.write(f"{i}: {weightdict[i]}\n")
output_file.close()

print(total_from_dict(weightdict))
for word in fun_words:
    print(word, weight_value(word, weightdict))
print(f"Testword weight = {weight_value(testword, weightdict)}")
print(f"\n\n", flush=True)
while True:
    inputword = input("> ")
    print(weight_value(inputword, weightdict))
"""
