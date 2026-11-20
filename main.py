import argparse
from pathlib import Path
import sys
import math

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    stations = dict()

    try:
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
    except FileNotFoundError:
        print("Файл не найден", file=sys.stderr)
        return

    except OSError:
        print("Не удалось открыть или прочитать файл", file=sys.stderr)
        return

    for name in stations:
        average_temperature = stations[name][1] / stations[name][3]
        half_up_temperature = math.floor(average_temperature * 10 + 0.5) / 10
        stations[name][1] = half_up_temperature
        stations[name].pop(3)

    sorted_stations = sorted(stations)

    for name in sorted_stations:
        min_temperature = stations[name][0]
        mean_temperature = stations[name][1]
        max_temperature = stations[name][2]
        print(f"{name};{min_temperature:.1f};"
              f"{mean_temperature:.1f};{max_temperature:.1f}")

if __name__ == "__main__":
    main()
