from collections import Counter


def count_words(string):
    d = {}
    for word in string.split():
        d[word] = d.get(word, 0)+1
    return(d)


def max_occurence_words(string):
    dictionary = count_words(string)
    return(sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0][0])


if __name__ == "__main__":
    string = input()
    print(max_occurence_words(string))
