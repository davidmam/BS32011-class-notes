# Useful Bash commands

### directories and files

`pwd` - shows my current location in the file system

`cd <dir>` change to a specific directory
`cd` change to home directory
`cd ..` go up one directory
`cd -` change to the previous directory

`ls` list files in that directory

`mkdir` create a new folder

`less filename` read a file one page at a time. 
*Q* to quit. *ENTER* to go down a line. *SPACE* to go down a page

`rm filename` - deletes a file. There is no undelete


# Git commands

`git init`  - put a directory under version control

`git status` - current status of the repository

`git add filename` adds a file to the staging area

`git config --global user.email 'd.m.a.martin@dundee.ac.uk'` - setup global git email
`git config --global user.name 'David Martin'` - setup global git user name

`git commit -m ' message'`  - save a version in the repository with the message.

`git log` - show a commit history

`git checkout -- filename` restore the last committed version of filename

