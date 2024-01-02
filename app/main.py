import os
import cx_Oracle
from dotenv import load_dotenv
from typing import Union
from fastapi import FastAPI

app = FastAPI()

load_dotenv()

DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_SERVER = os.environ.get("DB_SERVER")
DB_LIB_PATH = os.environ.get("DB_LIB_PATH")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test_connection/")
def read_item(item_id: int, q: Union[str, None] = None):
    try:
        cx_Oracle.init_oracle_client(lib_dir=DB_LIB_PATH)
    except Exception as err:
        print(err)

    connection = None

    try:
        connection = cx_Oracle.connect(
            DB_USERNAME,
            DB_PASSWORD,
            DB_SERVER,
            encoding='UTF-8'
        )
        print(connection.version)

    except cx_Oracle.Error as error:
        print(error)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    print("This is the app.py file")