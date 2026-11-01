cache_lines = 8
cache = [None] * cache_lines

memory_blocks = [3, 11, 3, 19, 11, 27, 3]

hits = 0
misses = 0

print("Memory Block\tCache Line\tHIT/MISS\tCache Contents")

for block in memory_blocks:
    line = block % cache_lines

    if cache[line] == block:
        status = "HIT"
        hits += 1
    else:
        status = "MISS"
        misses += 1
        cache[line] = block

    print(f"{block}\t\t{line}\t\t{status}\t\t{cache}")

total_accesses = len(memory_blocks)
hit_ratio = hits / total_accesses

print("\nFinal Cache Contents:")
for i in range(cache_lines):
    print("Cache Line", i, ":", cache[i])

print("\nTotal Accesses:", total_accesses)
print("Total Hits:", hits)
print("Total Misses:", misses)
print("Hit Ratio:", hit_ratio)
print("Hit Ratio (%):", hit_ratio * 100)
