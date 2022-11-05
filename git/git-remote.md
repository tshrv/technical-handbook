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

`git pull` is essentially shorthand for a `git fetch` followed by a `merge` of whatever branch was just fetched.
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
### 7. Locked main


##  To Origin And Beyond -- Advanced Git Remotes! 
### 1. Push main
### 2. Merging with remotes
### 3. Remote tracking
### 4. Git push arguments
### 5. Fetch arguments
### 6. Source of nothing
### 7. Pull arguments
