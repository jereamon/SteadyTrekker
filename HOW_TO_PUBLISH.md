# Local workflow to publish
`make publish`
`ghp-import output`
`git push origin gh-pages`

# Local Notes
You can use `pelican content` or `make html` or `make publish`.

I'm not sure how `pelican content` is different from the other two.

But `make html` uses `pelicanconf.py` for settings
while `make publish` uses `publishconf.py` for settings.

`publishconf.py` imports everything from `pelicanconf.py` anyway.

### Why you use `make publish`
Ok, I'm a little confused. But basically, you need to use make publish when you publish
because I specified the site URL in there and without that none of the resources (css/js/images)
will have paths that can be found. So use `make publish` when you mean to publish!

The part I'm confused about is somehow everything still seems to 


## Important -- gh-pages branch
Using pip I installed the package: **ghp-import**.
When used it will copy the contents of a folder to the gh-pages branch.

Use it as such:
`ghp-import output`

Then push that branch:
`git push origin gh-pages`


# On Github Notes
In settings > pages, for the repo I set it to deploy from a branch and set that branch to gh-pages. Easy peasy.