# Learning git and github

learning the basics and advanced git usage 

make a directory and run command to make the directory a git repository

```
	> git init
```

create a file sample.py and add a simple print statement into the file

run command

```
	> git status
```

git status gives us the status of the files that are changed recently inside the git repository

the git gives us the command to add the files into the staging area and commit the changes

```
	> git add <file>
	> git add sample.py
```

now the file sample.py is in the staging area, now we can use the command for commiting the changes

```
	> git commit
	the file that is in the staging area will be the one that will be commited
	if we have set the sublime editor for commiting then editor will open for writing the message
```

after typing the message, save the file and close the editor, you will see the number of lines 
changed and the insertion of lines in the file

```
to remove a file from staging area run the command 
	> git rm --cached sample.py
```

If we want to keep a file away from the git repo and the staging area then we can add that file to
.gitignore

** When we import a local file into another file and use it then python3 creates a __pycache__ file 
in which all the pyc files will be stores which are bytecode compiled version of the file

To make a .gitignore file in the repo and add the files that are to be prevented from staging area

make a new file from ST3 and save it as .gitignore and type in the full names of the files along
with the extension

the git will show the .gitignore text file as the untraked file so

```
	> git add .gitignore
	> git commit -m "create .gitignore and add __pycache__ and README.rst"
```

-m and a message in quotes after that will add the message in the commit

after typing in the names of the files that are to be ignored from git, those files and folder will
not be in the git status anymore

NOTE: there are limitations for the files to be added in the git repo, only those files that are
	  source files (files that we write in the editor) are to be added and not the generated files
	  or the files that are made by the computer

** There are times when you have to work on your code seperately and while working in teams you 
have to work on your code and then commit the changes afterwards, for that you have to move away
from master branch and create a seperte stream for you own project

```
	> git checkout -b rishabh_branch
```

this command checks out in the new branch just created by the command -b <branch-name>

now git status, you can look at the branch you currently are in

once you have created the the new branch and checkout the branch, the changes you make in the files
will show up in status and you can commit those changes and also git log to see the commit you just
made but it will have a different SHA in the rishabh_branch

now checkout in the master branch and git log again, can you find your recent commit made in the 
rishabh_branch, NO!!!

this is magic of branches

Now to review your branches you can use the command 

```
	> git show-branch rishabh_branch master
```

this will show the commit in the master and rishabh_branch with their names and if you want to
look at their SHA then use 

```
	> git show-branch --sha1-name my_new_feature master
```

now if you want to merge the two branches then first

```
	> git checkout master
	> git merge rishabh_master
```

now look at the git log and you can see the changes from the rishabh_branch in the master branch

# Advanced Features
double dot notation

```
git log <commit_id_1>..<commit_id_2>
```

command will print the commits after commit_id_1 till commit_id_2 including commit_id_2 commit

When logging commits from an id at top from one parent and at top from second parent will only
print the commits from the common commit to the commit_id_2

