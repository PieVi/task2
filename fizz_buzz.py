#!usr/bin/env python3

import argparse

# def parse_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('num', type=int, help='the number the fizzbuzz range will be')
#     return parser.parse_args()

# args = parse_arguments()

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

def fizz_buzz_generator():
    i=0  
    while True:
        i+=1
        if i%3==0 and i%5==0:
            yield 'fizzbuzz'
        elif i%3==0:
            yield 'fizz'
        elif i%5==0:
            yield 'buzz'
        else:
            yield i
        



