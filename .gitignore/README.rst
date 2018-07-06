make a directory and run command to make the directory a git repository

	> git init

create a file sample.py and add a simple print statement into the file

run command

	> git status

git status gives us the status of the files that are changed recently inside the git repository

the git gives us the command to add the files into the staging area and commit the changes

	> git add <file>
	> git add sample.py

now the file sample.py is in the staging area, now we can use the command for commiting the changes

	> git commit
	the file that is in the staging area will be the one that will be commited
	if we have set the sublime editor for commiting then editor will open for writing the message

after typing the message, save the file and close the editor, you will see the number of lines 
changed and the insertion of lines in the file

to remove a file from staging area run the command 
	> git rm --cached sample.py

If we want to keep a file away from the git repo and the staging area then we can add that file to
.gitignore

** When we import a local file into another file and use it then python3 creates a __pycache__ file 
in which all the pyc files will be stores which are bytecode compiled version of the file

Windows won't allow you to make a .gitignore file so in terminal run command

	> mkdir .gitignore

and then place those files inside the .gitignore folder, to keep the files out of git repo

