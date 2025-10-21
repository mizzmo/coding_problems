# Sorting Algorithms

## Contents

1. [Bucket Sort](#bucket-sort)

## Bucket Sort

Sorting by dividing elements into various buckets (groups). Once the elements are divided into buckets, the buckets can be sorted internally by another sorting algorithm (*usually Insertion Sort*), and afterwards the elements are gathered together in an ordered fashion.

### Steps

1. Create n empty buckets.
2. Insert every array[i] into bucket n*array[i].
3. Sort the elements within each bucket using insertion sort.
4. Concatenate all sorted buckets.

[See in code](/sorting_algorithms/bucket_sort.py)
