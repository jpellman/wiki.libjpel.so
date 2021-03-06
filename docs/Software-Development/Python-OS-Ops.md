

Common Unix Command Line Operations and Their Python Equivalents
================================================================

Learning by analogy.

| Unix Command Line Operation | Python Operation |
| --------------------------- | ---------------- |
| pwd | https://docs.python.org/2/library/os.html#os.getcwd|os.getcwd() |
| cd | https://docs.python.org/2/library/os.html#os.chdir|os.chdir(path) |
| mkdir | https://docs.python.org/2/library/os.html#os.mkdir|os.mkdir(path,mode) |
| mkdir -p | https://docs.python.org/2/library/os.html#os.makedirs|os.makedirs(path,mode) (sort of; raises error if dir already exists so you need to check first) |
| rm | https://docs.python.org/2/library/os.html#os.remove|os.remove(path) |
| rmdir | https://docs.python.org/2/library/os.html#os.rmdir|os.rmdir(path) or https://docs.python.org/2/library/os.html#os.removedirs|os.removedirs(path) to remove empty directories recursively |
| rm -r | https://docs.python.org/2/library/shutil.html#shutil.rmtree|shutil.rmtree(path) |
| mv | https://docs.python.org/2/library/os.html#os.rename|os.rename(source,target) |
| ln | https://docs.python.org/2/library/os.html#os.link|os.link(source,target) |
| ln -s | https://docs.python.org/2/library/os.html#os.symlink|os.symlink(source,target) |
| echo $VAR | https://docs.python.org/2/library/os.html#os.getenv|os.getenv('VAR') |
| export VAR=foo | https://docs.python.org/2/library/os.html#os.putenv|os.putenv('VAR','foo') |
| ls | https://docs.python.org/2/library/subprocess.html#subprocess.check_output|subprocess.check_output('ls') |
| ls -l | https://docs.python.org/2/library/subprocess.html#subprocess.check_output|subprocess.check_output('ls','-l') |
| chmod <octal_mode or ugo shortcuts> <path>| https://docs.python.org/2/library/os.html#os.chmod|os.chmod(path,https://docs.python.org/2/library/stat.html#stat.S_ISUID|mode) |
| cp | https://docs.python.org/2/library/shutil.html#shutil.copy|shutil.copy(source,destination) |
| cp -p | https://docs.python.org/2/library/shutil.html#shutil.copy2|shutil.copy2(source,destination) |
| cp -r | https://docs.python.org/2/library/shutil.html#shutil.copytree|shutil.copytree(source,destination) |
| date | datetime |
| ps, top | psutil |

Generally useful: [shlex.split](https://docs.python.org/2/library/shlex.html#shlex.split)

