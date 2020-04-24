#!/Users/jpellman/miniconda3/bin/python
import os
from os.path import splitext
from git import Repo
import sys

CRAWL_BLACKLIST = ['.git','template','src','scripts','config.rb']

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

def renderFooter(categoryDir, gitRepoRoot):
    footerList = []
    rootLink = '[[%s|%s]]' % ('Home','/Home.md')
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
            treeNodes.append('[[%s|%s]]' % (lastElm, os.path.join(*treeElms,lastElm,'Home.md')))
        treeNodes = reversed(treeNodes)
        footerList+=treeNodes
    return ' **>** '.join(footerList)

if __name__ == '__main__':
    gitRepoRoot = chrootGitRepo()
    gitRepo = Repo(gitRepoRoot)
    gitIndex = gitRepo.index
    commitMsg = 'Regenerate subpages'
    # Don't run post-hook if the last commit was a regeneration of subpages.
    # Otherwise, we'll get into an infinite loop.
    if gitRepo.head.commit.message == commitMsg:
        sys.exit(0)
    # Automatically add as post-commit hook if not already there.
    if gitRepoRoot:
        postCommitPath = os.path.join(gitRepoRoot,'.git','hooks','post-commit')
        if not os.path.islink(postCommitPath) and not os.path.isfile(postCommitPath):
            os.symlink(os.path.join('..','..','scripts',os.path.basename(__file__)),postCommitPath)
    categories = crawlCategories(gitRepoRoot)
    for k,v in categories.items():
        footer = renderFooter(k, gitRepoRoot)
        with open(os.path.join(k,'_Footer.md'),'w') as f:
            f.write(footer)
        sidebar = renderSidebar(k,v,gitRepoRoot)
        if k.strip() != gitRepoRoot.strip():
            with open(os.path.join(k,'Home.md'),'w') as f:
                f.write(sidebar)
            gitIndex.add([os.path.join(k,'Home.md')])
            if os.path.isfile(os.path.join(k,'_Sidebar.md')):
                os.remove(os.path.join(k,'_Sidebar.md'))
            os.link(os.path.join(k,'Home.md'),os.path.join(k,'_Sidebar.md'))
            gitIndex.add([os.path.join(k,'_Sidebar.md')])
        else:
            with open(os.path.join(k,'_Sidebar.md'),'w') as f:
                f.write(sidebar)
            gitIndex.add([os.path.join(k,'_Sidebar.md')])
    gitIndex.commit(commitMsg)
