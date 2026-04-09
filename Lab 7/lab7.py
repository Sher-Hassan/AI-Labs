"""
Lab 07 – Smart Sorting Framework

Implements six sorting algorithms and automatically selects the best one
based on array size, sortedness, duplicates, and value range.
"""

import heapq
import math
import time
import random


# Sorting Algorithms

def bubble_sort(arr: list) -> list:
    """O(n^2) - good for small or nearly sorted data"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr: list) -> list:
    """O(n^2) - fewer swaps"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: list) -> list:
    """Good for small or nearly sorted arrays"""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def heap_sort(arr: list) -> list:
    """O(n log n)"""
    h = arr.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def merge_sort(arr: list) -> list:
    """O(n log n)"""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: list) -> list:
    """Quick sort with median pivot"""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    candidates = [(arr[0], 0), (arr[mid], mid), (arr[-1], len(arr) - 1)]
    candidates.sort(key=lambda x: x[0])
    pivot = candidates[1][0]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Data analysis

def analyse(arr: list) -> dict:
    """Analyze array properties"""
    n = len(arr)
    if n == 0:
        return {"n": 0}

    inversions = sum(1 for i in range(n - 1) if arr[i] > arr[i + 1])
    sorted_ratio = 1.0 - inversions / max(n - 1, 1)

    unique_ratio = len(set(arr)) / n
    value_range = max(arr) - min(arr) if n > 1 else 0

    return {
        "n": n,
        "sorted_ratio": round(sorted_ratio, 4),
        "unique_ratio": round(unique_ratio, 4),
        "value_range": value_range,
    }


# Algorithm selection

ALGORITHM_REGISTRY = {
    "bubble_sort":    bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "heap_sort":      heap_sort,
    "merge_sort":     merge_sort,
    "quick_sort":     quick_sort,
}


def select_algorithm(stats: dict) -> str:
    """Choose best algorithm"""
    n = stats.get("n", 0)
    sorted_ratio = stats.get("sorted_ratio", 0)
    unique_ratio = stats.get("unique_ratio", 1)

    if n <= 1:
        return "insertion_sort"
    if n <= 10:
        return "insertion_sort"
    if sorted_ratio >= 0.90:
        return "insertion_sort"
    if n <= 50:
        return "selection_sort"
    if unique_ratio <= 0.10:
        return "heap_sort"
    if n <= 500:
        return "quick_sort"
    return "merge_sort"


# Smart sort

def smart_sort(arr: list, verbose: bool = True) -> list:
    """Smart sorting"""
    if not arr:
        return []

    stats = analyse(arr)
    algorithm = select_algorithm(stats)
    sort_fn = ALGORITHM_REGISTRY[algorithm]

    start = time.perf_counter()
    result = sort_fn(arr)
    elapsed = (time.perf_counter() - start) * 1_000

    if verbose:
        print("Smart Sorting Report")
        print("Input size:", stats['n'])
        print("Sorted ratio:", stats['sorted_ratio'])
        print("Unique ratio:", stats['unique_ratio'])
        print("Value range:", stats['value_range'])
        print("Selected algorithm:", algorithm)
        print("Time (ms):", round(elapsed, 4))

    return result


# Demo

def _demo():
    test_cases = [
        {
            "label": "Tiny array",
            "data": [64, 34, 25, 12, 22, 11, 90],
        },
        {
            "label": "Nearly sorted",
            "data": [1, 2, 3, 4, 5, 6, 8, 7, 9, 10, 11, 12, 13, 15, 14],
        },
        {
            "label": "Small random",
            "data": random.sample(range(100), 30),
        },
        {
            "label": "Many duplicates",
            "data": [random.choice(range(10)) for _ in range(200)],
        },
        {
            "label": "Medium random",
            "data": random.sample(range(10_000), 300),
        },
        {
            "label": "Large random",
            "data": random.sample(range(100_000), 1_000),
        },
    ]

    for case in test_cases:
        print("\nTest:", case["label"])
        arr = case["data"]
        result = smart_sort(arr, verbose=True)

        assert result == sorted(arr), "Sort result incorrect"
        preview = result[:8]
        suffix = " ..." if len(result) > 8 else ""
        print("Preview:", preview, suffix)
        print("Verified")

    print("\nAll test cases passed")


if __name__ == "__main__":
    _demo()