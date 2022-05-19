Instructions

prerequisites:
- install git
- create a github account, preferably with alliander access, but not necessary
..



Step 1: create a local git project (what is git?!)

- open terminal and go to the main folder of your git project, the same folder this file is resided 
- do cmd: git init



Step 2: add and commit a file to your git project (add/commit tracking and not tracking projectfiles)

- do cmd: git add my_first_git_project/*
- do cmd: git status
- do cmd: git commit -m "first init message" 
- do cmd: git status



Step 3: create a github project, and upload this current project to github   (sync to github and origin concept)

- do cmd: git remote add origin  \*(see online the link)\*
- do cmd: git push -u origin master

check your new project online!



Step 4: run python file and make a small change (rehearse: git status, git add/commit, git push)

- do: run python file hello_git_scripting.py
- do: fix error
- do cmd: git status
- do cmd: git add .......
- do cmd: git commit -m "....your own message"



Step 5: add a .gitignore file to your project:

- create file in main folder: .gitignore
- open .gitignore file and put in: .idea/*

optionally add more files that you like to ignore

- do cmd: git status  (check what happens when you add .gitignore to your .gitignore file)
- do cmd: git add and commit the .gitignore file
- do cmd: git puhs origin master
- Check changes online



Step 6: branching
- do cmd: git branch develop
- do cmd: git checkout develop
- do cmd: git status
    - Question: Does your branch currenty live only online or locally, or both?
- do cmd: git push origin develop 



Step 7: Do in pairs: fix the rest of the code
- do: if you have a partner, decide which codebase to use for the remaining part, and clone the codebase if you don't have it on your computer yet

try fixing the following issues:

    - structure the hello_git_scripting.py using functions, take inspiration from the file 'hello_git_function.py'
        - implement a check that asks the user whether he /she likes to try again after guessing the decryption key
    - try fixing the decrypt message function
    
- do: divide the tasks above, and each do the following:
    - do: think of a new branch name
    - do cmd: git checkout -b feature/*branch_name*   (similar to: git branch feature/*branch_name*; and then: git checkout *branch_name*)
    - do check: are you on your feature branch?
    - do python: fix the code as you like
    - do add/commit your changes
    - do push your changes to github
    - do check if your feature branch is online visible
    - do: open up a pull request from your branch to develop on github.com, and ask for a review by your partner
    - do: review the work of your partner, if you like, give harsh criticism and try to once and for all destroy the confidence of your colleague by questioning everything in the code
    - do: return to your own branch and resolve any comments of your partner
    

Step 8: Merging or rebasing your branch to develop
For the first feature branch, the one that restructured the python file, do the following:
- go to the online interface, and check if github notices any conflicts that need a manual fix before merging to develop
- probably not, so just merge your branch to develop

- go to the other branch, the one that solves the decryption, and check if github notices any conflicts that need a manual fix before merging to develop
- there may possibly turn up some merge conflicts. To follow some good Git Hygiene practices, we do the following:

- first merge the new version of develop to your branch, before merging your work to develop. This eschews that unresolved conflicts will turn up in the develop branch

Merging the develop branch into your own branch can be done in two ways:
- git merge

 OR
- git rebase

The syntax for rebase is a bit less intuitive if you are going to use extra parameters, but we won't need them today. So for both you need to do the following:

- do cmd: git checkout develop
- do cmd: git pull
- do cmd: git checkout feature/*branch_name*  (the branch that still needs to be merged to develop)
- do cmd: git status (check if you are really on your feature branch, and not on develop)
- do cmd: git merge develop    OR  git rebase develop
- do cmd: fix possible conflicts
- do test python files: check if your code still works!
- after resolving all conflicts, do cmd: git push origin feature/*branch_name*

check your branch online, and see if git sees possible merge conflicts, if not merge your branch to develop and close the pull request


    
Step 8: Bring develop to master
- do cmd: git checkout develop
- do cmd: git pull develop
- do cmd: git checkout master, and pull master
- do cmd: git merge develop

