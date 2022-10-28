# Git Fundamentals

Learning resource [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
Playground [https://learngitbranching.js.org/?NODEMO](https://learngitbranching.js.org/?NODEMO)

## Introdution
A nicely paced introduction to the majority of git commands.

#### 1. Commit
Git wants to keep commits as lightweight as possible though, so it doesn't just blindly copy the entire directory every time you commit. It can (when possible) compress a commit as a set of changes, or a "delta", from one version of the repository to the next.
`git commit`

#### 2. Branching
Branches in Git are incredibly lightweight as well. They are simply pointers to a specific commit -- nothing more. This is why many Git enthusiasts chant the mantra:
`branch early, and branch often`
Because there is no storage / memory overhead with making many branches, it's easier to logically divide up your work than have big beefy branches.
When we start mixing branches and commits, we will see how these two features combine. For now though, just remember that a branch essentially says "I want to include the work of this commit and all parent commits."
- create a branch `git branch <new-branch-name>`

On branch `main`, at commit `c1`, `git branch dev` will create a new branch `dev` which will also point to commit `c1` at that point.

- move to `dev` branch `git checkout <branch-name>` this branch has to exist, if need to create use `checkout -b`

There is a new command `switch`, experimental.

#### 3. Merging
Great! We now know how to commit and branch. Now we need to learn some kind of way of combining the work from two different branches together. This will allow us to branch off, develop a new feature, and then combine it back in.
The first method to combine work that we will examine is git merge. Merging in Git creates a special commit that has two unique parents. A commit with two parents essentially means "I want to include all the work from this parent over here and this one over here, and the set of all their parents."

On branch `main`, `git merge bugFix` will merge `bugFix` into `main`
This will create a new commit `c3` which has two parents `c1` from main and `c2` from `bugFix`
Also need to do `git checkout bugfix; git merge main` to merge all changes from `main` into `bugfix` so that both branches have all the work.
for instance, on feature branch, pull dev, checkout to dev and merge feature into dev

Queries-
- on main, git merge bugfix, on bugfix, git merge main, difference?

#### 4. Rebase
The second way of combining work between branches is rebasing. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.
While this sounds confusing, the advantage of rebasing is that it can be used to make a nice linear sequence of commits. The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.
```
c0--c1(main, bugfix)

        +--c2(main)
c0--c1--|
        +--c3(bugfix)
```

on branch bugfix, `git rebase main` will create a copy of `c3` as `c3'` and put in ahead of `c2` so that it would look like `c3'` was done after `c2`, sequentially, but actually it was done in parallel.
This is how we make it look linear and pretty
```
        +--c2(main)--c3'(bugfix)
c0--c1--|
        +--c3
```
on branch main, `git rebase bugfix` will move main to c3'
original `c3` still exists in the tree, but no longer being referenced by any branch
```
        +--c2--c3'(main, bugfix)
c0--c1--|
        +--c3
```

## Ramping Up
The next serving of 100% git awesomes-ness. Hope you're hungry.

#### 1. Detach the HEAD

#### 2. Relative refs

#### 3. Reverse changes


## Moving work around
"Git" comfortable with modifying the source tree :P
#### 1. Cherrypick

#### 2. Interactive rebase

## Mixed bag
A mixed bag of Git techniques, tricks, and tips.
#### 1. Grabbing Just 1 Commit

#### 2. Juggling Commits

#### 2. Tags

#### 2. Describe

## Advanced
For the truly brave!
#### 1. Rebasing over 9000 times

#### 2. Multiple parents

#### 2. Branch Spaghetti
