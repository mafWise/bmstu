import statistics
import json
import sys

opts = ["O1", "O2", "O3", "O0", "Os"]
counters = [1, 2]
max_size = int(sys.argv[2])
min_size = int(sys.argv[1])
step = int(sys.argv[3])
all = int(((max_size - min_size) / step + 1) * len(opts) * len(counters))
co = 1

for counter in counters:
    for opt in opts:
        for NMAX in range(min_size, max_size + 1, step):
            filename = f"0{counter}_{opt}_{NMAX}.txt"

            try:
                with open(f"./data/{filename}", "r") as src:
                    data = list(map(int, src.read().split()))
            except:
                print(f"Нет подходящего файла: {filename}")
                continue

            curr_params = dict()

            curr_params["minimum"] = min(data)
            curr_params["maximum"] = max(data)
            curr_params["mean"] = statistics.fmean(data)
            curr_params["median"] = statistics.median(data)
            #curr_params["top_quart"] = statistics.quantiles(data)[2]
            #curr_params["bottom_quart"] = statistics.quantiles(data)[0]
            curr_params["opt"] = opt
            curr_params["counter"] = counter
            curr_params["NMAX"] = NMAX

            filename = filename[:-3] + "json"

            try:
                with open(f"./preproc/{filename}", "w") as dst:
                    json.dump(curr_params, dst)
            except:
                print("Нет папки preproc")

            print(f"Подготовка файла [{co} / {all}]", end='\r')
            co += 1
print("")
