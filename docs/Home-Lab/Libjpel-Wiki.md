I recently switched from MoinMoin to Gollum for my personal wiki.  I'm using this page to list my justifications, as well as include any notes related to the transition.

# Reasons to Use Gollum Over MoinMoin

 * I was the only user of my wiki, which kind of goes against the spirit of a proper wiki in the first place.
 * My MoinMoin instance lived on a reserved AWS t3.micro instance, which was costing me more money than I thought was justifiable for what I was getting out of it (at least for this use case).  Since I already paid for a year upfront for this, I'm thinking of converting the reserved instance into a [BOINC machine](Systems-Administration/BOINCAMI).
 * Regardless of any security measures I took (i.e., using AWS security groups, changing the SSH port- this only really improves security marginally at the expense of usability and might not have been super necessary since AWS enforces the use of key pairs, but I did it anyways because I was the only person using the machine and it didn't hurt) I would still get pounded by brute force login attempts on the (public-facing) web app's login page.  I wanted to find a way to share my notes while not having to deal with bad actors at all, and having the wiki exist as a static site, with editing done locally on machines with Gollum installed, seemed like the best way to accomplish this.  Using a static site should pretty much get rid of the attack space entirely on my end- since I'm planning on serving this with a gh-pages branch, security becomes GitHub's problem and I'm okay with that.

# TODO

 * Find a way to convert Gollum pages into HTML automatically via a Travis job.  I was thinking about using [gollum-site](https://github.com/dreverri/gollum-site), but it seems moribund / hasn't been updated in 6 years and I don't trust it.  Most likely I'll use a Python script to convert Gollum-specific syntax into Markdown, and then use [Pandoc](https://pandoc.org/) to render HTML versions of all of the Markdown docs in wiki repository.
 * Find a way to automatically build a tree that people can navigate in the static site version.
 * Update any misc leftover MoinMoin syntax that is lingering about.
 * Remove the MoinMoin category designations at the end of some documents.  I'm thinking that I'll drop a Gollum footer file in each of the sub-directories within the wiki repo that contains representation of where you're at in the tree, and that will be rendered instead.
 * Fix sidebar and links on main page.
