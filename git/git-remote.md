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
### 5. Faking Teamwork
### 6. Git Pushin'
### 7. Diverged history
### 8. Locked main


##  To Origin And Beyond -- Advanced Git Remotes! 
### 1. Push main
### 2. Merging with remotes
### 3. Remote tracking
### 4. Git push arguments
### 5. Fetch arguments
### 6. Source of nothing
### 7. Pull arguments
