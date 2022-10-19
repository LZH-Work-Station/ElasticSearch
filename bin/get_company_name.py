import os
import random

current_directory = os.path.dirname(os.path.abspath(__file__))
from loguru import logger


def search_key(file):
    res = []
    lines = file.readline()
    pos = 0
    count = 0
    for line in lines.split("("):
        if pos == 0:
            pos += 1
            continue
        if random.random() <= 0.035:
            res.append(line.split(")")[0])
            logger.info(line.split(")")[0] + " with count = " + str(count))
            count += 1
    file.close()
    return res


def write_key_in_file(file, res):
    for company in res:
        file.write(company + '\n')
    file.close()


if __name__ == '__main__':
    file_input = open(current_directory + '/../conf/initial.txt', mode='r', encoding='utf-8')
    file_output = open(current_directory + '/../conf/company_symbole.txt', mode='w', encoding='utf-8')
    write_key_in_file(file_output, search_key(file_input))
`
