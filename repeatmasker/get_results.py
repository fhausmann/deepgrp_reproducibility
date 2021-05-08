#!/usr/bin/env python3

import argparse
import pathlib
import numpy as np
import re
import pandas as pd
from datetime import datetime

def parse_time(time:str) -> float:

    if "." not in time:
        time = time + ".0"
    if not time.count(":") == 2:
        time = "0:" + time
    pt = datetime.strptime(time,"%H:%M:%S.%f")
    time_in_seconds = pt.second + pt.hour*3600 + pt.minute * 60
    return time_in_seconds + (pt.microsecond * 1e-6)


def parse_linux(filename):
    results = dict()
    header_regex = re.compile(r"hg\d{2}/chr.*\.fa")
    exit_status = re.compile(r"Command exited with non-zero status (\d*)")
    times = re.compile(
        r"(\d+\.\d+)user\s(\d+\.\d+)system\s((\d+:)?\d+:\d+(\.\d+)?)elapsed")
    header = None
    with pathlib.Path(filename).open("r") as file:
        for line in file:
            line = line.strip()
            match = header_regex.search(line)
            if match:
                header = match.group(0)
                continue
            match = exit_status.search(line)
            if match and header:
                if int(match.group(1)) == 1:
                    continue
                results[header] = dict(real=np.nan, user=np.nan, sys=np.nan)
                header = None
                continue
            match = times.search(line)
            if match and header:
                real_time = parse_time(match.group(3))
                results[header] = dict(real=real_time,
                                       user=float(match.group(1)),
                                       sys=float(match.group(2)))
                header = None
                continue
    return pd.DataFrame(results).T


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--linux", required=False, action="store_true")
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    results = parse_linux(args.filename)
    results[["real", "sys", "user"]] = results[["real", "sys",
                                                "user"]].astype(float)
    results.to_csv("running_time.csv")

if __name__ == "__main__":
    main()
