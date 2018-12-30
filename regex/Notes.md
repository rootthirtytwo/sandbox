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
* DOTALL : allow dot (.) to match newline.
* MULTILINE : Multiline match in the given string is spread across many lines. 

## Greedy v/s Non-Greedy
* .*  : Greedy. e.g pattern = <b.*>, str = <b\>Hello<\/b>, result = <b\>Hello<\/b> goes till the last available '>' character match.
* .*? : Non-Greedy. Stops are first occurrence, result = <b\>

## substitution


## *References*
1. Google for Education. [link](https://developers.google.com/edu/python/regular-expressions)
2. RegexOne. [Link](https://regexone.com/references/python)

