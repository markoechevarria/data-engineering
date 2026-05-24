# 7. Seeing the word as the shell sees it

* Eeach time a command is types and the ENTER key is pressed, bash performs several substitutions upon the text before it carries out the command. This process is called *expansion*
* Pathname expansion: the mechamism by which wildcards work
* Tilde expansion: When used at the beginning of a word, it expands into the name of the home directory of the named user
* Arithmetic expansion: Thell allows arithmetics to be performed by expansion `echo $((expression))`
* Brace expansion: It allow create multiple text strings from a pattern containing braces `echo {A,B,C}` `echo {1..5}`
* Parameter expansion: It allow get variable and its content `echo $USER`
* Command substitution: allow to use the output of a command as an expansion `echo $(ls -la)`

## Quoting

* Double quotes: Inside double quotes, all the special characters used by the shell lose their special meaning and are treated as ordinary characters, the exceptions are $, \ and `
* Single quotes: It allow suppress all expansions
* Escaping characters: To quote only a single character, also used to escaping to eliminate the special meaning of a character in a filename
* Backslash escape sequences: \n -> newline, \t -> tab

