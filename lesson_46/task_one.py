"""Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data. The input should ask for :

- database name
- collection name
- field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , 
then value is number (float, int) which is random number from a(min) to b(max) )
- number o documents to create.
"""
from pymongo import MongoClient
from typing import Dict, Any, List, Optional, Union
import random
from random_word import RandomWords


def choice_cli() -> int:
    while True:
        try:
            valide_inputs = [1, 2]
            choice = int(input("Enter your choice (1-2): "))
            if choice in valide_inputs:
                return choice
        except ValueError:
            print("You have to input numer between 1 and 2!")
            continue


def get_database_name() -> str:
    return input("Enter database name: ")


def get_collection_name() -> str:
    return input("Enter collection name: ")


def get_number_of_fields() -> int:
    return int(input("Enter number of fields: "))


def get_field_name() -> str:
    return input("Enter field name: ")


def get_field_value_type() -> str:
    print("Select data type:")
    print("1. Integer;")
    print("2. Float;")
    print("3. String.")
    while True:
        choice = int(input("Enter number 1-3: "))
        if choice == 1:
            return "integer"
        if choice == 2:
            return "float"
        if choice == 3:
            return "string"


def get_min_value() -> str:
    return input("Enter minimal value (integer or float): ")


def get_max_value() -> str:
    return input("Enter maximal value (integer or float): ")


def create_free_document_schema() -> Optional[Dict[str, Any]]:
    document_schema = {}
    while True:
        print("1. Add new field")
        print("2. Next step")
        choice = choice_cli()
        if choice == 1:
            field_name = get_field_name()
            field_type = get_field_value_type()
            if field_type == "integer":
                min_value: Union[int, float] = int(get_min_value())
                max_value: Union[int, float] = int(get_max_value())
                document_schema.update({field_name: [field_type, min_value, max_value]})
                print(document_schema)
            if field_type == "float":
                min_value = float(get_min_value())
                max_value = float(get_max_value())
                document_schema.update({field_name: [field_type, min_value, max_value]})
                print(document_schema)
            if field_type == "string":
                document_schema.update({field_name: [field_type]})
                print(document_schema)
        if choice == 2:
            break
    print(document_schema)
    return document_schema


def create_fixed_document_schema() -> Optional[Dict[str, Any]]:
    document_schema = {}
    number_of_fields = get_number_of_fields()
    for _ in range(number_of_fields):
        field_name = get_field_name()
        field_type = get_field_value_type()
        if field_type == "integer":
            min_value: Union[int, float] = int(get_min_value())
            max_value: Union[int, float] = int(get_max_value())
            document_schema.update({field_name: [field_type, min_value, max_value]})
            print(document_schema)
        if field_type == "float":
            min_value = float(get_min_value())
            max_value = float(get_max_value())
            document_schema.update({field_name: [field_type, min_value, max_value]})
            print(document_schema)
        if field_type == "string":
            document_schema.update({field_name: [field_type]})
            print(document_schema)
    print(document_schema)
    return document_schema


def create_document(document_schema) -> Dict[str, Any]:
    document = {}
    for key, value in document_schema.items():
        if value[0] == "integer":
            field_value: Union[int, float, str] = get_integer_field_value(
                value[1], value[2]
            )
            document.update({key: field_value})
        if value[0] == "float":
            field_value = get_float_field_value(value[1], value[2])
            document.update({key: field_value})
        if value[0] == "string":
            field_value = get_string_field_value()
            document.update({key: field_value})
    return document


def get_number__of_documents_to_create() -> int:
    return int(input("Enter number of documents to create: "))


def get_integer_field_value(min_value, max_value) -> int:
    return random.randint(min_value, max_value)


def get_float_field_value(min_value, max_value) -> float:
    return random.uniform(min_value, max_value)


def get_string_field_value() -> str:
    r = RandomWords()
    return r.get_random_word()


def display_menu():
    print("\n\/\/\/\/\/\/\/\/\/\/\/")
    print("DATABASE CREATION MENU")
    print("\/\/\/\/\/\/\/\/\/\/\/\n")
    print("1. Create a new database")
    print("2. Exit")


class DbGenerator:
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host, port)  # type: ignore
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_document(self, document: Dict[str, Any]) -> str:
        result = self.collection.insert_one(document)
        return str(result.inserted_id)


if __name__ == "__main__":
    # display_menu()
    # field_value: Optional[Union[str, int, float]] = None
    # while True:
    #     choice = choice_cli()

    #     if choice == 1:
    #         db_name = get_database_name()
    #         db_collection = get_collection_name()
    #         new_db = DbGenerator(
    #             host="localhost",
    #             port=27017,
    #             db_name=db_name,
    #             collection_name=db_collection,
    #         )
    #         number_of_fields = get_number_of_fields()
    #         number_of_documents = get_number__of_documents_to_create()
    #         for _ in range(number_of_documents):
    #             document: Dict[str, Any] = {}
    #             for _ in range(number_of_fields):
    #                 field_name = get_field_name()
    #                 field_type = get_field_value_type()
    #                 if field_type == 1:
    #                     field_value = get_integer_field_value()
    #                 if field_type == 2:
    #                     field_value = get_float_field_value()
    #                 if field_type == 3:
    #                     field_value = get_string_field_value()
    #                 document.update({field_name: field_value})
    #             print(document)
    #             new_db.add_document(document)

    #     if choice == 2:
    #         exit

    create_document_schema()
