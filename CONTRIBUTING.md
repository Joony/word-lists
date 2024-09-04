# Contributing to Word Lists for Games

Thank you for your interest in contributing to the Word Lists for Games project! We welcome contributions that enhance the quality and diversity of our word lists. This document outlines the process for contributing, including how to add new words and submit pull requests.

## How to Contribute

### 1. Fork the Repository

To contribute to this project, you'll need to fork the repository to your own GitHub account:

1. Click the "Fork" button at the top right of this repository's page.
2. This will create a copy of the repository in your GitHub account.

### 2. Clone the Forked Repository

Once you have forked the repository, clone it to your local machine:

```sh
git clone https://github.com/your-username/word-lists-for-games.git
```

Replace `your-username` with your GitHub username.

### 3. Add a New Word

To add a new word to an existing word list, use the `insert_word.py` script. This script will automatically insert the word in the correct alphabetical position within the specified file.

**Example Command:**

```sh
python insert_word.py en.txt apple
```

This command inserts the word "apple" into the `en.txt` file, ensuring that the list remains alphabetically sorted.

### 4. Filter Words by Length

If you want to create a new word list with words of a specific length, use the `filter_words.py` script. This script will filter words from an input file and save them to an output file based on the specified length constraints.

**Example Command:**

```sh
python filter_words.py en.txt en_2-9.txt 2 9
```

This command filters words from `en.txt` that have between 2 and 9 characters and saves them to `en_2-9.txt`.

### 5. Commit Your Changes

After making your changes, commit them to your forked repository:

```sh
git add en.txt
git commit -m "Added the word 'apple' to en.txt"
git push origin main
```

### 6. Submit a Pull Request

Once your changes are committed and pushed to your forked repository, you can submit a pull request:

1. Go to the original repository on GitHub.
2. Click on the "Pull Requests" tab.
3. Click "New Pull Request".
4. Choose the branch from your fork that contains the changes you want to merge.
5. Submit the pull request for review.

### 7. Review and Merge

Your pull request will be reviewed by the maintainers of the project. If everything looks good, it will be merged into the main repository. If there are any issues or suggestions, you will be notified via the pull request comments.

## License

By contributing to this repository, you agree that your contributions will be licensed under the [Creative Commons Zero (CC0) License](https://creativecommons.org/publicdomain/zero/1.0/).

Thank you for contributing to Word Lists for Games!
