# Installation

* Clone from github
* Go to directory of files
* Run: `python3 -m venv venv`
* Run: `source venv/bin/activate`
* Run: `pip install --editable .`

# Usage

```
Usage: bagtoingest [OPTIONS] PATH

  Contruct Scholar@UC import template from BagIt manifest file

Options:
  --checksum TEXT     Type of manifest file to look for. Defaults to md5.
  --destination PATH  Location of output file; include trailing /. Defaults to
                      current directory.
  --help              Show this message and exit.
```
