import logging

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

for element_number in range(1, 5):
    elements_list = ['first', 'second', 'third', 'fourth']
    input_element = input(f'Input your {elements_list[element_number-1]} element: ')
    logging.info(f'Your {elements_list[element_number-1]} entered element is: {input_element}')

