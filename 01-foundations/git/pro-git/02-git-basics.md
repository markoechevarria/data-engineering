# 02. Git Basics

## Getting a Git Repository

### Initializing a Repository in a Existing Repository

* If we have a project directory that is currently not under version control and we want to start controlling it with Git, we first need to go to that project's directory

* `git init`: this creates a new subdirectory named `.git` that contains all of our necessary repository files.

### Cloning an Existing Repository

* `git clone <url>`: Get a copy of an existing Git repository. Every version of every file for the history of the project is pulled down by default when we run `git clone`

## Recording changes to the Repository

* Tracked Files: are files that were in the last snapshot, as well as any newly staged files; they can be unmodified, modified, or staged
* Untracked Files: are everything else - any files in our working directory that were not in our last snapshot and are not in our staging area

### Checking the status of our files

* `git status`: We use this command to determine which files are in which state. It tells us which branch we are on

### Tracking new Files or Staging modified Files

* `git add <file-name>`: used to begin tracking new files, to stage files, and do other things





