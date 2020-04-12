#!/usr/bin/env python
import os
from os.path import splitext

CRAWL_BLACKLIST = ['.git','templates','src','scripts']

def chrootGitRepo():
    cwd = os.getcwd()
    while not os.path.isdir(os.path.join(cwd,'.git')):
        if (cwd == '/') or (cwd == 'C:\\'):
            return False
        os.chdir('..')
        cwd = os.getcwd()
    return cwd

def crawlCategories(gitRepoRoot):
    categoryTree = {}
    for p,n,f in os.walk(gitRepoRoot):
        # Remove directories in the crawl blacklist from consideration.
        firstLevelDir = p.replace(gitRepoRoot,'').split(os.path.sep)
        if len(firstLevelDir) >= 2:
            firstLevelDir = firstLevelDir[1]
        if firstLevelDir in CRAWL_BLACKLIST:
            continue
        # Remove hidden files and Gollum subpages from consideration.
        f = [fi for fi in f if not (fi.startswith('.') or fi.startswith('_'))]
        d = [os.path.join(os.path.basename(di),'Home.md') for di in n if os.path.basename(di) not in CRAWL_BLACKLIST]
        categoryTree[p] = f + d
    return categoryTree

def renderSidebar(categoryDir, categoryList, gitRepoRoot):
    sidebar = ''
    relativeCategoryPath = categoryDir.replace(gitRepoRoot,'')
    if categoryDir == gitRepoRoot:
        category = 'Home'
    else:
        category = os.path.basename(categoryDir) 
    sidebar+='# [[%s|%s]]\n' % (category.replace('-',' '), os.path.join(relativeCategoryPath, 'Home.md'))
    for page in categoryList:
        sidebar+=' * [[%s|%s]]\n' % (splitext(page)[0].replace('-',' ').replace('/Home',''), os.path.join(relativeCategoryPath,page))
    return sidebar

if __name__ == '__main__':
    gitRepoRoot = chrootGitRepo()
    categories = crawlCategories(gitRepoRoot)
    for k,v in categories.items():
        print(renderSidebar(k,v,gitRepoRoot))
        if k.strip() != gitRepoRoot.strip():
            with open(os.path.join(k,'Home.md'),'w') as f:
                f.write(renderSidebar(k,v,gitRepoRoot))
            if os.path.isfile(os.path.join(k,'_Sidebar.md')):
                os.remove(os.path.join(k,'_Sidebar.md'))
            os.link(os.path.join(k,'Home.md'),os.path.join(k,'_Sidebar.md'))
        else:
            with open(os.path.join(k,'_Sidebar.md'),'w') as f:
                f.write(renderSidebar(k,v,gitRepoRoot))
