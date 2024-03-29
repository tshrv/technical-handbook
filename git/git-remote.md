# Git Remote
Working with remote repositories.

##  Push & Pull -- Git Remotes! 
### 1. Clone intro
```
git clone
```

**Remote**
```
c0<--c1(main)
```
**Local**
```
c0<--c1(main*,origin/main)
```
We are on branch `main` but there also exists another branch `origin/main` which is on the remote.
```
branch-name => from local, present locally
remote-name/branch-name => from remote, present locally
```

### 2. Remote branches
Remote branches reflect the state of remote repositories (since you last talked to those remote repositories). They help you understand the difference between your local work and what work is public.

Remote branches have the special property that when you check them out, you are put into `detached HEAD` mode. Git does this on purpose because you **can't work** on these branches directly; you have to work elsewhere and then share your work with the `remote` (after which your remote branches will be updated).

To be clear: Remote branches are on your local repository, not on the remote repository.
```
c0<--c1(main*,origin/main)
git checkout origin/main
git commit
c0<--c1(main,origin/main)<--c2(HEAD) # detached HEAD
```
`origin/main` will only update when the remote updates.

### 3. Git Fetchin'
Working with git remotes really just boils down to transferring data to and from other repositories. As long as we can send commits back and forth, we can share any type of update that is tracked by git (and thus share work, new files, new ideas, love letters, etc.).  
The command for this is conveniently named `git fetch`.  

```
**remote**
c0<--c1<--c2<--c3<--c6(main)
      ^--c4<--c5<--c7(dev)

**local**
c0<--c1<--c2(main,origin/main)
      ^--c4(dev,origin/dev)

git fetch # this will download all the changes for all the branches.

**local**
c0<--c1<--c2(main)<--c3<--c6(origin/main)
      ^--c4(dev)<--c5<--c7(origin/dev)

```
Commits `C2` and `C3` were downloaded to our local repository, and our remote branch `origin/main` was updated to reflect this.  
`git fetch` usually talks to the remote repository through the Internet (via a protocol like `http://` or `git://`).  

`git fetch` performs two main steps, and two main steps only. It:
- Downloads the commits that the remote has but are missing from our local repository, and...
- Updates where our remote branches point (for instance, `origin/main`)

However, it does not change anything about your local state. It will not update your main branch or change anything about how your file system looks right now. You can think of running `git fetch` as a download step.


### 4. Git Pullin'
Let's update our work to reflect the fetched changes. There are actually many ways to do this -- once you have new commits available locally, you can incorporate them as if they were just normal commits on other branches. This means you could execute commands like:
- `git cherry-pick o/main`
- `git rebase o/main`
- `git merge o/main`
Workflow of fetching remote changes and then merging them is so common that git actually provides a command that does both at once! That command is `git pull`.

```
# remote
c0<--c1<--c3(main)

# local
c0<--c1(origin/main)<--c2(main*)

# on branch main
git fetch

# local - now we have new commits on origin/main
c0<--c1<--c2(main*)
      ^--c3(origin/main)

# update main to reflect changes from origin/main
git merge origin/main

# local
c0<--c1<--c2<-------------c4(main*)
      ^--c3(origin/main)--'

```

`git pull` is essentially shorthand for a `git fetch` followed by a `git merge` of whatever branch was just fetched.
```
# remote
c0<--c1<--c3(main)

# local
c0<--c1(origin/main)<--c2(main*)

git pull
# local
c0<--c1<--c2<-------------c4(main*)
      ^--c3(origin/main)--'
```

**Important**
- `git pull` - fetch and merge, creates a merge commit.
- `git pull --rebase` - fetch and rebase, without a merge commit.


### 5. Git Pushin'
`git push` is responsible for uploading your changes to a specified `remote` and updating that remote to incorporate your new commits.
__note --__ the **behavior** of git push with no arguments varies depending on one of git's settings called `push.default`. The default value for this setting depends on the version of git you're using, but we are going to use the `upstream` value in our lessons.
```
# remote
c0<--c1(main)

# local
c0<--c1(origin/main)<--c2(main*)

git push
# step 1 - update remote
c0<--c1<--c2(main)

# step 2 - update local
c0<--c1<--c2(origin/main, main*)
```

