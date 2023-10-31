import re
from collections import Counter
import csv

def reader(filename):
    regex = r'\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3}'
    with open(filename) as f:
        log = f.read()
        ip_list = re.findall(regex, log)
    return ip_list


def count(ip_list):
    count = Counter(ip_list)
    return count

def write_csv(count):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequence']
        writer.writerow(header)
        for item in count:
            pass

if __name__ == '__main__':
    reader('2023_10_31.log')