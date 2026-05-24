# 6. Redirection

* I/O redirection allows us to redefine where starndar output goes. It use the `>` redirection operator and the `>>` append redirection operator
* Redirect standard error: use the `2>` redirector
Redirect standar output and standard error to one file: `ls -l /bin/usr > ls-output.txt 2>&1`

* `cat`: reads one or more files and copies them to standard output
* To create a file containing text entered by the user `cat > document.txt`

* Pipelines: Allow *pipe* the standar output of one command into the standardar inpuot of another

* `uniq`: used in conjuction with `sort`
* `wc`: print line, word, and byte counts, the -l option limites output to report only lines
* `grep pattern filenam`: print lines matching a pattern
* `head/tail`: print first/last part of files, by default both commands print 10 lines of text, but that can be adjusted with the -n option
* `tee`: read from stdin and output to stdout and files, useful for capturing a pipeline's contents at an intermediate stage of processing
