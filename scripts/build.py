#!/usr/bin/env python
import os
from git import Repo
from glob import glob
import sys
from sh import pandoc

def getCategoryDict(gitRepoRoot, fileList):
    '''
    A function that iterates throught a list of files and then returns
    a dictionary with the directories for changed categories as keys, and a list 
    containing the pages belonging to those categories as values.
    '''
    categoryDict = {}
    for fi in fileList:
        # Ignore scripts directory.
        if os.path.dirname(fi) == "scripts":
            continue
        if not os.path.isdir(os.path.join(gitRepoRoot, os.path.dirname(fi))):
            continue
        # Remove hidden files, non-markdown files, and Gollum subpages from consideration.
        if (fi.startswith('.') or fi.startswith('_') or fi == "Home.md" and not fi.endswith('.md')):
            continue
        categoryPages = set(glob(os.path.join(gitRepoRoot, os.path.dirname(fi), '*.md')))
        # Needed in case the category is brand new.
        categoryPages.add(os.path.join(gitRepoRoot, os.path.dirname(fi), 'Home.md'))
        categoryPages = [os.path.basename(elm) for elm in categoryPages if not os.path.basename(elm).startswith('_') and not os.path.basename(elm).startswith('.')]
        categoryDict[os.path.join(gitRepoRoot,os.path.dirname(fi))] = categoryPages
    return categoryDict

def makeSidebar(categoryDir, categoryList, gitRepoRoot):
    sidebar = ''
    relativeCategoryPath = categoryDir.replace(gitRepoRoot.rstrip(os.path.sep),'')
    relativeCategoryPath = relativeCategoryPath.strip(os.path.sep)
    if categoryDir == gitRepoRoot:
        category = 'Home'
    else:
        category = os.path.basename(categoryDir) .replace('-',' ')
    sidebar+='### [%s](%s)\n' % (category, './Home.html')
    # Make sure we get subcategories in sidebar as well.
    dirglobbed = glob(os.path.join(categoryDir,"*"))
    for possibleDir in dirglobbed:
        if os.path.isdir(possibleDir) and os.path.basename(possibleDir) != "scripts":
            categoryList.append(os.path.join(os.path.basename(possibleDir),"Home.md"))
    categoryList = sorted(categoryList)
    for page in categoryList:
        # Ignore home
        if page == "Home.md":
            continue
        sidebar+=' * [%s](%s)\n' % (page.replace('.md','').replace("/Home","").replace('-',' '), page.replace('.md','.html'))
    return sidebar

