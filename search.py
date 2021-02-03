import glob
import os

path = "../deeprotvo_weight10_results"
# path = "../attnrotvo_weight10_results"
seq = "00"
stats = glob.glob(f"{path}/**/{seq}_*_eval/*_stats.txt", recursive=True)
stats = sorted(stats)
errors = []

print(f"Found {len(stats)} stats")
for s in stats:
    with open(s, 'r') as f:
        lines = f.read()
        # error = float(lines.split("\n")[1].split(":")[1].strip())
        error = float(lines.split("\n")[2].split(":")[1].strip())
        errors.append((error, s.split("/")[-2].split("_")[1]))
errors = sorted(errors, reverse=False, key=lambda x: x[0])
print(errors[:10])