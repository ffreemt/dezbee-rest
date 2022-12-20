# dezbee-rest
[![pytest](https://github.com/ffreemt/dezbee-rest/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dezbee-rest/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dezrest.svg)](https://badge.fury.io/py/dezrest)

Serve [de|ez|dz]bee via FastAPI port 6666

## python 3.8 only

## Pre-install for Windows without C++ environment
Ignore this step if your system has C++, e.g., Visual Studio or mingw

* fasttext
  * `pip install fasttext` (linux) or `pip install fasttext*whl` (Windows)
* pycld2, PyICU
  * e.g. `poetry run pip install pycld2-0.41-cp38-cp38-win_amd64.wh PyICU-2.9-cp38-cp38-win_amd64.whl`
* polyglot fix:
  * `poetry run pip install -U git+https://github.com/aboSamoor/polyglot.git@master` or
  *  `pip install artifects\polyglot-16.7.4.tar.gz` (modified cloned polyglot: futures removed from requirements.txt)
* scikit-learn (for deprecated sklearn used in some packages) and pybind11 (for Windows)

Refer to [workflows](https://github.com/ffreemt/dezbee-rest/blob/main/.github/workflows/routine-tests.yml)

## Install it (Python 3.8 only)

##
```shell
pip install dezrest

# pip install git+https://github.com/ffreemt/dezbee-rest
# poetry add git+https://github.com/ffreemt/dezbee-rest
# git clone https://github.com/ffreemt/dezbee-rest && cd dezbee-rest
```

You may wish to create a python virutal environment first, e.g.,
```
mkdir temp-dir && cd temp-dir
py -3.8 -m venv .venv
call .venv\Scripts\activate
pip install dezrest
```

## Use it

```bash
# sart the server at port 5555 via `uvicorn` with 2 workers
python -m dezrest

# or
dezrest

# or run at external IP
python -m dezrest --host 0.0.0.0

# or dezrest --host 0.0.0.0

# cli help
python -m dezrest --help

# or
dezrest --help

# REST docs (Swagger UI)
http://127.0.0.1:5555/docs

```

### Sample run:
```
$ dezrest
[D 221220 10:48:21 fastlid:34] fetching lid.176.ftz (once only)
[I 221220 10:48:22 fastlid:44] Downloading https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz (need to do this just once)
[I 221220 10:48:27 __main__:204]  pid: C:\mat-dir\playground\venv-python
INFO:     Uvicorn running on http://127.0.0.1:5555 (Press CTRL+C to quit)
INFO:     Started parent process [486952]
INFO:     Started server process [548488]
INFOINFO:     Started server process [:     Waiting for application startup.
547296]
INFOINFO:     Application startup complete.
:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:7114 - "POST /post/ HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [547296]
```

To kill the server, kill the parent process (CTRL+C does not quite work), e.g.
```
taskkill /f /pid 486952 /pid 548488
```

### Test the REST API:
```python
import httpx
res = httpx.post("http://127.0.0.1:5555/post/", json=["test\nlove", "没有\n测试\n其他\n爱"]).json()
print(res)
# [['', '没有', ''], ['test', '测试', '0.75'], ['', '其他', ''], ['love', '爱', '0.87']]

```