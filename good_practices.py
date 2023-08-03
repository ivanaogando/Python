"""
good_practices.py

Project: None

Maintainer Ivana Ogando González (you@you.you)
Created @ Thursday, 20th July 2023 8:55:58 am

Copyright (c) 2023 Your Company
All Rights Reserved
"""

# ----- VARIABLES -----

import datetime
import time

from typing import Union, Dict
from typing import Generator, Iterator

current_date_now: str = datetime.datetime.now().strftime("%d-%m-%y")
print(current_date_now)

current_date: str = datetime.date.today().strftime("%d-%m-%y")
print(current_date)


def get_user_info():
    pass


def get_user_data():
    pass


def get_user_record():
    pass


# from typing import Union, Dict


class Record:
    pass


class User:
    info: str

    @property
    def data(self) -> Dict[str, str]:
        return {}

    def get_record(self) -> Union[Record, None]:
        return Record()


# import time

# Declare them in the global namespace for the module.
SECONDS_IN_A_DAY = 60 * 60 * 24
time.sleep(SECONDS_IN_A_DAY)


locations = ("Austin", "New York", "San Francisco")

for location in locations:
    # do_stuff()
    # do_some_other_stuff()
    # ...
    print(location)


# ----- FUNCTIONS -----

# from typing import Generator, Iterator


class Client:
    active: bool


def email(client: Client):
    pass


def active_clients(clients: Iterator[Client]) -> Generator[Client, None, None]:
    """Only active clients"""
    return (client for client in clients if client.active)


def email_client(clients: Iterator[Client]) -> None:
    """Send an email to a given list of clients."""
    for client in active_clients(clients):
        email(client)
