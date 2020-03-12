

Common Unix Command Line Operations and Their Python Equivalents
================================================================

Learning by analogy.

| Unix Command Line Operation | Python Operation |
| --------------------------- | ---------------- |
| pwd | http/docs.python.o2/libraos.html#os.getcwd|os.getcwd() |
| cd | http/docs.python.o2/libraos.html#os.chdir|os.chdir(path) |
| mkdir | http/docs.python.o2/libraos.html#os.mkdir|os.mkdir(path,mode) |
| mkdir -p | http/docs.python.o2/libraos.html#os.makedirs|os.makedirs(path,mode) (sort of; raises error if dir already exists so you need to check first) |
| rm | http/docs.python.o2/libraos.html#os.remove|os.remove(path) |
| rmdir | http/docs.python.o2/libraos.html#os.rmdir|os.rmdir(path) or http/docs.python.o2/libraos.html#os.removedirs|os.removedirs(path) to remove empty directories recursively |
| rm -r | http/docs.python.o2/librashutil.html#shutil.rmtree|shutil.rmtree(path) |
| mv | http/docs.python.o2/libraos.html#os.rename|os.rename(source,target) |
| ln | http/docs.python.o2/libraos.html#os.link|os.link(source,target) |
| ln -s | http/docs.python.o2/libraos.html#os.symlink|os.symlink(source,target) |
| echo $VAR | http/docs.python.o2/libraos.html#os.getenv|os.getenv('VAR') |
| export VAR=foo | http/docs.python.o2/libraos.html#os.putenv|os.putenv('VAR','foo') |
| ls | http/docs.python.o2/librasubprocess.html#subprocess.check_output|subprocess.check_output('ls') |
| ls -l | http/docs.python.o2/librasubprocess.html#subprocess.check_output|subprocess.check_output('ls','-l') |
| chmod <octal_mode or ugo shortcuts> <path>| http/docs.python.o2/libraos.html#os.chmod|os.chmod(path,http/docs.python.o2/librastat.html#stat.S_ISUID|mode) |
| cp | http/docs.python.o2/librashutil.html#shutil.copy|shutil.copy(source,destination) |
| cp -p | http/docs.python.o2/librashutil.html#shutil.copy2|shutil.copy2(source,destination) |
| cp -r | http/docs.python.o2/librashutil.html#shutil.copytree|shutil.copytree(source,destination) |
| date | datetime |
| ps, top | psutil |

Generally useful: [shlex.split](http/docs.python.o2/librashlex.html#shlex.split)

* * * * *

> Python
