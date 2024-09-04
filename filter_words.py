import argparse

def filter_words(input_file, output_file, min_length, max_length):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            word = line.strip()
            if min_length <= len(word) <= max_length:
                outfile.write(f"{word}\n")

def main():
    parser = argparse.ArgumentParser(description="Filter words by length from an input file and save to an output file.")
    parser.add_argument('input_file', type=str, help="The input file containing words to filter")
    parser.add_argument('output_file', type=str, help="The output file to save the filtered words")
    parser.add_argument('min_length', type=int, help="The minimum number of characters a word must have to be included")
    parser.add_argument('max_length', type=int, help="The maximum number of characters a word can have to be included")
    
    args = parser.parse_args()
    
    filter_words(args.input_file, args.output_file, args.min_length, args.max_length)

if __name__ == '__main__':
    main()
