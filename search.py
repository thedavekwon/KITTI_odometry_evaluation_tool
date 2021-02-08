import glob
import os

# vo = "deeprotvo"
# vo = "deeprotvo_weight100"
vo = "attnrotvo_weight100"
weight_path = f"../{vo}_w"
result_path = f"../{vo}_results"
keyword=""

seq = "00"
stats = glob.glob(f"{result_path}/**/{seq}_*_eval/*_stats.txt", recursive=True)
stats = sorted(stats)
errors = []

weights = list(map(lambda x: x.split("/")[-1].split(".")[0], glob.glob(f"{weight_path}/*")))
for s in stats:
    with open(s, 'r') as f:
        lines = f.read()
        error = float(lines.split("\n")[0].split(":")[1].strip())
        seq = s.split("/")[-2].split("_")[1]
        if not seq in weights:
            continue
        errors.append((error, seq))
errors = sorted(errors, reverse=False, key=lambda x: x[0])
print(f"Found {len(errors)} results")
if keyword:
    errors = filter(lambda x: keyword in x[1], errors) 
for e in errors:
    print(e)

