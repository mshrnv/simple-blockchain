"""Block node Module"""
import json
from prettytable import PrettyTable


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
        hash_: str,
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
        self.__hash = hash_

    def pretty_print(self) -> None:
        """Prints table with block data"""
        table = PrettyTable()
        table.field_names = ["Field", "Value"]
        table.title = f"Block №{self.__counter}: {self.__hash}"
        table.add_row(["Source", self.__source])
        table.add_row(["Destination", self.__destination])
        table.add_row(["Amount", self.__amount])
        table.add_row(["Date", self.__timestamp.strftime("%m/%d/%Y, %H:%M:%S")])

        print(table)

    def get_data(self) -> dict:
        """Returns block data dict

        Returns:
            dict: Block data
        """
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
        """Data dict to JSON serialization

        Returns:
            str: Serialized data
        """
        data = self.get_data()
        json_data = json.dumps(data)
        return json_data

    @staticmethod
    def deserialize(serialized_data: str) -> dict:
        """JSON to dict deserialization

        Args:
            serialized_data (str): Serialized data

        Returns:
            dict: Data dict
        """
        data = json.loads(serialized_data)
        return data
