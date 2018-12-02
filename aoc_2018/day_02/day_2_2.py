# --- Day 2: Inventory Management System ---
# Part 2 -

import sys

with open('./input.txt') as fp:
    pkg_ids = [x for x in fp.read().split('\n') if x]

for pkg_id in pkg_ids:
    candidates = pkg_ids.copy()
    errors = set()
    for i in range(0, len(pkg_id)):
        new_candidates = []
        for candidate in candidates:
            if candidate == pkg_id:
                # Skip the id itself
                continue

            if pkg_id[i] == candidate[i]:
                new_candidates.append(candidate)
            elif candidate not in errors:
                new_candidates.append(candidate)
                errors.add(candidate)

        candidates = new_candidates

    if len(candidates) > 0:
        res = []
        candidate = candidates[0]
        for i in range(len(pkg_id)):
            if pkg_id[i] == candidate[i]:
                res.append(pkg_id[i])

        print(''.join(res))
        break
