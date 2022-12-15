"""REST API Module"""
import uvicorn
from fastapi import FastAPI
import utils
from blockchain import Blockchain


app = FastAPI()
blockchain = Blockchain()


@app.get("/")
def get_root():
    """Default method"""
    return {"status": "ok"}


@app.get("/blockchain")
def get_blockchain() -> dict:
    """Returns list of all blocks into chain"""
    return {
        "data": blockchain.get_blockchain(),
        "length": blockchain.get_latest_block().get_counter() + 1,
    }


@app.post("/new_block/")
def new_block(source: str, destination: str, amount: float, difficulty: int):
    """New block generation"""

    data = {
        "source": source,
        "destination": destination,
        "amount": amount,
    }

    last_block_hash = blockchain.get_latest_block().get_hash()
    last_block_index = blockchain.get_latest_block().get_counter()

    nonce = utils.find_hash(
        difficulty, last_block_index + 1, last_block_hash, data.values()
    )

    is_block_added = blockchain.add_block(
        difficulty,
        last_block_index + 1,
        utils.get_time(),
        last_block_hash,
        nonce["hash"],
        nonce["i"],
        data,
    )

    return {"status": f"{is_block_added}"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
