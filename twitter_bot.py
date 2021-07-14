import string


def weight_value(tweet, weightmap):
    keylist = weightmap.keys()
    total = 0
    for symbol in tweet:
        if symbol in keylist:
            total += weightmap[symbol]
    return(total)


if __name__ == '__main__':

    weightmap = {}
    for line in open("output_weight.txt").readlines():
        line = line.split(": ")
        weightmap[line[0]] = float(line[1].strip())
    fun_words = ["Bitcoin", "bitcoin", "Elon Musk", "To the moon!", "Dogecoin",
                 "Cryptocurrency", "SpaceX", "In retrospect, it was inevitable",
                 "the quick brown fox jumped over lazy dog", string.ascii_lowercase]
    for word in fun_words:
        print(word, end=" ")
        print(weight_value(word, weightmap))
