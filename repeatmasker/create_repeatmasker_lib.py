#!/usr/bin/env python3
import pathlib
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", type=str)
    parser.add_argument("outfile", type=str)
    parser.add_argument("--repeatclass", type=str)
    args = parser.parse_args()
    repeatclasses = {}
    if args.repeatclass:
        with pathlib.Path(args.repeatclass).open("r") as file:
            repeatclasses = json.load(file)["RepeatMasker"]
    with pathlib.Path(args.infile).open("r") as infile:
        with pathlib.Path(args.outfile).open("w") as outfile:
            for line in infile:
                if not line.startswith(">"):
                    outfile.write(line)
                    continue
                header = line[1:].strip()
                typ = repeatclasses.get(header, "unknown")
                outfile.write(f">{header}#{typ}\n")


if __name__ == "__main__":
    main()
