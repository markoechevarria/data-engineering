# 12. A gentle introduction to vi

* Vi is a text editor, one of the core programs in the Unix Tradition

* `i`: to enter to insert mode

* `l`: right one character
* `h`: left one character
* `j`: down one line 
* `k`: up one line
* `0`: To the beginning of the current line.
* `^`: To the first non-whitespace character on the current line.
* `$`: To the end of the current line.
* `w`: To the beginning of the next word or punctuation character.
* `W`: To the beginning of the next word, ignoring punctuation characters.
* `b`: To the beginning of the previous word or punctuation character.
* `B`: To the beginning of the previous word, ignoring punctuation characters.
* `ctrl-F or page down`: Down one page.
* `ctrl-B or page up`: Up one page.
* `number G`: To line number. For example, 1G moves to the first line of the file.
* `G`: To the last line of the file.

* `:q`: exit
* `:w`: save

* `o`: open a line below the current line
* `O`: open a line above the current line

* `x`: The current character
* `3x`: The current character and the next two characters
* `dd`: The current line
* `5dd`: The current line and the next four lines
* `dW`: From the current cursor position to the beginning of the next word
* `d$`: From the current cursor location to the end of the current line
* `d0`: From the current cursor location to the beginning of the line
* `d^`: From the current cursor location to the first non-whitespace character in the line
* `dG`: From the current line to the end of the file
* `d20G`: From the current line to the twentieth line of the file

* `yy`: The current line
* `5yy`: The current line and the next four lines
* `yW`: From the current cursor position to the beginning of the next word
* `y$`: From the current cursor location to the end of the current line
* `y0`: From the current cursor location to the beginning of the line
* `y^`: From the current cursor location to the first non-whitespace character in the line
* `yG`: From the current line to the end of the file
* `y20G`: From the current line to the twentieth line of the file
