import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(INPUT_FILENAME, OUTPUT_FILENAME) -> None:
    b=[]
    with open(INPUT_FILENAME) as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            b.append(row)

    #json_data = json.dumps(reader, indent=4, ensure_ascii=ensure_ascii)
    with open(OUTPUT_FILENAME, "w") as jsonf:
        st=json.dumps(b, indent=4)
        jsonf.write(st)

#print(task("input.csv", "output.json"))
if __name__ == '__main__':
    # Нужно для проверки
    task("input.csv", "output.json")

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
