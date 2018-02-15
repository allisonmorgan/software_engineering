# Github Pages & Jekyll: Overview

Github Pages helps Github users easily create and publish personal, project or organization webpages. As a user, Github will host a website for you for free at: `https://<username>.github.io`. The two most popular use cases include (1) hosting your own website, and (2) hosting a website for a project. 

#### Setting Up a Personal Webpage

First, [create a new repository](https://github.com/new) where the documents associated with your website will be stored. This repository will need to be named `<username>.github.io`. Once you've created this repository, then you can add and `index.html` file within the Github online UI, or via the command line as such:

```
git clone https://github.com/<username>/<username>.github.io
cd <username>.github.io
echo "Hello World" > index.html
```

The first line is reproducing the repository on your computer locally. The second navigates to the location of the repository, and the third creates an `index.html` file containing the single line "Hello World".

Then you'll need to commit and push these changes to the remote version of the repository. Just as we have done in class, this looks something like:
```
git add .
git commit -m "Initial commit"
git push origin master
```

Finally, visit `<username>.github.io` to see your new website! (The steps above drew heavily from [Github's own tutorial](https://pages.github.com) for setting up a person webpage.) Obviously, you can generate more personal content with slightly more sophisticated HTML and CSS. (I've provided some resources for HTML and CSS below.)

#### Setting Up a Project Webpage

You can also use Github Pages to host a webpage for one of your repositories. In order to do so, just navigate to the the project within the Github UI. Within the root directory for that repository, create an `index.html` file. Via the command line:

```
cd <repository>
echo "Hello World" > index.html
```

Then pushing these changes to the remote repository:
```
git add . 
git commit -m "Add Github Pages to repository"
git push origin master
```

Theres one last step before you can view your project's page. Within Github's web interface, navigate to the repository's settings, then to the "Github Pages" section. Choose a branch for Github Pages to look to. In the case above, we've pushed this webpage to the master branch, so select `master-branch` from the dropdown and hit "Save".

Now, visit `<username>.github.io/<repository>` to see your project's webpage. (Again, the steps above were inspired by [Github's own documentation](https://pages.github.com).)

### Jekyll 

[Jekyll](https://jekyllrb.com/docs/home/) is a "static site generator," essentially a program for turning raw text and Markdown files into HTML. You do not need to use Jekyll to create your website on Github (as I have shown above), it can make [some steps in the process easier](https://help.github.com/articles/about-github-pages-and-jekyll/).

For one, you can write your website in Markdown instead of HTML. Another plus is the ease of integration with Github. For example, you can easy [add a pre-designed theme](https://help.github.com/articles/adding-a-jekyll-theme-to-your-github-pages-site/) to your website, of which there are [many](https://help.github.com/articles/adding-a-jekyll-theme-to-your-github-pages-site-with-the-jekyll-theme-chooser/) to choose from.

### References

- Github Pages: 
	- [Tutorial](https://pages.github.com), [FAQ](https://help.github.com/categories/github-pages-basics/)
	- [HTML](https://www.codecademy.com/learn/learn-html) and [CSS](https://www.codecademy.com/learn/learn-css)

- Jekyll:
	- [Overview of Github and Jekyll](https://help.github.com/articles/about-github-pages-and-jekyll/)
	- [Using Jekyll](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)

Author: Allie Morgan (allison.morgan@colorado.edu)