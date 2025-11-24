# obtain a list of files in the input directory


from ._internals.write_word_counts import write_count_words
from ._internals.count_words import count_words
from ._internals.split_into_words import split_into_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines


def main():
    input_folder = 'data/input/'
    output_folder = 'data/output/'
    # read all lines
    all_lines = read_all_lines(input_folder)
    # preprocess lines
    all_lines = preprocess_lines(all_lines)
    # split in words
    words = split_into_words(all_lines)
    # count words
    counter = count_words(words)
    # write count words
    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()