visit [advanced git tutorial](https://realpython.com/advanced-git-for-pythonistas/) for whole 
tutorial.

Triple dot notation

```
git log <commit_id_1>...<commit_id_2>
```

command will print the commits that are in between either commits but not in both commit ids

```
git rebase <branch-name>
```

the above command is for those cases when we have,

HEAD , MASTER on the last commit
We have to make some changes in some 5 level before revision
So, we checkout that commit
Checkout a new branch
Commit our changes there
Checkout the master branch
Find our changes haven't affected the master branch
So, we rebase the whole commits after our branch using

```
git rebase <branch-name>
```

```
git stash save | git stash pop
git stash save == git stash
git stash save | git stash pop --index
git stash save "save-work" | git stash pop
git stash save --include-untracked "saving-work" | git stash pop --index | git stash pop
git stash list
git stash show | git stash show stash@{1} | git stash show -p stash@{1}
git stash pop stash@{1} | git stash apply | git stash apply stash@{1}
```

above command will save our non-committed work including untracked files or files that are in staging
area or index and using stash pop will recover all our work and we can also name our stash, stash 
list returns all the stashes that we have so far. For getting all the information of the files that 
are in the stash we use the command stash show, mentioning the stash number will show details for 
that particular stash or we can use -p to see very detailed path info with the changes in each file

We can pop the stash into the working directory from the stash list by specifying the stash or we can
keep our work in stash as well as in the working directory using the stash apply

```
git diff | git diff --staged
```

We can use diff to get the changes that are currently in all the files in the working directory
The default diff shows all the changes that are unstaged, for getting all the changes in files that 
are in the staging use the optional --staged

```
git diff SHA SHA
```

To compare any two commits in the your repo use the diff with the SHA

```
git diff master temp
git diff master^ master
git diff HEAD~3 HEAD
git diff HEAD~3 HEAD --greeting.py
git diff HEAD^ HEAD
git diff HEAD^ HEAD --name-only
```

To get all set of changes between the master and any branch say temp then use git diff
The --name-only option will show you the list of filename that were changed between two commits, but 
not what changed in those files.

```
git config --global diff.tool meld
git config --global difftool.prompt false
git difftool HEAD^ HEAD
git difftool stash@{1} | git difftool stash
```

Difftool launches a seperate window for showing the changes which is much easier to look at than our
command line interface, you can launch the difftool with the same keyword.

```
git commit --amend | git commit --amend -m "commit message"
```

If you have made some mistakes in the commit message then you can edit the message for that 
particular commit using the --amend option and this amends should be made only when there are no
other commits based on this particular commit, then too you should only --amend when the commit is 
local and not has been pushed to github.

```
git pull -r
```

If there are changes in the remote that you want to pull and have in your local repo you will git 
pull which will merge the changes to the remote branch, git pull -r will rebase your commits on top 
of the changes that were on the remote.

```
git rebase -i
```

There is a -i flag you can add to the rebase command that will put it into interactive mode, this 
feature lets you have full list of commits before you push them to the remote

```
git log --oneline
```

For showing a short listed details with only the SHA (short) and the commit message, you can use
the --oneline option along with git log

```
git rebase -i SHA
```

Suppose you have added a new feature and in that process you have made a lot of commits and those
commits appear in the log which belongs to single feature, those commits won't be needed by you in 
the future and neither by your team members so you can put all those commits inside the single one
using the rebase -i option, choose the commit from the log above which all the other commits exists
for your feature and then use it with the above replacing its SHA in the command.

Then you will be given all the log commits in reverse order from bottom to top but not including the
SHA that was used with the rebase command. There will be instructions given, generally you will pick
the first commit message that appears for the parent one for feature (which happens to be the commit 
just after the commit used with the rebase command), then you can either use the full keyword or just
the short 's' for squasing all the commits under the picked commit.

Save the sublime window (if sublime is set your default editor for git) and git will show you the 
preview of how your commits will look after rebasing and you can edit them, save and git will rebase 
all those commits onto the one you picked, git log again and you can see your changes

```
git revert HEAD | git revert HEAD -n
```

When you want to remove the changes made from the most recent commit you can revert your HEAD using
the above command and those changes will be back but the commit history won't change but a new 
commit message (default) will be added to the log, there is no option to add a message in the 
revert but you can skip the process of showing the window using the -n.

```
git clean | git clean -x | git clean -xd
```

CAUTION: Use git clean carefully as the actions from clean command are not reversible
This command cleans all the files that are untracked in the working directory
If you want to delete the files that are in the .gitignore for ignoring you can use -x for that
For deleting any folders that are ignored, you can include 'd' as in -xd

```
dir >> file.extension | ls >> file.ext | echo lines-to-add >> file.ext >> echo print-anything-in-cmd
```

To add a new file in the current directory you can use dir command in windows or ls in git / terminal
or you can just add a new line using the echo command in the file, do not add quotes in the line 
unless you want quotes in the file too and mention the file name after two angle brackets
