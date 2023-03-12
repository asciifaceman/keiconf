# keiconf

[![PyPI - Version](https://img.shields.io/pypi/v/keiconf.svg)](https://pypi.org/project/keiconf)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/keiconf.svg)](https://pypi.org/project/keiconf)
[![Hatch - Version](https://img.shields.io/badge/hatch-1.6.3-success)](https://github.com/pypa/hatch)

![Repo - PRs](https://img.shields.io/github/issues-pr-raw/asciifaceman/keiconf)
![Repo - Issues](https://img.shields.io/github/issues-raw/asciifaceman/keiconf)

A small, minimalist application json configuration tool for small projects.

-----

**Table of Contents**

- [Why tho?](#why-tho)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [License](#license)

## Why tho?
Fair question.

I originally started this project as an excuse to use Hatch and write a pyproject.toml no-distutils/setuptools python project and see how green the grass was.

I've typically been unhappy with the configuration options for python in a way I can't articulate very well, and I just wanted a simple json file read with some guiderails. Some quick user-side discovery to find my platform's config path and get going.

This project isn't meant to be a fully featured configuration system to slap into your next big webservice, it's just a small system to slap on your next prototype or small project. 

## Installation

```console
pip install keiconf
```

## Usage

Coming Soon

```
from keiconf import KeiConf

k = KeiConf(filepath="path/to/file.json")


```

## Development
Development/Testing/Contribution requires hatch. Hatch provides the project management, environment abstraction, dependency resolution, and dev/test entrypoints. 

```
python3 -m pip install hatch
```

although it is recommended to install hatch via pipx

```
python3 -m pip install pipx
python3 -m pipx ensurepath
python3 -m pipx install hatch
```

## License

`keiconf` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
