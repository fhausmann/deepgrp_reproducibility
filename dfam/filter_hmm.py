#!/usr/bin/env python3
import pathlib
import pandas as pd
import argparse
import logging


def parse_hmm(file):
    content = []
    ids = None
    for line in file:
        if line.startswith("#"):
            continue
        if line.startswith("//"):
            content.append(line)
            yield ids, content
            ids = None
            content = []
            continue
        content.append(line)
        if line.startswith("ACC"):
            ids = line.replace("ACC", "").strip().split(".")[0]
    if ids:
        yield ids, content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hmm_file", type=str)
    parser.add_argument("known_repeats", type=str)
    parser.add_argument("outputfile", type=str)
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()

    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, args.verbose)]
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")


    with pathlib.Path(args.known_repeats).open("r") as file:
        known_repeats = list(json.load(file)["DFAM"].keys())

    known_repeats = {x.split(".")[0] for x in known_repeats}
    logger = logging.getLogger()
    logger.info("Found %d known repeats", len(known_repeats))
    n_repeats = 0
    n_total = 0
    with pathlib.Path(args.hmm_file).open("r") as file:
        with pathlib.Path(args.outputfile).open("w") as output:
            for n_total, repeat in enumerate(parse_hmm(file), 1):
                logger.debug("Found repeat %s", repeat[0])
                if repeat[0] in known_repeats:
                    for line in repeat[1]:
                        output.write(line)
                    logger.debug("Wrote %s to file", repeat[0])
                    n_repeats += 1
    logger.info(
        "Wrote %d of %d repeats to new file %s", n_repeats, n_total, args.outputfile
    )


if __name__ == "__main__":
    main()
