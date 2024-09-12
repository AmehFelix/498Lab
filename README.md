Hi, I edited this file!
# 498 GitHub Lab
### 0. Setting up Git

#### 0a
If you haven't already, install Git on your system 
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
####

### Fork this repo

#### 0b
In this exercise, we'll be creating a repo by forking with GitHub. AT the top of this page, find this dialogue by clicking on fork 
####

![image](https://github.com/user-attachments/assets/5f590784-e375-4332-ac23-b2e0b7f26474)
# 

#### 0c
At the top of your forked repo, check out the options available if you click on 'code' and copy the HTTPS url
####

#
![image](https://github.com/user-attachments/assets/298afbaa-c194-42b1-86d9-2dbe3f24ce50)

In this lab, we'll be working with git bash. There are other good options such as GitHub Desktop or GitHub's CLI tool

### 1. Cloning
#### 1a
In your local coding environment terminal, navigate to a folder you can clone this repo into and enter 

```git clone replace_with_url``` 
####

#### 1b
In your local environment, add some comments to program included in the repo. For each change you make, include in a comment above that line what the previous code was or what the issue was
####

### 2. Pushing and Pulling
#### Using git add

We can add untracked changes/files to gits staging area. These changes will be what get committed when you use git commit. 

#### 2a
To add a single file ```git add replace_with_file_path``` 
####

or add all untracked changes in the repository ```git add .```

#### Using git commit
This will add the changes in your staging area to git's commit history, where git tracks all commits made. 

#### 2b
Making a commit usually looks like this ```git commit -m "replace_with_message"``` The message you enter will allow you to figure out what each commit did/does. 
####

You can also revert the most recent commit with ```git reset --soft HEAD~1 ```, 

or revert a commit with a commit ID using ```git reset replace_with_ID ```. 

To find a commit's ID, run ```git log``` to view the commit history. 

#### Using git push
Finally, sending your stuff back to a remote repo is the goal for this lab. 

#### 2c
The command ```git push origin main``` will automatically push your changes to the remote repo you cloned from. 
####

If this project started the other way around, i.e. you made a git repo locally first with ```git init```. 

Then this command would look like ```git push replace_with_url main``` 

or you could do ```git remote add origin replace_with_url``` and the first command would work.

### 3. Branching and Commit Reversal

#### 3a
Create or put in any file you want to your repo and then add, commit, and push that. 
####

Now let's say we F-ed up and the changes in our first commit need to be reworked or something, idk. But we also want to keep a backup of those changes, in case they're important later.

We will make a branch from main, navigate back to main, and revert the first commit.

#### 3b
Branching is straight forward ```git checkout -b replace_with_branch_name``` will create and move you to that branch. 
####

You can see all the branches in a repo with ```git branch```. 
 
Going back to main would be ```git checkout main```.

#### 3c
Next we can use ```git log``` to find the commit with the changes to the program. 
####

###
![image](https://github.com/user-attachments/assets/c84840b1-e45d-49d7-a567-64b350a4b30f)
###

#### 3d
Copy the commit ID (the hash), and then put that in this command ```git revert replace_with_commit_ID```. Make sure you're doing this is main. 
####

#### 3e
Next, push these changes back to GitHub. And also push your branch with ```git push origin replace_with_branch_name```
####

### 4. Stuff to note 
#### Code Spaces
While we're here, also check out codespaces. Really simple way to make quick changes or to work without access to your local machine. HOWEVER codespace sessions expire, they cannot be saved, without committing changes of course, and there is a usage limit. So this needs to be noted when using codespaces

#### Branching
This is the best way to coordinate multiple people working on the same GitHub project. 

In your local CLI, the command ```git checkout -b replace_with_branch_name``` will create a new branch and switch to that branch. Changes here will not affect main . 

To merge branches to main, first switch to main ```git checkout main``` 

and then run ```git merge replace_with_branch_name```. 

And to push a new branch to the remote repo ```git push origin replace_with_branch_name```

#### Issues and Pull Requests

These are features of GitHub itself. Pull Requests will allow you to merge your repo with a parent repo after forking, or a branch with the main codebase, and can act as a way to review changes as well. It's useful for suggesting changes from a GitHub account without access to the main codebase. 

Issues may also be useful to us as a way to track bugs and other issues that come up. This is something you should suggest to your clients, if they use GitHub. Internal you can use it for documenting suggestions, managing tasks, or just recording your progress.

### Submission
Include a folder called "submissions" in your new repositories and add screenshots of Task 1 and Task 2. Task 3 I should be able to see in your repo's GitHub page.

In Task 1, your screenshot should include the correct output of the program and the command line should show that you are in a git repository

In Task 2, Show in your command line, the commit and push outputs after running the commands.

For Task 3, your main branch should have no changes to the program and the new file you uploaded, while your branch will have the corrected program and everything else.

Finally, ! and most importantly !, make a Pull Request on this repository so I can find what you did. 

Also most importantly, ! Include your name somewhere in the Pull Request title !
