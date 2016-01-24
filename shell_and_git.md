# Bash commands

`pwd` - shows my current location in the file system

`cd <dir>` - change to a specific directory

`cd` - change to home directory

`cd ..` - go up one directory

`cd -` - change to the previous directory

`ls` - list files in that directory

`mkdir` - create a new folder

`less filename` - read a file one page at a time; *Q* to quit, *ENTER* to go down a line, *SPACE* to go down a page

`rm filename` - deletes a file (there is no undelete)

'nano <filename>' - Create a file and begin adding text into this file, save it, and exit nano editor (You can use any editor available)

'cat <filename>' - Show file contents (i.e. the text within)

# Git commands

### PULL AND PUSH

'git pull origin master' - Pull changes from the remote repository to the local one

'git push <remote> <origin>' - Push local changes to the remote repository and update with the latest changes


### SETTING UP

`git config --global user.email '<email>'` - Setup global git email

`git config --global user.name '<name>'` - Setup global git username

'git config --list' - Displays your settings and shows you the chosen name, email, and other relevant information

### CREATE

'git clone ssh://user@domain.com/repo.git' - Clone an existing repository

'git init' - Create a new local repository and putting the directory under version control

### LOCAL CHANGES

'git status' - Check any changed files in your working directory

'git diff' - Changes to tracked files

'git diff --staged' - Shows the difference between the last committed change and what's in the staging area

'git add' - Add all current changes to the next commit

'git commit -m <message>' - save a version in the repository with the message.

'git commit -a <message>' - Commit all local changes in tracked files

'git commit -am <message>'  - Will commit all files being tracked

### COMMIT HISTORY AND STATUS

'git log' - Show all commits in reverse chronological order

'git log -p <file>' - Show changes over time for a specific file

'git blame <file>' - Who changed what and when in <file>

`git status` - Current status of the repository

`git checkout -- filename` restore the last committed version of filename

`git log` - show a commit history

'git diff HEAD~X <file>' - View the different changes at different steps to refer to old commits, where X refers to a number (for example the number 2 would show the second last commit done)

'git diff *log number* <file>'

### IGNORE

'nano .gitignore' - Create a file with written text, showing the core extensions of the files that require ignoring and not to be viewed (for example *.dat is written for files like a.dat, b.dat, c.dat to be ignores)

'git add -f <filename.extension>' - Command overrides the ignore settings set in *.gitignore* and will add <filename.extension>

'git status ignored' - View the status of ignored files withn .gitignore

======

See [this article](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668) for an overview and introduction to git
