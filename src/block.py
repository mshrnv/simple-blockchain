"""Block node Module"""
import json
from prettytable import PrettyTable


class Block:
    """Block node class"""

    def __init__(
        self,
        mining_complexity: int,
        counter: int,
        mined_time: int,
        prev_hash: str,
        hash_: str,
        nonce: str,
        data: dict,
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
        self.__mining_complexity = mining_complexity
        self.__mined_time = mined_time
        self.__hash = hash_
        self.__nonce = nonce
        self.__data = data

    def pretty_print(self) -> None:
        """Prints table with block data"""
        table = PrettyTable()
        table.field_names = [f"Block: {self.__counter}"]
        table.add_row([f"Time: {self.__mined_time}"])
        table.add_row([f"Hash: {self.__hash}"])
        table.add_row([f"Nonce: {self.__nonce}"])
        table.add_row([f"Prev: {self.__prev_hash}"])
        table.add_row(["Transaction: Transaction"])

        print(table)

    def get_data(self) -> dict:
        """Returns block data dict

        Returns:
            dict: Block data
        """
        data = {
            # "counter": self.__counter,
            # "source": self.__source,
            # "destination": self.__destination,
            # "amount": self.__amount,
            # "prev_hash": self.__prev_hash,
            # "hash": self.__hash,
            # "mining_complexity": self.__mining_complexity,
            # "timestamp": self.__timestamp,
        }

        return data

    def get_counter(self) -> int:
        """Counter property"""
        return self.__counter

    def get_hash(self) -> str:
        """__hash property"""
        return self.__hash

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
