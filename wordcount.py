from os import path, walk
import sys


def run(root, top=10):
    source = ''
    for dpath, _, fnames in walk(root):
        for fname in fnames:
            # collect source text from each file
            source += open(path.join(dpath, fname)).read()

    # turn text source into sequence of words
    words = source.lower().split()

    # count occurrences of all words
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # sort counts in descending order
    counts = sorted(counts.items(), key=lambda item: -item[1])
    # print top n words with counts
    print(counts[:top])


# recursively walk the first command line argument, count words
run(sys.argv[1])
