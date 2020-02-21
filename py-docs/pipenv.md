# pipenv

`Virtualenv` gives you the low-level visualization feature with basic environmental isolation. However it lacks others features of a full-fledged package manager, That is where the Pipenv comes in. It has a host of features that can create and manage packages for complex projects at scale. I will go into it in brief as the documentation for pipenv is pretty easy to read and well written.

## Installation and Basic usage

`Pipenv` stores all the package information in a file called `Pipfile` and `Pipfile.lock` which has all the details of packages, versions, and source(Pypi or custom Github source).

A simple example of `Pipfile` and `Pipfile.lock` is given below (Edited version from the documentation)

`Pipfile`

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"
​
[packages]
numpy = "*"
​
[dev-packages]
pytest = "*"
```

`Pipfile.lock`: (My `Pipfile.lock` after creating a fresh Pipenv environment and installing `numpy`)

```json
{
    "_meta": {
        "hash": {
            "sha256": "532f630f67db39ae5920f79895733204f9869909ded64df233d99611b657a39c"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "2.7"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "numpy": {
            "hashes": [
                "sha256:1980f8d84548d74921685f68096911585fee393975f53797614b34d4f409b6da",
                "sha256:22752cd809272671b273bb86df0f505f505a12368a3a5fc0aa811c7ece4dfd5c",
                "sha256:23cc40313036cffd5d1873ef3ce2e949bdee0646c5d6f375bf7ee4f368db2511",
                ....
            ],
            "index": "pypi",
            "version": "==1.16.2"
        }
    },
    "develop": {}
}
```

```
$ pip install pipenv
```

```
$ mkdir env_experiments
$ cd env_experiments
```

You can now use pipenv install to setup an existing environment using a pipfile or it creates a new pipfile for you. If you only have a requirements.txt file available in the same folder when running pipenv install, pipenv will automatically import the contents of requirements.txt file.

```
$ pipenv install
```

Work on virtual environment.

```
$ pipenv shell
```

## Installing and running packages

```
$ pipenv install "requests>=1.4"   # will install a version equal or larger than 1.4.0
$ pipenv install "requests<=2.13"  # will install a version equal or lower than 2.13.0
$ pipenv install "requests>2.19"   # will install 2.19.1 but not 2.19.0
```

## Upgrading packages

```
$ pipenv update <package_name>
```

check if there are any updates

```
$ pipenv update --outdated
```

Uninstalling

```
$ pipenv uninstall <package-name>

$ pipenv uninstall --all
$ pipenv uninstall --all-dev
```

## Specifying Python version

```
$ pipenv --python version_number
```

```
$ pipenv --python 3 # Creates Python3 environment
$ pipenv --python 3.6 # Createst Python 3.6 environments
```

When given a Python version, like this, Pipenv will automatically scan your system for a Python that matches that given version.

If a Pipfile hasn't been created yet, one will be created for you, otherwise, the python version information will be appended at the end of the existing Pipfile that looks like this:

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
​
[dev-packages]
​
[packages]
​
[requires]
python_version = "3.6"
```

## pipenv lock

`$ pipenv lock` is used to create a `Pipfile.lock`, which declares all dependencies (and sub-dependencies) of your project, their latest available versions, and the current hashes for the downloaded files. This ensures repeatable, and most importantly deterministic, build.
