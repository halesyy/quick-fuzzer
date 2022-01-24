
import json
from fuzzywuzzy import process, fuzz # Local import.

# 1. Fuzzy matching shorthand.
# 2. TSV interpreter shorthand. Replace \t with , for a csv parser.
fuzzy_match = lambda needle, haystack, n=1: process.extract(needle, haystack, limit=n, scorer=fuzz.token_set_ratio)
tsv = lambda fn: [r.split("\t") for r in str(open(fn, "r").read()).strip().split("\n")]

# Dataset interpreter, we want to
# end this process with two lists.
dataset_primary = [row[0] for row in tsv("datasets/a.example")] # Our needles.
dataset_secondary = [row[0] for row in tsv("datasets/b.example")] # Our haystack.

for needle in dataset_primary:
    print("------")
    print(f"> search for: {needle}")
    close = fuzzy_match(needle, haystack=dataset_secondary, n=3)
    print(f"> responses: {close}")
    print("-------")
    input()
