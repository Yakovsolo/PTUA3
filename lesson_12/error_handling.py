from typing import Optional, Union





# try:
#     my_divided_number = divider('0')
#     print(my_divided_number)
#     print(my_divided_number / 0)
 

# except  TypeError:
#     print("We are f*cked up!")
# except ZeroDivisionError:
#     print("Neer divide by 0")


# try:
#     my_magic_number = 2
#     my_divided_number = divider(20)
#     print(my_divided_number)
#     print(my_divided_number / my_magic_number)
# except Exception as e:
#     print(f'Error: {e}')
# else:
#     print('Success')
# finally:
#     print('\n I dont care: I am printed anyways')

# def physics_is_fun(temp_c: float, pressure_mbar: float, time_utc: float, weight_kg: float) -> None:
#     pass

# physics_is_fun(temp_c= 55.87, pressure_mbar= 26.58, time_utc= 1258955, weight_kg= 458.3)

# def divider(number: Union[float, int]) -> Optional[Union[float, int]]:
#     try:
#         return number / 2 if isinstance(number, float) else number // 2
#     except TypeError:
#         print('Wrong type received')
#     except Exception as e:
#         print(f'Error: {e}')