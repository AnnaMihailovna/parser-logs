import re
from collections import Counter

def reader(filename):
    regex = r'\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3}'
    with open(filename) as f:
        log = f.read()
        ip_list = re.findall(regex, log)
    return ip_list


def count(ip_list):
    pass




if __name__ == '__main__':
    reader('2023_10_31.log')