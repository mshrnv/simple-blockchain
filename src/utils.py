"""Utils Module"""
from datetime import datetime
from time import time
from hashlib import sha256
from merkle import MerkleTree


def get_time() -> str:
    """Returns current datetime

    Returns:
        str: Datetime in needle format
    """
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time


def get_merkle_root(values: list) -> str:
    """Returns root of merkle tree"""
    mtree = MerkleTree(values)
    return mtree.get_root_hash()


def find_hash(mining_complexity, index, prev_hash, txs) -> tuple:
    """Mining"""
    target = "0" * mining_complexity
    header = str(index) + prev_hash + get_merkle_root(txs)

    start = time()
    for i in range(384993400, 0, -1):
        block_hash = sha256((header + str(i)).encode("utf-8")).hexdigest()
        print(f"Mining... {block_hash}")
        if block_hash[:mining_complexity] == target:
            end = time()
            print("Success!")
            print(f"Elapsed time: ~{end - start} seconds")

            result = {"hash": block_hash, "i": str(i)}

            return result

    print("Mining failed...")
    return {"hash": "", "i": ""}
