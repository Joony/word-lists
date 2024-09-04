# Word Lists for Games

Welcome to the Word Lists for Games repository! This project provides sorted word lists designed specifically for games. Currently, the repository includes word lists in English.

## About the Word Lists

The word lists in this repository are intended for use in various word-based games and activities. Each file contains words that are sorted alphabetically.

## Insert a Word into a Sorted List (`insert_word.py`)

The `insert_word.py` script allows you to insert a new word into an existing sorted word list while maintaining the sorted order. This is useful for adding new words to your word lists without manually sorting the file after every addition.

### Usage

The script can be run from the command line with the following syntax:

```sh
python insert_word.py filename word
```

### Command-Line Arguments

- **`filename`**: The path to the file where the word should be inserted (e.g., `en.txt`).
- **`word`**: The word to insert into the file.

### Example

To insert the word `apple` into the file `en.txt`, you would use the following command:

```sh
python insert_word.py en.txt apple
```

This command inserts the word "apple" into `en.txt`, ensuring that the list remains alphabetically sorted.

## Filter Words by Length (`filter_words.py`)

The `filter_words.py` script is a utility that filters words from an input file based on specified length constraints and writes the filtered words to an output file. This script is particularly useful for preparing word lists that are tailored to specific game requirements or other applications where word length is a factor.

### Usage

The script can be run from the command line with the following syntax:

```sh
python filter_words.py input_file output_file min_length max_length
```

### Command-Line Arguments

- **`input_file`**: The path to the input file containing the list of words (e.g., `en.txt`).
- **`output_file`**: The path to the output file where the filtered words will be saved (e.g., `en_2-9.txt`).
- **`min_length`**: The minimum number of characters a word must have to be included in the output file.
- **`max_length`**: The maximum number of characters a word can have to be included in the output file.

### Example

To filter words from `en.txt` that have between 2 and 9 characters and save them to `en_2-9.txt`, you would use the following command:

```sh
python filter_words.py en.txt en_2-9.txt 2 9
```

This command will process the words in `en.txt`, including only those words that have between 2 and 9 characters (inclusive) and write them to `en_2-9.txt`. 

## License

This repository is licensed under the [Creative Commons Zero (CC0) License](https://creativecommons.org/publicdomain/zero/1.0/). You can use, modify, and distribute the content in any way you like, without any restrictions.

## Contributing

We welcome contributions to enhance our word lists. To contribute, please refer to our detailed [CONTRIBUTING.md](CONTRIBUTING.md) file for instructions on how to add new words and create pull requests.

## Contact

If you have any questions or need further assistance, feel free to open an issue on the GitHub repository or contact us through GitHub.
