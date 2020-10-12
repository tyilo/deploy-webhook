import yaml

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.post("/hook/{token}")
async def root(token: str):
    with open("data/tokens.yml") as f:
        tokens = yaml.safe_load(f)

    path = tokens.get(token)
    if not path:
        raise HTTPException(404, "Matching token does not exist.")

    with open("data/fifo", "w") as f:
        f.write(path)

    return {"success": True}
