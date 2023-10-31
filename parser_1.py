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
    return Counter(ip_list)

def write_csv(count):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Frequence']
        writer.writerow(header)
        for item in count:
            writer.writerow((item, count[item]))


if __name__ == '__main__':
    write_csv(count(reader('2023_10_31.log')))
