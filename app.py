r"""```bash
Serve ezbee via post port default 5555
In: [str, str]
Out: List[Tuple[str, str, str]]

Tests:
curl -X 'POST' \
  'http://127.0.0.1:5555/post/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text1": "string",
  "text2": "string"
}'

res = httpx.post("http://127.0.0.1:5555/post/", json={'text1': 'a', 'text2': 'b'})
# res.json() = {'res': [['a', 'b', ''], ['c', 'c', '0.5']]}

x httpx.post("http://127.0.0.1:5555/post/", json=['a', 'b']).json()
httpx.post("http://127.0.0.1:5555/post/", json={'texts': ['a', 'b']}).json()

var r = await axios.post(`http://127.0.0.1:5555/post/`, { text1: 'a', text2: 'b' })
var r = await axios.post(`http://127.0.0.1:5555/post/`, { texts: ['a', 'b'] })
r.data
// { res: [ [ 'a', 'b', '' ], [ 'c', 'c', '0.5' ] ] }
```
"""
# pylint: disable=invalid-name
# sanic sanic-app:app or sanic sanic-app.app
# http://127.0.0.1:8000
# from icecream import ic
# pylint: disable=invalid-name
import json
import os
import sys
from argparse import Namespace  # from types import SimpleNamespace
from pathlib import Path

# import signal
# from signal import SIG_DFL, SIGINT, signal
from typing import List, Optional, Tuple, Union

import logzero
import uvicorn
from logzero import logger
from set_loglevel import set_loglevel

logzero.loglevel(set_loglevel())

# from sanic.log import logger

# from sanic import Sanic, response
# from sanic.response import text
# from sanic.exceptions import ServerError, NotFound

# from time import sleep
from ezbee import ezbee
from ezbee.gen_pairs import gen_pairs
from ezbee.save_xlsx_tsv_csv import save_xlsx_tsv_csv
from fastapi import FastAPI
from pydantic import BaseModel

from dezrest import __version__

# app = Sanic("MyHelloWorldApp")
debug = True
port = 5555

app = FastAPI(
    title="dezbee-rest",
    version=__version__,
    description=f"{__doc__}",
)


@app.get("/")
async def hello_world():
    # ic(request)
    # ic(request.args)
    # return text("Hello, world.")
    return {"greetings": "Hello from dezbee-rest"}


class Texts(BaseModel):
    # text1: str
    # text2: str
    __root_: Tuple[str, str]


class ThreeCols(BaseModel):
    __root__: List[Tuple[str, str, Union[str, float]]]


# @app.post("/post/", response_model=ThreeCols)
# def on_post(texts: Texts):


@app.post("/post/", response_model=List[Tuple[str, str, str]])
def on_post(texts: Tuple[str, str]):
    """Deliver aligned pairs.

    ```
    Request body: [str, str]

    Response model: List[Tuple[str, str, str]]
    """
    # logger.debug(" d texts: %s", texts)

    text1, text2 = texts
    lists = text1.splitlines(), text2.splitlines()

    # list1, list2 = text1.splitlines(), text2.splitlines()
    # logger.debug("type(list1): %s, list1[:5]: %s", type(list1), list1[:5])
    # logger.debug("type(list2): %s, list2[:5]: %s", type(list2), list2[:5])

    # aset = ezbee(lines1, lines2)
    # aset = ezbee(list1, list2)

    aset = ezbee(*lists)

    logzero.loglevel(set_loglevel())
    if aset:
        logger.debug("aset: %s...%s", aset[:4], aset[-4:])
        # logger.debug("aset: %s", aset)

    # aligned_pairs = gen_pairs(list1, list2, aset)
    aligned_pairs = gen_pairs(*lists, aset)

    logger.debug("aligned_pairs[:10]: %s", aligned_pairs[:10])

    return aligned_pairs

    _ = """
    return [
        ['a', 'b', ''],
        ['c', 'd', .5],
    ]
    # """


if __name__ == "__main__":
    # sanic sanic-app:app -p 7777 --debug --workers=2
    # or python sanic-app.py  # production-mode
    #
    # app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)  # dev=True
    # app.run(host="0.0.0.0", port=8000, auto_reload=True)
    # dev = True

    # app.run(port=port, auto_reload=True, workers=2, debug=debug)

    # uvicorn app:app --host 0.0.0.0 --port 5555
    # curl http://127.0.0.1:5555
    # curl -XPOST http://127.0.0.1:5555/post/ -H "accept: application/json" -H "Content-Type: application/json" -d "{\"text1\": \"a b c\", \"text2\": \"d e f\"}"

    uvicorn.run(
        "app:app",
        # host='0.0.0.0',
        # host='127.0.0.1',
        port=port,
        reload=True,
        # workers=2,
        # debug=True,
        # timeout_keep_alive65,
        log_level=10,
    )
