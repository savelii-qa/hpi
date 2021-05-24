import argparse
import logging
import time
import os

if __name__ == '__main__':
    start_time = time.time()

    FORMAT = '[%(asctime)s] : %(message)s'
    DATEFMT = '%m/%d/%Y %I:%M:%S'

    parser = argparse.ArgumentParser(description='Create html file with chart.')
    parser.add_argument('symbol', metavar='S', type=str, nargs='?', help='symbol to get info.')

    args = parser.parse_args()
    symbol = vars(args)['symbol']

    logging.basicConfig(filename="datacamp.log", level=logging.INFO, format=FORMAT, datefmt=DATEFMT)
    logging.StreamHandler().terminator = '\n'
    logging.info(f'Starting script for {symbol}')

    logging.info(f'Running lab13')
    os.system(f'python lab13.py {symbol}')
    logging.info(f'Running lab14')
    os.system(f'python lab14.py {symbol}')
    logging.info(f'Running lab15')
    os.system(f'python lab15.py {symbol}')

    # logging.info(f'Remove csv files.')
    # os.remove(f'{symbol}13.csv')
    # os.remove(f'{symbol}14.csv')
    end_time = time.time() - start_time
    logging.info(f'Script done with time - {round(end_time, 2)}\n')