### 6. Diverged history
Where history has diverged, git doesn't allow you to `push` your changes. It actually forces you to incorporate the latest state of the remote before being able to share your work.
```
# remote
c0<--c1(main)

# local
c0<--c1(origin/main, main*)
```
Now let's say our peers have pushed some code to the remote and we have made some commits locally as well.
```
# remote
c0<--c1<--c2(main)

# local
c0<--c1(origin/main)<--c3(main*)
```
A `git push` will fail because based on current state of local and remote, the branch `origin/main` points to two different commits.
Thus we need to incorporate those changes, from remote to our local and then.  

**How do you resolve this situation?** It's easy, all you need to do is base your work off of the most recent version of the remote branch.  
There are a **few ways** to do this, but the **most straightforward** is to **move your work via rebasing**. Let's go ahead and see what that looks like.

```
# remote
c0<--c1<--c2(main)

# local
c0<--c1(origin/main)<--c3(main*)
git push -- fails, branched have diverged.
```

`git pull` does a fetch and merge, let's try `git fetch` and `git rebase` (or, `git pull --rebase` to do everything together) for a cleaner/linear commit history.

```
git fetch

# local
c0<--c1<--c3(main*)
      ^--c2(origin/main)

git rebase origin/main
c0<--c1<--c3
      ^--c2(origin/main)<--c3'(main*)
    
git push

# remote
c0<--c1<--c2<--c3'(main)

# local
c0<--c1<--c2<--c3'(main*, origin/main)

# or, instead of fetch and merge, simply use
git pull --rebase
git push
```
We updated our local representation of the remote with `git fetch`, `rebased` our work to reflect the new changes in the remote, and then pushed them with `git push`.  

Although `git merge` doesn't move your work (and instead just creates a `merge commit`), it's a way to tell git that you have incorporated all the changes from the remote. This is because the remote branch is now an ancestor of your own branch, meaning your commit reflects all commits in the remote branch.

```
# remote
c0<--c1(main)

# local
c0<--c1(origin/main)<--c3(main*)

# remote - received some changes from someplace else
c0<--c1<--c2(main)

# on branch main in local
git fetch

# local
c0<--c1<--c3(main*)
      ^--c2(origin/main)

git merge origin/main
# local
c0<--c1<--c3<--------------c4(main*)[merge_commit]
      ^--c2(origin/main)--'

git push
# remote - new changes received
c0<--c1<--c2<--,
      ^--c3<----c4(main)

# local - changes reflect in remote branch
c0<--c1<--c3<--c4(main*,origin/main)[merge_commit]
      ^--c2---'
```


### 7. Locked main
In a large collaborative team it's likely that main is locked and requires some **Pull Request** process to merge changes.  
If you commit directly to main locally and try pushing you will be greeted with a message similar to this:
```
! [remote rejected] main -> main (TF402455: Pushes to this branch are not permitted; you must use a pull request to update this branch.) 
```
You meant to follow the process creating a branch then pushing that branch and doing a pull request, but you forgot and committed directly to main.  

**Solution** - Create another branch called `feature` and push that to the remote. Also reset your main back to be in sync with the remote otherwise you may have issues next time you do a pull and someone else's commit conflicts with yours.  

```
# remote
c0<--c1(main)

# local
c0<--c1(origin/main, main*)
```
By mistake we made some commits on `main` and now we are stuck since `push` on `main` is not allowed.

```
# local
c0<--c1(origin/main)<--c2(main*)
```

Let's create a new branch `feature` for our changes. `push` it to remote. And sync `main` back to `origin/main`

```
git branch feature
c0<--c1(origin/main)<--c2(main*,feature)

git branch -f main origin/main
c0<--c1(origin/main,main*)<--c2(feature)

git checkout feature
c0<--c1(origin/main,main)<--c2(feature*)

git push
# remote
c0<--c1(main)<--c2(feature)

# local
c0<--c1(origin/main,main)<--c2(feature*,origin/feature)
```

##  To Origin And Beyond -- Advanced Git Remotes! 
### 1. Push main
### 2. Merging with remotes
### 3. Remote tracking
`git checkout -b not_main origin/main` Now branch `not_main` is set to **track** and work with `main` on remote.  
Previously set default tracking of `main` to `origin/main` is automatically removed.

### 4. Git push arguments
```
git push <remote> <place>

<place> on local will be synchronized with its tracking branch on <remote>
```
`git push origin main` Go to the branch named `main` in my repository, grab all the commits, and then go to the branch `main` on the remote named `origin`(**tracking branch on remote**). Place whatever commits are missing on that branch and then tell me when you're done.  
By specifying `main` as the `place` argument, we told git where the commits will come from and where the commits will go. It's essentially the `place` or `location` to synchronize between the two repositories.
> Keep in mind that since we told git everything it needs to know (by specifying both arguments), it totally ignores where we are checked out!

