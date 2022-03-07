import os
import sys
import json

results = {}

for i in filter(os.path.isdir, os.listdir(os.getcwd())):
    if not i.startswith("."):
        results[i] = []
        os.chdir(i)
        for files in os.listdir(os.getcwd()):
            results[i].append(files)
        os.chdir("..")

fullJson = ',\n'.join(json.dumps(results).split(",")) + "\n"

print(fullJson)

with open('images.json', 'w') as f:
    f.write(fullJson)
