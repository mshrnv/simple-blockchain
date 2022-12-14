"""Block node Module"""
from datetime import datetime
from hashlib import sha256
from prettytable import PrettyTable
import json


class Block:
    """Block node class"""

    def __init__(
        self,
        counter: int,
        prev_hash: str,
        source: str,
        destination: str,
        amount: float,
        mining_complexity: int,
        timestamp: int,
        hash: str,
    ):
        """Default initialization

        Args:
            counter (int): Number of node
            prev_hash (str): Hash of previous block
            source (str): Source address
            destination (str): Destination address
            amount (float): Amount of transaction
            mining_complexity (int): Complexity of mining
            timestamp (int): Timestamp
            hash (str): Hash of block
        """
        self.__counter = counter
        self.__prev_hash = prev_hash
        self.__source = source
        self.__destination = destination
        self.__amount = amount
        self.__mining_complexity = mining_complexity
        self.__timestamp = timestamp
        self.__hash = self.hash

    # def __hash__(self) -> str:
    #     to_hash_string = (
    #         self.__prev_hash
    #         + self.__source
    #         + self.__destination
    #         + str(self.__amount)
    #         + str(self.__timestamp)
    #     )

    #     return sha256(to_hash_string.encode("utf-8")).hexdigest()

    def pretty_print(self) -> None:
        table = PrettyTable()
        table.field_names = ["Field", "Value"]
        table.title = f"Block №{self.__counter}: {self.__hash}"
        table.add_row(["Source", self.__source])
        table.add_row(["Destination", self.__destination])
        table.add_row(["Amount", self.__amount])
        table.add_row(["Date", self.__timestamp.strftime("%m/%d/%Y, %H:%M:%S")])

        print(table)

    def get_data(self) -> dict:
        data = {
            "counter": self.__counter,
            "source": self.__source,
            "destination": self.__destination,
            "amount": self.__amount,
            "prev_hash": self.__prev_hash,
            "hash": self.__hash,
            "mining_complexity": self.__mining_complexity,
            "timestamp": self.__timestamp,
        }

        return data

    def serialize(self) -> str:
        json_data = json.dumps(data)
        return json_data

    @staticmethod
    def deserialize(self, serialized_data: str) -> dict:
        data = json.loads(serialized_data)
        return data
