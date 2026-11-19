import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    stations = dict()

    with open(args.path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            name, temperature = line.split(";")
            temperature = float(temperature)
            if name not in stations:
                stations[name] = [temperature, temperature, temperature, 1]
            else:
                stations[name][0] = min(stations[name][0], temperature)
                stations[name][1] = stations[name][1] + temperature
                stations[name][2] = max(stations[name][2], temperature)
                stations[name][3] += 1

if __name__ == "__main__":
    main()
