# sanic sanic-app:app or sanic sanic-app.app
# http://127.0.0.1:8000
# from icecream import ic
import logzero
from logzero import logger
logzero.loglevel(10)

# from sanic.log import logger

from sanic import Sanic, response
from sanic.response import text
from sanic.exceptions import ServerError, NotFound

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
    # ic(request)
    # ic(request.args)
    return text("Hello, world.")


# https://www.geeksforgeeks.org/introduction-to-sanic-web-framework-python/
@app.route("/post", methods =['POST'])
def on_post(request):
    # ic(request)
    # ic(request.json)
    logger.debug(request.json)
    try:
        if request.json is None:
            logger.warning(" no data in workload ")
            raise Exception(" no data received, dont know how to proceed without data ")
        return response.json({"content": request.json})
    except Exception as ex:
        import traceback
        # logger.error(f"{traceback.format_exc()}")
        raise ServerError(f"{ex}", status_code=500)

if __name__ == '__main__':
    # sanic sanic-app:app -p 7777 --debug --workers=2
    # or python sanic-app.py  # production-mode
    # 
    # app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)  # dev=True
    # app.run(host="0.0.0.0", port=8000, auto_reload=True)
    # dev = True
    
    debug = True
    port = 7776
    app.run(port=port, auto_reload=True, workers=2, debug=debug)
    