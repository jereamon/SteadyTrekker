# Local workflow to publish
`make github`

Check `Makefile` to see what `make github` actually does. It should run `make publish`, use `ghp-import` to move contents of the output dir to the gh-pages branch, push that branch to github, and then run `make html` to bring the content back to its local development state.


# On Github Notes
In settings > pages, for the repo I set it to deploy from a branch and set that branch to gh-pages. Easy peasy.