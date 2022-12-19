import uvicorn
import typer
from fastapi import FastAPI

app = typer.Typer(
    name="xxx",
    add_completion=False,
    help="xxx",
)

app_fastapi = FastAPI(
    title="test",
)

@app_fastapi.get("/")
async def hello_world():
    return {"greeting": "Hello"}

@app.command()
def main(port: int = 5555):
    print("running at port: {port}")
    uvicorn.run(
        app_fastapi,
        port=port,
    )

if __name__ == "__main__":
    app()
    # main()
    # uvicorn.run(
        # app_fastapi, # port=port,
    # )