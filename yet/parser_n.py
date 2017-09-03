# -*-coding:utf-8 -*-
import argparse


def parse():
    parser = argparse.ArgumentParser(description="number")
    parser.add_argument('--number_of_bars', '-n', default=20,
                        type=int, help="number of bar")
    args = parser.parse_args()
    n = args.number_of_bars
    
    return n

