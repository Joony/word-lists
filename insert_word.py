import argparse
import bisect

def insert_word(filename, new_word):
    # Read the existing words from the file
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        words = []
    
    # Use bisect to find the position where the new word should be inserted
    index = bisect.bisect_left(words, new_word)
    
    # Insert the new word into the list
    words.insert(index, new_word)
    
    # Write the updated list back to the file
    with open(filename, 'w') as file:
        file.write('\n'.join(words) + '\n')

def main():
    parser = argparse.ArgumentParser(description='Insert a word into a sorted file.')
    parser.add_argument('filename', type=str, help='The name of the file to modify')
    parser.add_argument('word', type=str, help='The word to insert into the file')
    
    args = parser.parse_args()
    
    insert_word(args.filename, args.word)

if __name__ == '__main__':
    main()
