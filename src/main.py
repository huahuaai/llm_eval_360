import argparse
from evaluator import Evaluator
from transformers import set_seed
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("")
    parser.add_argument("--device_map",)
    parser.add_argument("--seed", dtype=int, default="")
    args = parser.parse_args()

def main():
    args = get_args()
    set_seed(args.seed)


if __name__ == '__main__':
    main()