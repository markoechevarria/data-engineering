# Working with Unix

* man: look up the documentation for a command
* apropos: search commands associated with a word
* \*: star wildcard can represent many kinds and number of characters
* grep: search a file for a word
* grep -E: search  regular expresions
    * \. : represent any character
    * \+ : one or more ocurrences of the proceeding expression
    * \* : zero or more ocurrences of the preceding expression
    * \{\} : specify an exact number of ocurrences of an expression
    * \(\) : capture groups withing regular expressions
    * \\w : represent all "word" characters
    * \\d : represent all "number" characters
    * \\s : represent all "space" characters
    * \-v flag: return all of the lines not matched by the regular expression
    * \[\] : create a set of something
    * \[\^\] : complement of a set
    * \- : specify a range of characters
    * \^ : represent the start of a line
    * \$ : represent the end of a line
    * \| : "or" metacharacter
* find : find the location of a file or the location of a group of files ` find [directory] [method flag]`
* history: display what commands have entered into the console since opening the current terminal
* ~/.bash_history file list command have been used in the past
* alias: create a command that can be used as a substitue for a longer command 
* ~/.bash_profile is a text file that is run every time the shell start, and it's the best place to assign aliase
* pipes ( \| ) : allows take the output of a command and use it as the input to another command




























