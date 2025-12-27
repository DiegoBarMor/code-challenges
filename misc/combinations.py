# ------------------------------------------------------------------------------
def iter_permutations(*args):
    """Generate all permutations of the given arguments."""
    if not args:
        yield (); return

    for i,x in enumerate(args):
        for c in iter_permutations(*args[:i], *args[i+1:]):
            yield c + (x,)


# ------------------------------------------------------------------------------
def iterate_integer_partitions(k: int, total: int):
    """Generate all k-tuples of non-negative integers that sum to total."""
    if k == 1:
        yield (total,); return

    for n in range(total+1):
        for c in iterate_integer_partitions(k-1, total-n):
            yield c + (n,)


# ------------------------------------------------------------------------------
def iter_selection_masks(n: int):
    """Yield all length-n tuples of booleans representing selection masks."""
    if not n:
        yield (); return

    for mask in iter_selection_masks(n-1):
        yield (True,)  + mask
        yield (False,) + mask


# ------------------------------------------------------------------------------