def makeFooter(categoryDir, gitRepoRoot):
    footerList = []
    rootDistance = categoryDir.replace(gitRepoRoot.rstrip(os.path.sep), '').count(os.path.sep)
    rootDistance = [".."]*rootDistance
    rootLink = '[%s](%s)' % ('Home',os.path.join(os.path.sep.join(rootDistance),'Home.html'))
    if categoryDir == gitRepoRoot:
        footerList.append(rootLink)
    else:
        footerList.append(rootLink)
        relativeCategoryPath = categoryDir.replace(gitRepoRoot.rstrip(os.path.sep),'')
        relativeCategoryPath = relativeCategoryPath.strip(os.path.sep)
        treeElms = relativeCategoryPath.split(os.path.sep)
        treeElms = [treeElm for treeElm in treeElms if treeElm]
        treeNodes = []
        rootDistance = []
        while treeElms:
            rootDistance.append('..')
            lastElm = treeElms.pop()
            treeNodes.append('[%s](%s)' % (lastElm.replace('-',' '), os.path.join(os.path.sep.join(rootDistance),lastElm,'Home.html')))
        treeNodes = reversed(treeNodes)
        footerList+=treeNodes
    return ' **>** '.join(footerList)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Generate HTML with footers/headers from multiple markdown files using pandoc")
    parser.add_argument("-i", "--initialize", action="store_true", help="Regenerate all header and footer files.")
    parser.add_argument("-u", "--update", action="store_true", help="Regenerate only header and footer files for categories that were updated in the last commit.")
    args = parser.parse_args()

    # Sanity checks
    if args.initialize and args.update:
        print("You cannot both initialize and update the headers/footers.")
        print("Exiting now.")
        sys.exit(1)
    if not args.initialize and not args.update:
        print("You must specify an initialization or update operation.")
        print("Exiting now.")
        sys.exit(1)
   
    # Create the git repo object.  Find the root of the git repository and make an index object.
    gitRepo = Repo('.', search_parent_directories=True)
    gitRepoRoot = gitRepo.working_tree_dir
    srcRoot = os.path.join(gitRepoRoot, "src")
    
    # Only look at recently modified pages.
    fileList = []
    if args.update:
        fileList = list(gitRepo.head.commit.stats.files.keys())
        for fi in fileList:
            # If a file has moved just regenerate everything.
            if "=>" in fi:
                fileList = []

    if args.initialize or not fileList:
        for root, dirname, filenames in os.walk(srcRoot):
            for filename in filenames:
                fileList.append(os.path.join(root,filename))

    categories = getCategoryDict(srcRoot, fileList)

    for categoryDir,categoryPages in categories.items():
        categoryHTMLDir = categoryDir.replace(srcRoot,os.path.join(gitRepoRoot,"docs"))
        print(categoryHTMLDir)
        if not os.path.isdir(categoryHTMLDir):
            os.makedirs(categoryHTMLDir)
        # Make a footer for the changed category.
        footer = makeFooter(categoryDir, srcRoot)
        footerPath = os.path.join(categoryDir,'_Footer.md')
        footerPathHTML = os.path.join(categoryHTMLDir, '_Footer.html')
        with open(footerPath,'w') as f:
            f.write(footer)
        pandoc('-f','markdown','-t','html','-o', footerPathHTML, footerPath)
        
        # Make a sidebar for the changed category.
        # Also save the sidebar as a home/index page if we aren't at the
        # top of the repository.
        sidebar = makeSidebar(categoryDir,categoryPages,srcRoot)
        sidebarPath = os.path.join(categoryDir,'_Sidebar.md')
        sidebarPathHTML = os.path.join(categoryHTMLDir,'_Sidebar.html')
        indexPath = os.path.join(categoryHTMLDir,'index.html')
        if categoryDir.strip() != srcRoot.strip():
            with open(os.path.join(categoryDir,'Home.md'),'w') as f:
                f.write(sidebar)
            pandoc('-f','markdown','-t','html','-o',os.path.join(categoryHTMLDir,'Home.html'), os.path.join(categoryDir,'Home.md'))
            if not os.path.islink(sidebarPath) and os.path.exists(sidebarPath):
                os.remove(sidebarPath)
            if not os.path.islink(sidebarPath):
                os.symlink('Home.md',sidebarPath)
            if not os.path.islink(sidebarPathHTML) and os.path.exists(sidebarPathHTML):
                os.remove(sidebarPathHTML)
            if not os.path.islink(sidebarPathHTML):
                os.symlink('Home.html',sidebarPathHTML)
        else:
            with open(sidebarPath,'w') as f:
                f.write(sidebar)
            pandoc('-f','markdown','-t','html','-o',sidebarPathHTML, sidebarPath)

        # Render all pages with pandoc.
        for page in categoryPages:
            # No ToC for main page.
            if categoryDir.strip() == srcRoot.strip() and page == "Home.md":
                pandoc('-f','markdown','-t','html','-o',os.path.join(categoryHTMLDir, page.replace('.md','.html')),'--template=%s' % os.path.join(gitRepoRoot,"scripts","template","template.html"),'--include-after-body=%s' % footerPathHTML,'--include-before-body=%s' % sidebarPathHTML,'--metadata','title=%s' % page.replace('.md','').replace('-',' '), '--css',os.path.join(gitRepoRoot,"scripts","template","template.css"), '--self-contained',os.path.join(categoryDir,page))
            elif "Home.md" not in page:
                pandoc('-f','markdown','-t','html','-o',os.path.join(categoryHTMLDir, page.replace('.md','.html')),'--template=%s' % os.path.join(gitRepoRoot,"scripts","template","template.html"),'--include-after-body=%s' % footerPathHTML,'--include-before-body=%s' % sidebarPathHTML,'--toc','--toc-depth=2','--metadata','title=%s' % page.replace('.md','').replace('-',' '), '--css',os.path.join(gitRepoRoot,"scripts","template","template.css"), '--self-contained',os.path.join(categoryDir,page))

        # Make symlinks
        if categoryDir.strip() != srcRoot.strip():
            if not os.path.islink(indexPath) and os.path.exists(indexPath):
                os.remove(indexPath)
            if not os.path.islink(indexPath):
                os.symlink('Home.html',indexPath)
        else:
            if not os.path.islink(indexPath) and os.path.exists(indexPath):
                os.remove(indexPath)
            if not os.path.islink(indexPath):
                os.symlink('Home.html',indexPath)

