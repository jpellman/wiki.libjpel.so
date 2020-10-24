#!/usr/bin/env python
import os
from os.path import splitext
from git import Repo
from glob import glob
import sys

def getChangedCategories(gitRepo):
    '''
    A function that finds only recently changed markdown pages and then returns
    a dictionary with the directories for changed categories as keys, and a list 
    containing the pages belonging to those categories as values.
    '''
    # Only look at recently modified pages.
    lastModifiedFiles = list(gitRepo.head.commit.stats.files.keys())
    gitRepoRoot = gitRepo.working_tree_dir

    categoryDict = {}
    for fi in lastModifiedFiles:
        # Ignore scripts directory.
        if os.path.dirname(fi) == "scripts":
            continue
        if "=>" in fi:
            fi = fi.split(">")[1].strip("})
        if not os.path.isdir(os.path.join(gitRepoRoot, os.path.dirname(fi))):
            continue
        # Remove hidden files, non-markdown files, and Gollum subpages from consideration.
        if (fi.startswith('.') or fi.startswith('_')  and not fi.endswith('.md')):
            continue
        categoryPages = set(glob(os.path.join(gitRepoRoot, os.path.dirname(fi), '*.md')))
        # Needed in case the category is brand new.
        categoryPages.add(os.path.join(gitRepoRoot, os.path.dirname(fi), 'Home.md'))
        categoryPages = [os.path.basename(elm) for elm in categoryPages if not os.path.basename(elm).startswith('_') and not os.path.basename(elm).startswith('.')]
        categoryDict[os.path.join(gitRepoRoot,os.path.dirname(fi))] = categoryPages
    return categoryDict

def makeSidebar(categoryDir, categoryList, gitRepoRoot):
    sidebar = ''
    relativeCategoryPath = categoryDir.replace(gitRepoRoot,'')
    if categoryDir == gitRepoRoot:
        category = 'Home'
    else:
        category = os.path.basename(categoryDir) 
    sidebar+='# [%s](%s)\n' % (category.replace('-',' '), os.path.join(relativeCategoryPath, 'Home.md'))
    for page in categoryList:
        sidebar+=' * [%s](%s)\n' % (splitext(page)[0].replace('-',' ').replace('/Home',''), os.path.join(relativeCategoryPath,page))
    return sidebar

def makeFooter(categoryDir, gitRepoRoot):
    footerList = []
    rootLink = '[%s](%s)' % ('Home','/Home.md')
    if categoryDir == gitRepoRoot:
        footerList.append(rootLink)
    else:
        relativeCategoryPath = categoryDir.replace(gitRepoRoot,'')
        relativeCategoryPath = relativeCategoryPath.strip(os.path.sep)
        footerList.append(rootLink)
        treeElms = list(os.path.split(relativeCategoryPath))
        treeElms = [treeElm for treeElm in treeElms if treeElm]
        treeNodes = []
        while treeElms:
            lastElm = treeElms.pop()
            treeNodes.append('[%s](%s)' % (lastElm, os.path.join(*treeElms,lastElm,'Home.md')))
        treeNodes = reversed(treeNodes)
        footerList+=treeNodes
    return ' **>** '.join(footerList)

if __name__ == '__main__':
    # Create the git repo object.  Find the root of the git repository and make an index object.
    gitRepo = Repo('.', search_parent_directories=True)
    gitIndex = gitRepo.index
    gitRepoRoot = gitRepo.working_tree_dir

    # Get all changed categories and the pages that belong to them.
    categories = getChangedCategories(gitRepo)

    for categoryDir,categoryPages in categories.items():
        # Make a footer for the changed category.
        footer = makeFooter(categoryDir, gitRepoRoot)
        with open(os.path.join(categoryDir,'_Footer.md'),'w') as f:
            f.write(footer)
        
        # Make a sidebar for the changed category.
        # Also save the sidebar as a home/index page if we aren't at the
        # top of the repository and symlink "_Sidebar.md" to the Home/Index page.
        sidebar = makeSidebar(categoryDir,categoryPages,gitRepoRoot)
        sidebarPath = os.path.join(categoryDir,'_Sidebar.md')
        if categoryDir.strip() != gitRepoRoot.strip():
            with open(os.path.join(categoryDir,'Home.md'),'w') as f:
                f.write(sidebar)
            if not os.path.islink(sidebarPath) and os.path.exists(sidebarPath):
                os.remove(sidebarPath)
            if not os.path.islink(sidebarPath):
                os.link(os.path.join(categoryDir,'Home.md'),sidebarPath)
        else:
            with open(sidebarPath,'w') as f:
                f.write(sidebar)
