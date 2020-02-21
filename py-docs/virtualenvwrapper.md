# virtualenvwrapper

## Install and setup `virtualenvwrapper`

```
$ pip install virtualenvwrapper

$ export WORKON_HOME=~/Envs

$ source /usr/local/bin/virtualenvwrapper.sh
```

when you execute the `export WORKON_HOME=~/Envs` command, it will place all the future virtual environments created using `virtualenv` wrappers in `~/Envs` folder.

## Creating and working with a project

Create a virtual environment in `~/Envs`

```
$ mkvirtualenv project_folder
```

Work on a virtual environment

```
$ workon project_folder
```

Alternatively, you can make a project, which creates the virtual environment, and also a project directory inside `$WORKON_HOME`, which is cd-ed into when you workonproject_folder.

```
$ mkproject project_folder
```

virtualenvwrapper provides tab-completion on environment names. It helps when you have many environments and have trouble remembering their names.

`workon` also deactivates whatever environment you are currently in, so you can quickly switch between environments.

- Deactivating is still the same:

```
$ deactivate
```

- To delete:

```
$ rmvirtualenv venv
```
