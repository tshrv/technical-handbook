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
Moving around in Git
Before we get to some of the more advanced features of Git, it's important to understand different ways to move through the commit tree that represents your project.
Once you're comfortable moving around, your powers with other git commands will be amplified

#### 1. Detach the HEAD
First we have to talk about `"HEAD"`. HEAD is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of.
HEAD always points to the most recent commit which is reflected in the working tree. Most git commands which make changes to the working tree will start by changing HEAD.
Normally HEAD points to a branch name (like bugFix). When you commit, the status of bugFix is altered and this change is visible through HEAD.
Detaching HEAD just means attaching it to a commit instead of a branch. This is what it looks like beforehand: `HEAD -> main -> C1`
`git checkout c1`
And now it's `HEAD -> C1`

Queries
- why detach HEAD? solution to which problem?

#### 2. Relative refs
Moving around in Git by specifying commit hashes can get a bit tedious. In the real world you won't have a nice commit tree visualization next to your terminal, so you'll have to use git log to see hashes.
Furthermore, hashes are usually a lot longer in the real Git world as well. For instance, the hash of the commit that introduced the previous level is `fed2da64c0efc5293610bdd892f82a58e8cbc5d8`. Doesn't exactly roll off the tongue...
The upside is that Git is smart about hashes. It only requires you to specify enough characters of the hash until it uniquely identifies the commit. So I can type `fed2` instead of the long string above.

Like I said, specifying commits by their hash isn't the most convenient thing ever, which is why Git has relative refs. They are awesome!
With relative refs, you can start somewhere memorable (like the branch bugFix or HEAD) and work from there.
Relative commits are powerful, but we will introduce two simple ones here:
Moving `upwards one commit` at a time with `^`
Moving `upwards a number of times` with `~<num>`

Let's look at the `Caret (^)` operator first. Each time you append that to a ref name, you are telling Git to find the parent of the specified commit.
So saying `main^` is equivalent to `"the first parent of main"`.
`main^^` is the grandparent `(second-generation ancestor)` of main

You can also reference `HEAD` as a relative ref.
Easy! We can travel backwards in time with `HEAD^`
`git checkout HEAD^` moves `HEAD` one commit up, thus moving back in time.
`git checkout HEAD~5` move 5 commits up
`git checkout HEAD~0` points to where `HEAD` currently points

Git also has the `tilde (~) operator`.
The tilde operator (optionally) takes in a trailing number that specifies the number of parents you would like to ascend.

**Branch Forcing**
One of the most common ways I use relative refs is to move branches around. You can directly reassign a branch to a commit with the `-f` option.

`git branch -f main HEAD~3` moves (by force) the main branch to three parents behind HEAD.

```
c0--c1--c2--c3(*main)
git branch -f main HEAD~2
c0--c1(*main)--c2--c3
```
Relative refs gave us a concise way to refer to C1 and branch forcing (-f) gave us a way to quickly move a branch to that location.

#### 3. Reverse changes
There are many ways to reverse changes in Git. And just like committing, reversing changes in Git has both a low-level component (staging individual files or chunks) and a high-level component (how the changes are actually reversed).

There are two primary ways to undo changes in Git -- one is using `git reset` and the other is using `git revert`.

`git reset` reverses changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;" git reset will move a branch backwards as if the commit had never been made in the first place.
`git reset HEAD~1` move Head one point up
```
c1<--c2(main*)
c1<--c2<--c3(main*)
git reset HEAD~1
c1<--c2(main*)<--c3
c1<--c2<--c4(main*)
      ^--c3
```

`git revert` While resetting works great for local branches on your own machine, its method of **"rewriting history" doesn't work for remote branches that others are using**.

In order to reverse changes and share those reversed changes with others, we need to use git revert. Let's see it in action.

```
c1<--c2(main*)
c1<--c2<--c3(main*)
git revert HEAD
c1<--c2<--c3<--c3'(main*)
c1<--c2<--c3<--c3'<--c4(main*)
```

## Moving work around
"Git" comfortable with modifying the source tree :P
It's a way for developers to say "I want this work here and that work there" in precise, eloquent, flexible ways.

#### 1. Cherrypick
`git cherry-pick <Commit1> <Commit2> <...>`
You would like to **copy a series of commits** below your current location (`HEAD`).

```

c1<--c2<--c3(main*)
      ^--c4<--c5<--c6(side)
```
We selectively want to pick commits `c4` and `c6` and add it below current `HEAD`.
on branch main: `git cherry-pick c4 c6`
```
c1<--c2<--c3<--c4'<--c6'(main*)
      ^--c4<--c5<--c6(side)
```

#### 2. Interactive rebase
Cherrypicking is good when we know which commits we need to copy, i.e. we know their hashed. But what about when we do not know which commits we are looking for?  
Interactive rebasing allows us to review a series of commits we are about to rebase.  
Using the `rebase` command with the `-i` option, it will open up a UI to show you which commits are about to be copied below the target of the rebase. It also shows their commit hashes and messages, which is great for getting a bearing on what's what.  
It is worth mentioning that in the **real git interactive rebase** you can do many more things like `squashing (combining) commits`, `amending commit messages`, and even `editing the commits` themselves.  

```
c0<--c1<--c2<--c3<--c4<--c5(main*, HEAD)

git rebase -i HEAD~4
This meand rebase current HEAD / main to HEAD~4 interactively.
Difference between current HEAD and HEAD~4(c1) => c2, c3, c4, c5
c2 - pick, after seeing what is in there
c3 - omit, after seeing what is in there
c4 - omit, after seeing what is in there
c5 - pick, after seeing what is in there
**order of the commits, commit messages, and more, can also be changed here**

c0<--c1<--c2'<--c5'(main*,HEAD)
      ^--c2<--c3<--c4<--c5
```
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
