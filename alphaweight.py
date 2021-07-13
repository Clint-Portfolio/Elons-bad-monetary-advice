import string


def addweight(weightdict, sentence, difference):
    # print(sentence, difference)
    sentence = sentence.replace(" ", "")
    sentenceweight = difference / len(set(sentence))
    # print(len(set(sentence)), set(sentence))
    # print(symbolweight)

    for i in [x for x in sentence if x in weightdict.keys()]:
        weightdict[i] = weightdict[i] + sentenceweight

    return(weightdict)


def initialize_weightdict():
    weightdict = {x: 0 for x in list(string.ascii_lowercase +
                                     string.ascii_uppercase) +
                                     [str(y) for y in range(0, 10)]}
    return(weightdict)


def convert_to_weight(weightdict, sentence):
    total_weight = 0
    for letter in sentence:
        if letter in weightdict.keys():
            total_weight += weightdict[letter]
    return(total_weight)


if __name__ == '__main__':
    weightdict = {x: 0 for x in list(string.ascii_lowercase +
                                     string.ascii_uppercase) +
                                     [str(y) for y in range(0, 10)]}
    # weightdict = {}
    # for x in re.compile([a-z][A-Z]):
    #     weightdict[x] = 0

    sentence = "Hoi dit is sentence."
    starting_value = 20
    final_value = 30
    print(sum([82, 15, 28, 43, 13, 22, 2, 61, 70, 2, 8, 40, 24, 67, 75, 19, 1, 60, 63, 91, 28, 10, 24, 2, 20, 1]))
    print(len([82, 15, 28, 43, 13, 22, 2, 61, 70, 2, 8, 40, 24, 67, 75, 19, 1, 60, 63, 91, 28, 10, 24, 2, 20, 1]))
    print(len(string.ascii_lowercase))
    # print(addweight(weightdict, sentence, starting_value, final_value))
