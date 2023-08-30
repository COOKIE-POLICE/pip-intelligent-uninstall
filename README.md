# piu: Pip Intelligent Uninstall

piu is a command-line tool that helps you uninstall Python packages without breaking the dependencies of other packages. It shows you which packages can be safely removed and which ones are required by other packages. It also gives you the command to uninstall the packages with one line.

# Installation
You can install piu with pip:

```
pip install git+https://github.com/COOKIE-POLICE/pip-intelligent-uninstall.git
```

# Usage
You can use piu with any package name that you have installed with pip. For example, if you want to uninstall pytest, you can type:

```
piu uninstall pytest
```

This will show you something like this:

```
You cannot uninstall: packaging, colorama (Other packages depend on them)
You can uninstall: iniconfig, pluggy, pytest (Other packages do not depend on them)

Do you want to proceed to uninstall the packages: iniconfig, pluggy, pytest? [y/N]:
```

# License

piu is licensed under the MIT license. See the LICENSE file for more details.


