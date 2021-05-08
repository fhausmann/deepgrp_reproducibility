#!/usr/bin/env python3
import pathlib
import json
import argparse
import pandas as pd
from typing import List, Match
import re

_ID_REGEX = re.compile(r"ID\s+(.+)\s+.*;\s(\d+)\sBP.")
_SUB_REGEX = re.compile(r"[\d\s]+")


class Record:
    def __init__(self, content: List[str]):
        match: Match[str] = _ID_REGEX.search(content[0])  # type: ignore
        self.id = match.group(1).split(" ", 1)[0]
        self._length = int(match.group(2))
        idx = {
            line.split(" ", 1)[0]: i
            for i, line in enumerate(content[1:], 1)
        }
        sequence = "".join(content[idx["SQ"] + 1:idx["//"]])
        sequence = sequence.lower()
        sequence = _SUB_REGEX.sub("", sequence)
        self._sequence = sequence
        assert len(self._sequence) == self._length, self.id

    def __repr__(self):
        return f"<Record named {self.id} of length {self._length}>"

    def to_fasta(self):
        if (self._length // 80) * 80 == self._length:
            endpoint = self._length
        else:
            endpoint = self._length + 80
        sequence = [self._sequence[i:i + 80] for i in range(0, endpoint, 80)]
        assert len("".join(sequence)) == self._length
        sequence = "\n".join(sequence)
        return f">{self.id}\n{sequence}"


def read_embl(filename: str):
    content: List[str] = []
    records: List[Record] = []
    with pathlib.Path(filename).open('r') as file:
        for line in file:
            line = line.rstrip()
            if line.startswith("ID") and content:
                records.append(Record(content))
                content = []
            if line.startswith("XX"):
                continue
            content.append(line)
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("embl_filename", type=str)
    parser.add_argument("output_fasta", type=str)
    parser.add_argument("--filter", type=str)
    args = parser.parse_args()
    records = read_embl(args.embl_filename)
    if args.filter:
        with pathlib.Path(args.filter).open("r") as file:
            id_filter = set(json.load(file)["DFAM"].keys())
        records = [record for record in records if record.id in id_filter]
    with pathlib.Path(args.output_fasta).open("w") as file:
        for record in records:
            file.write(record.to_fasta())


if __name__ == "__main__":
    main()
