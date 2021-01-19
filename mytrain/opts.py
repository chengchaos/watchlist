# -*- coding:utf-8 -*-
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("indent", type=int, help="indent for report")
    parser.add_argument("input_file", help="read data from this file")
    parser.add_argument("-f", "--file", dest="filename",
                        help="write report to FILE", metavar="FILE")

    args = parser.parse_args()

    print("arguments: ", args)


main()
