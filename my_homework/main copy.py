import datetime
from typing import List, Dict, Union, Optional


class Reservation:
    def __init__(
        self,
        name: str,
        surname: str,
        time: datetime,
        time_delta: int,
    ) -> None:
        self.name = name
        self.surname = surname
        self.time = time
        self.time_delta = time_delta
        self.end_of_reservation_time = time + datetime.timedelta(hours=time_delta)


class Table:
    def __init__(
        self,
        table_type: str,
    ) -> None:
        self.table_type = table_type
        self.reservations: List[Reservation] = []

    def create_reservation(
        self,
        name: str,
        surname: str,
        time: datetime,
        time_delta: int,
    ):
        reservation = Reservation(name, surname, time, time_delta)
        self.reservations.append(reservation)

    def check_availability(
        self,
        time: datetime,
        time_delta: datetime,
    ):
        for reservation in self.reservations:
            if reservation.time <= time and time < reservation.end_of_reservation_time:
                return False
            elif (
                reservation.time < time + datetime.timedelta(hours=time_delta)
                and time + datetime.timedelta(hours=time_delta)
                < reservation.end_of_reservation_time
            ):
                return False
        return True

    def get_reservations_info(self) -> List[Dict[str, Union[str, datetime.datetime]]]:
        reservations_info = []
        for reservation in self.reservations:
            info = {
                "name": reservation.name,
                "surname": reservation.surname,
                "time": reservation.time,
                "end of table reservation": reservation.end_of_reservation_time,
            }
            reservations_info.append(info)
        return reservations_info


class Restaurant:
    def __init__(self) -> None:
        self.tables: Dict[str, List[Table]] = {}

    def add_table(self, table_type: str, quantity: int):
        tables = [Table(table_type) for _ in range(quantity)]
        if table_type in self.tables:
            self.tables[table_type] += tables
        else:
            self.tables[table_type] = tables

    def create_reservation(
        self, name: str, surname: str, time: datetime, time_delta: int
    ) -> Optional[str]:
        available_table = None
        for tables in self.tables.values():
            for table in tables:
                if table.check_availability(time, time_delta):
                    available_table = table
                    break
            if available_table:
                break

        if available_table:
            available_table.create_reservation(name, surname, time, time_delta)
        else:
            return None

    def check_table_availability(
        self, table_type: str, time: datetime, time_delta: int
    ) -> bool:
        if table_type not in self.tables:
            return False
        for table in self.tables[table_type]:
            if table.check_availability(time, time_delta):
                return True
        return False

    # def get_tables_info(self):
    #     for table[table_type] in self.tables:


if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.add_table("single table", 3)
    restaurant.add_table("double table", 2)
    restaurant.add_table("family table", 2)

    name, surname = "Jakov", "Solovov"
    time = datetime.datetime(2023, 4, 1, 18)
    print(time)
    time_delta = 4
    table_type = "single table"
    available = restaurant.check_table_availability(table_type, time, time_delta)

    if available:
        table = Table(table_type)
        restaurant.create_reservation(name, surname, time, time_delta)
        print("Reservation created")

    else:
        print(f"{table_type} is not available at {time}")
