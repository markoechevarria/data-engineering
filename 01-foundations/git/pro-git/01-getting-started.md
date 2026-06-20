# 01. Getting Started

## About Version Control

* Version control is a system that records changes to a file or set of files ovver time so that you can recall specific version later
* A version control allows allows revert selected files back to a previous state, revert the entire project back to a previous state, compare changes over time, see who last modified something that might be causing a problem, who introduced an issue and when, and more

* Local Version control systems: it had a simple database that kept all the change to files under revision control
* Centralized Version control systems: these systems have a single server that contains all the versioned files, and a number of clients that check out files from that central place
* Distributed Version control systems: is a tool that tracks changes in files and coordinates work among multiple people. Unlike older centralized systems, every developer downloads a complete "clone" of the project, including its entire history, to their own computer.

## A short history of Git 

* It born in 2005, due to the end of the relationship between the Linux Kernel community and BitKeeper
* The goals of git were:
    * Speed
    * Simple Design
    * Strong support for non-linear development (thousand of parallel branches)
    * Fully distributed
    * Able to handle large projects like the Linux Kernel efficiently (speed and data size)

## What is Git?

### Snaphosts, Not differences

* Other systems think of the information they store as a set of files and the changes made to each file over time. Git thinks of its data more like a series of snapshots of a miniature filesystem
* With git, every time you commit, or save the state of your project, git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot

### Nearly Every Operation is Local

* Most operations in git need only local files and resources to operate. Because we have the entire history of the project right there on our local disk, most operations seem almost intantaneous

### Git has integrity

* Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it's impossible to change the contents of any file or directory without Git knowing about it

### Git generally only adds data

* When we do actions in Git, nearly all of them only add data to the Git database. It is hard to get the system to do anything that is not undoable or to make it erase data in any way

### The three states

* Modified: means that we have changed the file but have not commited it to our database yet
* Staged: means that we have marked a modified file in its curernt version to go into our next commit snapshot
* Commited: means that the data is safely stored in our local database

* The working tree is a single checkout of one version of the project
* The staging are is a file, generally contained in the Git directory, that store information about what will go into our next commit
* The git directory is where Git stores the metadata and object database for our project

* The basis Git workflow goes something like this:
    * We modify files in our working tree
    * We selectively stage just those changes we want to be part of our next commit, which adds only those changes to the staging area
    * We do a commit, which takes the files as they are in the staging are and stores that snapthot permanently to our git directory

## The Command Line

* Is the only place we can run all Git commands

## Installing Git

* In a Debian-based distribution `sudo apt install git-all`

## First-Time Git Setup

* `git config` lets us get and set configuration variables that control all aspects of how Git looks and operates
    * [path]/etc/config file: Contains values applied to every user on the system and all of their repositories
    * ~/.gitconfig file: values specific personally to us, the users    * config file: in the git directory. Specific to that single repository

### Identity

* To set our username and email address
```
git config --gloabl user.name "Marko"
git config --gloabl user.email markofidel10@gmail.commit
```
### Defaul branch name

* By default Git will create a branch called master when we create a new repository with `git init`
* To change the name of the default branch name do:
`git config --global init.defaultBranch new_name`

### Check our settings

* `git config --list`: List all setting Git can find at certain point

## Getting Help

`git help`: to get a comprehensive manual page (manpage) help for any of the Git commands
