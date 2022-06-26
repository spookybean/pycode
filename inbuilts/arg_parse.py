import argparse


parser = argparse.ArgumentParser(description='add an url')
parser.add_argument('-u', '--url', metavar='', help='download url', required=True)

args = parser.parse_args()