**colon refspec**
In order to specify both the **source** and the **destination** of `<place>`, simply join the two together with a colon:
`git push origin <source>:<destination>` -- It does not matter where you are currently checked out at.

```
git push origin <source>:<destination>
# push changes from local.source to origin.destination

# remote
c0<--c1(main)

# local
c0<--c1(main,origin/main)<--c2<--c3(foo*)

# send changes till c2 to main on remote
git push origin foo^:main

# remote
c0<--c1<--c2(main)

# local
c0<--c1(main)<--c2(origin/main)<--c3(foo*)
```

Git resolved `foo^` into a location, uploaded whatever commits that weren't present yet on the remote, and then updated destination.

If the destination branch on remote does not exist, it'll be created.
```
# remote
c0<--c1(main)

# local
c0<--c1(origin/main)<--c2(main*)

# send changes till local.main to remote.newBranch
git push origin main:newBranch

# remote
c0<--c1(main)<--c2(newBranch)

# local
c0<--c1(origin/main)<--c2(main*,origin/newBranch)
```

### 5. Fetch arguments

`git fetch origin foo` Git will go to the `foo` branch on the remote, grab all the commits that aren't present locally, and then plop them down onto the `origin/foo` branch locally.
```
# remote
c0<--c1(main)<--c2<--c3(foo)

# local
c0<--c1(main,origin/main,foo,origin/foo)

git fetch origin foo

# local
c0<--c1(main,origin/main,foo)<--c2<--c3(origin/foo)
```

`git fetch remote source:destination` Here source is the ref on remote and destination is the ref on local.  

`git fetch origin foo:side` instructs git to get changes from `foo` on `origin` and put it on `side` on local. Provided, `side` does not have any commit which isn't already on `origin foo`. This will not update the `origin/foo` which was supposed to be the default destination because we explicitly stated the destination where we needed the changes.  

Just like `push`, if the destination does not exist on local, it will be created.

### 6. Source of nothing
**Oddities of `<source>`** Git abuses the `<source>` parameter in two weird ways. These two abuses come from the fact that you can technically specify **"nothing"** as a valid source for both `git push` and `git fetch`. The way you specify nothing is via an empty argument:
- `git push origin :side`
- `git fetch origin :bugFix`

**`git push origin :foo`** Deleted branch `foo` on both local and remote.
```
# remote
c0<--c1(main,foo)

# local
c0<--c1(main,origin/main,foo,origin/foo)

git push origin :foo

# remote
c0<--c1(main)

# local
c0<--c1(main,origin/main)
```
**Deletes** This operation deleted the destination location both on remote and on local. "By pushing the concept of NOTHING to it".

**`git fetch origin :bar`** Creates branch `bar` on local
```
# remote
c0<--c1(main)

# local
c0<--c1(main,origin/main)

git fetch origin :bar

# remote
c0<--c1(main)

# local
c0<--c1(main,origin/main,bar)
```
**Creates** This operation created the destination location on local. "By fetching the concept of NOTHING to it".


### 7. Pull arguments
`git pull` at the end of the day is really just shorthand for a `fetch` followed by `merging` in whatever was just fetched. You can think of it as running `git fetch` with the **same arguments** specified and then merging in where those commits ended up.

`git pull origin foo` is equal to `git fetch origin foo; git merge origin/foo;`  
`git pull origin bar~1:bugFix` is equal to `git fetch origin bar~1:bugFix; git merge bugFix;`

```
# remote
c0<--c1<--c2(main)

# local
c0<--c1(main,origin/main)<--c3(bar*)

git pull origin main:foo

# local - create destination branch foo since it does not exist
c0<--c1(main,origin/main,foo)<--c3(bar*)

# local - fetch all changes from origin.main to local.foo
c0<--c1(main,origin/main)<--c3(bar*)
      ^--c2(foo)

# local - since pull is fetch + merge, merge to currently checked out branch bar via a merge commit (rebase if --rebase supplied)
c0<--c1(main,origin/main)<--c3<--c4(bar*)
      ^--c2(foo)<----------------'
```
Wow, that's a TON in one command. We created a new branch locally named `foo`, downloaded commits from remote's `main` onto that branch `foo`, and then `merged` that branch into our currently checked out branch `bar`.