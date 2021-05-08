#!/usr/bin/env python3

import pandas as pd
import pathlib
import json
import argparse


def main():
    """Convert DFAM format to repeatmasker/deepgrp format."""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dfamfile", type=str, help="DFAM input file",
        default="hg38_dfam.nrph.hits.gz")
    parser.add_argument("--knownrepeats", type=str, help="Known repeats file",
        default="../repeats.json")
    args = parser.parse_args()

    data = pd.read_csv(
        args.dfamfile,
        sep="\t",
        usecols=["#seq_name", "family_acc", "ali-st", "ali-en"],
        dtype={
            "#seq_name": "category",
            "family_acc": str,
            "ali-st": int,
            "ali-en": int,
        },
    )
    with pathlib.Path(args.knownrepeats).open("r") as file:
        known_repeats = json.load(file)["DFAM"]

    known_repeats = pd.Series(known_repeats).reset_index()
    known_repeats.columns = ["family_acc", "repeatclass"]
    data = pd.merge(data, known_repeats, on="family_acc", how="inner")
    data.repeatclass = (data.repeatclass.astype("category")
        .cat.reorder_categories(
            ["Satellite", "ALR/Alpha", "SINE/Alu", "LINE/L1"],
            ordered=True)
    )
    data["repeatlabel"] = data.repeatclass.cat.codes + 1
    data[
        ["#seq_name", "ali-st", "ali-en", "repeatlabel", "family_acc", "repeatclass"]
    ].to_csv("hg38.dfam.bed", sep="\t", header=None, index=None)


if __name__ == "__main__":
    main()
