# Git Style Guide

This Git Style Guide directly borrows, extends, and adapts from the following guides:

* [Git Style Guide by agis-](https://github.com/agis-/git-style-guide)
* [Git branch naming conventions by lovingly](http://www.guyroutledge.co.uk/blog/git-branch-naming-conventions/)
* [Branching by digitalijhelms](https://gist.github.com/digitaljhelms/4287848)

# Table of contents

1. [Branches](#branches)
2. [Commits](#commits)
  1. [Messages](#messages)
3. [Merging and Pull Requests](#merging)
4. [Issues](#issues)
5. [Stuff to check later](#misc)

# Branches

<table>
  <thead>
    <tr>
      <th>Instance</th>
      <th>Branch</th>
      <th>Description, Instructions, Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Master</td>
      <td>master</td>
      <td>Accepts merges from Develop and Hotfixes</td>
    </tr>
    <tr>
      <td>Develop</td>
      <td>develop</td>
      <td>Accepts merges from us/Issues and Hotfixes</td>
    </tr>
    <tr>
      <td>Task</td>
      <td>task/short-desc</td>
      <td>Always branch off HEAD of develop, it referes to an iteration task described on Trello.</td>
    </tr>
    <tr>
      <td>Hotfix</td>
      <td>hotfix/short-desc</td>
      <td>Always branch off Master, receives utmost priority for development, testing and code reviews. After merging and fixing Master in production it's changes get merged into Develop</td>
    </tr>
    <tr>
      <td>Issue</td>
      <td>issue/{{issue-id}}-short-desc</td>
      <td>Never branches off Master, it may branch from any other branch as necessary but primarily branches off  develop.</td>
    </tr>
    <tr>
      <td>Docs</td>
      <td>docs/short-desc</td>
      <td>Branches off develop, and will contain documentation that does not refer to any specific piece of code i.e. this guide.</td>
    </tr>
    <tr>
      <td>Refactoring</td>
      <td>refactoring/short-desc</td>
      <td>Branches off develop, this type of branch restructures an existing
      piece of code.</td>
    </tr>
  </tbody>
</table>

* Choose *short* and *descriptive* names:

  ```shell
  # good
  $ git checkout -b task/oauth-migration

  # bad - too vague
  $ git checkout -b task/login_fix
  ```

* Always follow the folder structure outlined above:

  ```shell
  # good
  $ git checkout -b issue/18-utf-enconding

  #bad
  $ git checkout -b fix-utf-encoding
  ```

* Always branch off from the allowed branches for each instance, as specified above:

  ``` shell
  #good
  $ git checkout -b task/database-table-creation develop

  #bad
  $ git checkout -b task/database-table-creation master
  ```

* Use *dashes* to separate words.

* Delete your branch from the upstream repository after it's merged, unless
  there is a specific reason not to.

 [How to delete a branch via de terminal](https://makandracards.com/makandra/621-git-delete-a-branch-local-or-remote)
 [How to delete a branch from the upstream repository via github's GUI](https://github.com/blog/1377-create-and-delete-branches)

  Tip: Use the following command while being on "master", to list merged
  branches:

  ```shell
  $ git branch --merged | grep -v "\*"
  ```

# Commits

* Each commit should be a single *logical change*. Don't make several
  *logical changes* in one commit. For example, if a patch fixes a bug and
  optimizes the performance of a feature, split it into two separate commits.

* Don't split a single *logical change* into several commits.

* Commit *early* and *often*. Small, self-contained commits are easier to
  understand and revert when something goes wrong.

* Before pushing make sure, your code passes your tests and is properly linted.

## Messages

* Write your commit messages in imperative present tense.

* Use the editor, not the terminal, when writing a commit message:

  ```shell
  # good
  $ git commit

  # bad
  $ git commit -m "Quick fix"
  ```

  This means just writing ```git commit``` instead of ```git commit -m``` your prefered editor will appear automatically, and your comment will be saved as soon as you close your editor.

  Committing from the terminal encourages a mindset of having to fit everything
  in a single line which usually results in non-informative, ambiguous commit
  messages. The ```git commit``` command defaults to vi; in case you are not familiar with vi, or prefer another text editor, follow [these instructions](https://help.github.com/articles/associating-text-editors-with-git/) in order to change your default editor.

* The summary line (ie. the first line of the message) should be
  *descriptive* yet *succinct*. Ideally, it should be no longer than
  *50 characters*. It should be capitalized and written in imperative present
  tense. It should not end with a period since it is effectively the commit
  *title*:

  ```shell
  # good - imperative present tense, capitalized, fewer than 50 characters
  Mark huge records as obsolete when clearing hinting faults

  # bad
  fixed ActiveModel::Errors deprecation messages failing when AR was used outside of Rails.
  ```

* After that should come a blank line followed by a more thorough
  description. It should be wrapped to *72 characters* and explain *why*
  the change is needed, *how* it addresses the issue and what *side-effects*
  it might have.

  It should also provide any pointers to related resources (eg. link to the
  corresponding issue in a bug tracker):

  ```text
  Short (50 chars or fewer) summary of changes

  More detailed explanatory text, if necessary. Wrap it to
  72 characters. In some contexts, the first
  line is treated as the subject of an email and the rest of
  the text as the body.  The blank line separating the
  summary from the body is critical (unless you omit the body
  entirely); tools like rebase can get confused if you run
  the two together.

  Further paragraphs come after blank lines.

  - Bullet points are okay, too

  - Use a hyphen or an asterisk for the bullet,
    followed by a single space, with blank lines in
    between

  Source http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
  ```

  Ultimately, when writing a commit message, think about what you would need
  to know if you run across the commit in a year from now.

* If *commit A* solves a bug introduced by *commit B*, it should
  also be stated in the message of *commit A*.

# Merging and Pull Requests

* When creating your pull request you will be prompted with a section where you will be able to name it, as well as adding a description. This section will be prefilled with the contents of the PULL_REQUEST_TEMPLATE.md, it'll look something like this.

![example of prefilled pull request description](https://help.github.com/assets/images/help/pull_requests/pr-template-sample.png)

For more information on templates refere to [github's documentation](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/)

* **Test and document before you push:** Do not pull request half-done work
* Create a pull request via the github online interface, fill the pull request template, and select the person that will code review your code.

* **Merge only after your pull request has been accepted**

* **Do not rewrite published history.** The repository's history is valuable in
  its own right and it is very important to be able to tell *what actually
  happened*. Altering published history is a common source of problems for
  anyone working on the project.

* However, there are cases where rewriting history is legitimate. These are
  when:

  * You are the only one working on the branch and it is not being reviewed.

  * You want to tidy up your branch (eg. squash commits) and/or rebase it onto
    the "master" in order to merge it later.

  That said, *never rewrite the history of the "master" branch* or any other
  special branches (ie. used by production or CI servers).

* Keep the history *clean* and *simple*. *Just before you merge* your branch:

    1. Make sure it conforms to the style guide and perform any needed actions
       if it doesn't (squash/reorder commits, reword messages etc.)

    2. Rebase it onto the branch it's going to be merged to:

      ```shell
      [my-branch] $ git fetch
      [my-branch] $ git rebase origin/master
      # then merge
      ```

      This results in a branch that can be applied directly to the end of the
      "master" branch and results in a very simple history.

      *(Note: This strategy is better suited for projects with short-running
      branches. Otherwise it might be better to occassionally merge the
      "master" branch instead of rebasing onto it.)*

* If merging from the terminal, do not merge with a
  fast-forward, (the merge pull request button on github is equivalent):

  ```shell
  # good - ensures that a merge commit is created
  $ git merge --no-ff my-branch

  # bad
  $ git merge my-branch
  ```

# Issues

* Use issues to report any bug, task or enhancement that needs to be done on the project that is not part of the current planning.

* By default you should use the issue template, but feel free to change it for your issue if appropirate.

# Stuff to check later

* Use [annotated tags](http://git-scm.com/book/en/v2/Git-Basics-Tagging#Annotated-Tags)
  for marking releases or other important points in the history. Prefer
  [lightweight tags](http://git-scm.com/book/en/v2/Git-Basics-Tagging#Lightweight-Tags)
  for personal use, such as to bookmark commits for future reference.

* Keep your repositories at a good shape by performing maintenance tasks
  occasionally:

  * [`git-gc(1)`](http://git-scm.com/docs/git-gc)
  * [`git-prune(1)`](http://git-scm.com/docs/git-prune)
  * [`git-fsck(1)`](http://git-scm.com/docs/git-fsck)

# License

![cc license](http://i.creativecommons.org/l/by/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution 4.0
International license](https://creativecommons.org/licenses/by/4.0/).
