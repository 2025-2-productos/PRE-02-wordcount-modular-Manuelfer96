
def split_into_words(all_lines):
    # count the frequency of the words in the files in the input directory
    words = []
    for line in all_lines:
        words.extend(w.lower().strip(",.!?") for w in line.split())

    return words
