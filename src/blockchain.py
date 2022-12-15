"""Blockchain Module"""
from hashlib import sha256
import utils
from block import Block


class Blockchain:
    """Blockchain Class"""

    __blockchain = []

    def __init__(self):
        data = {
            "source": "Genesis",
            "destination": "Genesis",
            "amount": "Genesis",
        }
        genesis_hash = "000000000000000000000000000000000000000001"
        nonce = utils.find_hash(2, 0, genesis_hash, data)
        self.__blockchain.append(
            Block(2, 0, utils.get_time(), genesis_hash, nonce["hash"], nonce["i"], data)
        )

    def get_latest_block(self) -> Block:
        """Returns latest block"""
        return self.__blockchain[-1]

    def print(self) -> None:
        """Prints all blocks"""
        for block in self.__blockchain:
            block.pretty_print()

    def add_block(
        self,
        mining_complexity: int,
        counter: int,
        mined_time: str,
        prev_hash: str,
        hash_: str,
        nonce: str,
        data: dict,
    ) -> bool:
        """Appends block into blockhain

        Args:
            mining_complexity (int): Number of '0' at the start position
            counter (int): Number of block
            mined_time (str): Mining time
            prev_hash (str): Hash of previous block
            hash_ (str): Hash of block
            nonce (str): Nonce
            data (dict): Data into block (source, dest, amount)
        """
        target = "0" * mining_complexity
        header = str(counter) + prev_hash + utils.get_merkle_root(data.values()) + nonce

        if (
            sha256(header.encode("utf-8")).hexdigest() == hash_
            and hash_[:mining_complexity] == target
            and counter == len(self.__blockchain)
        ):
            self.__blockchain.append(
                Block(
                    mining_complexity,
                    counter,
                    mined_time,
                    prev_hash,
                    hash_,
                    nonce,
                    data,
                )
            )
            return True

        print("[Error] -> add_block")
        return False

    def get_blockchain(self):
        """Blockchain property"""
        return self.__blockchain


# bc = Blockchain()
# bc.print()
