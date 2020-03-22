#!/bin/bash
# Takes in Gollum wiki pages and renders them as a static site.

# Merge in changes from master
git merge master

# Iterate through every page, remove or convert Gollum-specific syntax
# and then render the page as HTML.
for PAGE in *.md;
do
	# Remove the table of contents tag.
	echo "Removing ToC for ${PAGE}"
	sed -i.bak -e "s/\[\[_TOC_.*\]\]//g" ${PAGE}
	echo "Rendering HTML for ${PAGE}"
	pandoc -f markdown -t html -o ${PAGE/md/html} --metadata title="${PAGE/.md/}" --template=templates/github/GitHub.html7 ${PAGE}
	# Remove the markdown file
	echo "Removing Markdown source for ${PAGE}"
	git rm -f ${PAGE}
done
git add *.html
rm *.bak
