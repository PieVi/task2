#!usr/bin/env python3

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Accepts an integer')
    parser.add_argument('num', type=int)
    return parser.parse_args()

args = parse_arguments()

def fizz_buzz(num):
    for i in range(num):
        if (i+1)%3==0 and (i+1)%5==0:
            print('fizzbuzz')
        elif (i+1)%3==0:
            print('fizz')
        elif (i+1)%5==0:
            print('buzz')
        else:
            print(i+1)

fizz_buzz(args.num)

