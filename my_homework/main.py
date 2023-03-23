import logging
from os import system

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Players:
    available_number_of_players = [1, 2, 3, 4, 5, 6]
    players_list: list = []
    list_of_numbers: list = [
        "first player",
        "second player",
        "third player",
        "fourth player",
        "fifth player",
        "sixth player",
    ]

    def get_number_of_players(self) -> int:
        try:
            number_of_players = int(
                input("Please enter the number of players (from one to six): ")
            )
            logging.info(f"{number_of_players} players entered to play")
            if number_of_players in self.available_number_of_players:
                return number_of_players

        except NameError as e:
            print(f"You must enter an integer from one to six! {e}")
            logging.error(
                f"You must enter an integer from one to six! {number_of_players} is not an integer!"
            )
            return self.get_number_of_players()
        else:
            print(f"You must enter an integer from one to six!")
            logging.error(
                f"You must enter an integer from one to six! {number_of_players} is out of range from one to six!"
            )
            return self.get_number_of_players()

    # def input_player_names(self) -> list:
    #     for number in range(self.number_of_players):
    #         player_name = input(
    #             f"PLease input {self.list_of_numbers[number]}'s name: "
    #         ).upper()
    #         logging.info(f"The {self.list_of_numbers[number]}'s name is: {player_name}")
    #         if len(player_name) > 3:
    #             player_name = player_name[0:3]
    #         self.players_list.append(player_name)
    #     return self.players_list


game = Players()
print(game.get_number_of_players())
