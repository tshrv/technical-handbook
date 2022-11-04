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
