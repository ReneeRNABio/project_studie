import argparse as arg
parser = arg.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",type= int)
args = parser.parse_args()
print(args.square**2)

