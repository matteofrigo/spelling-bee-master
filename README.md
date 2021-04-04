# Spelling Bee Master
A number of Python solutions
([1](https://towardsdatascience.com/solving-the-new-york-times-spelling-bee-puzzle-in-python-511bcb5ea65e),
[2](https://medium.com/python-examples/simple-python-app-for-spelling-bee-c220d239c8ae),
[3](https://mharty3.github.io/blog/spelling-bee/),
[4](https://github.com/philshem/open-spelling-bee)) have been proposed for the
[Spelling Bee problem](https://www.nytimes.com/puzzles/spelling-bee).
The one that we propose here aims at being the simplest and most 
**naive solution**.
It will probably be the slowest and numbest, but it provides a generous amount
of candidate words, among which the user will have to pick the ones that are 
not geographical terms or personal names.

## The rationale
* Download the english vocabulary from
[here](https://github.com/dwyl/english-words).
* Transform the vocabulary into a dictionary that associates each letter to the
set of words that contain that letter.
* From the struct, pick the set of the words that contain the mandatory letter.
* Go through each of these words and keep only those that are made with letters
in the admissible dictionary.

# How to use
* Set the mandatory (central) letter, e.g., `mandatory = 'u'`.
* Set the six optional letters in a set, e.g., 
  `optional = {'t', 'e', 'c', 'a', 'o', 'r'}`. 
* Run the script.
* Read the printed words.

## Requirements
* Python 3

# Acknowledgements
Thanks to the people that maintain the 
[english words database](https://github.com/dwyl/english-words).
