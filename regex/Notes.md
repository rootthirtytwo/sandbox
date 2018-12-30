## Basic Patterns
* . Any character
* \w : Alphanumeric characters
* \W : Non alphanumeric characters
* \d : Any digits [0-9]
* \D : Non digits 
* \b : boundary between word and non-word
* \s : Any whitespace
* \S : Any non whitespace characters
* \t : Tab
* \n : Newline
* \r : Return
* ^  : start of the match
* $  : end of the match
* \  : Escape character "specialness" of a character.

## Repetition

* \+ : One or more occurrences
* \* : Zero or more occurrences
* \? : Zero or one occurrence

## Options
The option flag is added as an extra argument to the search() or findall().
* IGNORECASE : Ignore upper/lowercase differences for matching.
* DOTALL : allows the dot (.) metacharacter match all characters, including the newline character (\n).
* MULTILINE : is necessary if your input string has newline characters (\n), this flag allows the start and end metacharacter (^ and $ respectively) to match at the beginning and end of each line instead of at the beginning and end of the whole input string. 

## Greedy v/s Non-Greedy
* .*  : Greedy. e.g pattern = <b.*>, str = <b\>Hello<\/b>, result = <b\>Hello<\/b> goes till the last available '>' character match.
* .*? : Non-Greedy. Stops at first occurrence, result = <b\>

## substitution


## *References*
1. Google for Education. [link](https://developers.google.com/edu/python/regular-expressions)
2. RegexOne. [Link](https://regexone.com/references/python)

