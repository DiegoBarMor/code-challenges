# TODO
cleanup this

# Instructions
1) populate `input.txt` with the desired input
2) run `find_longest_val.py` to find the longest string that the yields from `input.txt` will yield. Let's call the output `MAXLEN`
3) run `gen_cache divisors.py` and provide `MAXLEN` as its argument. `cache_divisors.json` will be generated
4) run `main.py`

# Why?
I thought the callenge could involve ranges with very long numbers (let's say 200 digits) and prepared beforehand to have an easy way of caching the "relevant splits" for a given integer. Of course, having huge integers would have complicated things in `main.py`, assuming the numbers were longer than the limit of python's 64-bit integers.

At the end, the challenge focused more in numbers with max ~10 digits, but big ranges between them, so caching the divisors beforehand is a bit unnecessary. Also, `gen_cache divisors.py` uses a relatively brutal implementation, so calling it with arguments larger than 10000 could be slow.

In any case, perhaps `gen_cache divisors.py` could be useful for other challenges / applications.
