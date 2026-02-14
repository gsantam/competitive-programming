"""
Benchmark comparing Linear Search vs Binary Search for different array sizes.
Includes statistical significance testing with p99 confidence intervals.
"""
import random
import time
import statistics
from typing import List, Optional, Tuple


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """Linear search - O(n)"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """Binary search - O(log n)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def generate_sorted_array(n: int) -> List[int]:
    """Generate a sorted array of n random integers"""
    arr = [random.randint(0, n * 10) for _ in range(n)]
    arr.sort()
    return arr


def benchmark_search_with_stats(
    search_func, arr: List[int], targets: List[int], iterations: int
) -> Tuple[float, float, float, float, List[float]]:
    """
    Run search function multiple times and return statistics.
    Returns: (mean, std_dev, p1, p99, all_times)
    """
    all_times = []

    for _ in range(iterations):
        for target in targets:
            start = time.perf_counter()
            search_func(arr, target)
            end = time.perf_counter()
            # Convert to microseconds
            all_times.append((end - start) * 1_000_000)

    mean = statistics.mean(all_times)
    std_dev = statistics.stdev(all_times) if len(all_times) > 1 else 0

    sorted_times = sorted(all_times)
    p1_idx = int(len(sorted_times) * 0.01)
    p99_idx = int(len(sorted_times) * 0.99)
    p1 = sorted_times[p1_idx]
    p99 = sorted_times[p99_idx]

    return mean, std_dev, p1, p99, all_times


def welch_t_test(mean1: float, std1: float, n1: int,
                 mean2: float, std2: float, n2: int) -> Tuple[float, float]:
    """
    Perform Welch's t-test for two samples with unequal variances.
    Returns: (t_statistic, degrees_of_freedom)
    """
    import math

    # Avoid division by zero
    if std1 == 0 and std2 == 0:
        return float('inf') if mean1 != mean2 else 0, n1 + n2 - 2

    se1 = (std1 ** 2) / n1
    se2 = (std2 ** 2) / n2
    se_diff = math.sqrt(se1 + se2)

    if se_diff == 0:
        return float('inf') if mean1 != mean2 else 0, n1 + n2 - 2

    t_stat = (mean1 - mean2) / se_diff

    # Welch-Satterthwaite degrees of freedom
    if se1 + se2 == 0:
        df = n1 + n2 - 2
    else:
        df = ((se1 + se2) ** 2) / ((se1 ** 2) /
                                   (n1 - 1) + (se2 ** 2) / (n2 - 1))

    return t_stat, df


def t_critical_99(df: float) -> float:
    """
    Approximate critical t-value for 99% confidence (two-tailed, alpha=0.01).
    Uses approximation for large df.
    """
    # For 99% confidence, two-tailed, we need t_0.005
    # Approximation based on normal distribution for large df
    if df >= 120:
        return 2.576  # z-value for 99%

    # Lookup table for common df values (two-tailed, alpha=0.01)
    t_table = {
        1: 63.657, 2: 9.925, 3: 5.841, 4: 4.604, 5: 4.032,
        10: 3.169, 15: 2.947, 20: 2.845, 25: 2.787, 30: 2.750,
        40: 2.704, 50: 2.678, 60: 2.660, 80: 2.639, 100: 2.626
    }

    # Find closest df
    closest = min(t_table.keys(), key=lambda x: abs(x - df))
    return t_table[closest]


def run_benchmark():
    # Test smaller array sizes with high precision
    sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12,
             15, 18, 20, 25, 30, 35, 40, 45, 50]
    iterations = 5000  # Number of times to repeat each test
    num_targets = 50   # Number of random targets to search per iteration

    print("=" * 110)
    print("BENCHMARK: Linear Search vs Binary Search (Statistical Analysis)")
    print("=" * 110)
    print(f"Iterations per size: {iterations}")
    print(f"Random targets per iteration: {num_targets}")
    print(f"Total samples per N: {iterations * num_targets:,}")
    print(f"Confidence level: 99% (p < 0.01)")
    print("=" * 110)
    print()

    header = (
        f"{'N':>4} | {'Linear':>8} | {'Binary':>8} | "
        f"{'Lin p99':>8} | {'Bin p99':>8} | "
        f"{'Diff':>8} | {'t-stat':>8} | {'Sig?':>6} | {'Winner':>8}"
    )
    print(header)
    print("-" * 110)

    results = []

    for n in sizes:
        # Generate sorted array
        arr = generate_sorted_array(n)

        # Generate random targets (mix of existing and non-existing elements)
        targets = []
        for _ in range(num_targets):
            if random.random() < 0.7:  # 70% chance to pick existing element
                targets.append(random.choice(arr))
            else:  # 30% chance to pick random (possibly non-existing)
                targets.append(random.randint(0, n * 10))

        # Benchmark both algorithms with statistics
        lin_mean, lin_std, lin_p1, lin_p99, lin_times = benchmark_search_with_stats(
            linear_search, arr, targets, iterations
        )
        bin_mean, bin_std, bin_p1, bin_p99, bin_times = benchmark_search_with_stats(
            binary_search, arr, targets, iterations
        )

        n_samples = len(lin_times)

        # Welch's t-test
        t_stat, df = welch_t_test(lin_mean, lin_std, n_samples,
                                  bin_mean, bin_std, n_samples)

        # Check significance at 99% level
        t_crit = t_critical_99(df)
        is_significant = abs(t_stat) > t_crit

        diff = lin_mean - bin_mean
        diff_pct = (diff / bin_mean * 100) if bin_mean > 0 else 0

        if is_significant:
            winner = "Linear" if lin_mean < bin_mean else "Binary"
            sig_marker = "Yes"
        else:
            winner = "TIE"
            sig_marker = "No"

        results.append({
            'n': n,
            'lin_mean': lin_mean,
            'bin_mean': bin_mean,
            'lin_std': lin_std,
            'bin_std': bin_std,
            'lin_p99': lin_p99,
            'bin_p99': bin_p99,
            'diff': diff,
            't_stat': t_stat,
            'significant': is_significant,
            'winner': winner
        })

        print(
            f"{n:>4} | {lin_mean:>8.3f} | {bin_mean:>8.3f} | "
            f"{lin_p99:>8.3f} | {bin_p99:>8.3f} | "
            f"{diff:>+8.3f} | {t_stat:>8.2f} | {sig_marker:>6} | {winner:>8}"
        )

    print("-" * 110)
    print()
    print("Legend:")
    print("  Linear/Binary: Mean time in microseconds (μs)")
    print("  p99: 99th percentile time (μs)")
    print("  Diff: Linear - Binary (positive = Binary faster)")
    print("  t-stat: Welch's t-statistic")
    print("  Sig?: Statistically significant at p < 0.01 (99% confidence)")
    print()

    # Analysis
    print("=" * 110)
    print("ANALYSIS")
    print("=" * 110)

    linear_wins = [r for r in results if r['winner'] == 'Linear']
    binary_wins = [r for r in results if r['winner'] == 'Binary']
    ties = [r for r in results if r['winner'] == 'TIE']

    if linear_wins:
        max_linear = max(r['n'] for r in linear_wins)
        print(
            f"Linear search significantly faster for: N = {[r['n'] for r in linear_wins]}")
    else:
        print("Linear search was NOT significantly faster for any tested size")
        max_linear = 0

    if binary_wins:
        min_binary = min(r['n'] for r in binary_wins)
        print(
            f"Binary search significantly faster starting at: N = {min_binary}")

    if ties:
        print(
            f"No significant difference (TIE) for: N = {[r['n'] for r in ties]}")

    # Find crossover point
    crossover = None
    for r in results:
        if r['winner'] == 'Binary':
            crossover = r['n']
            break

    if crossover:
        print(
            f"\nCrossover point: Binary search becomes significantly faster around N = {crossover}")

    print()
    print("=" * 110)
    print("VARIANCE ANALYSIS")
    print("=" * 110)
    print(f"{'N':>4} | {'Lin StdDev':>12} | {'Bin StdDev':>12} | {'CV Lin %':>10} | {'CV Bin %':>10}")
    print("-" * 60)

    for r in results:
        cv_lin = (r['lin_std'] / r['lin_mean'] *
                  100) if r['lin_mean'] > 0 else 0
        cv_bin = (r['bin_std'] / r['bin_mean'] *
                  100) if r['bin_mean'] > 0 else 0
        print(
            f"{r['n']:>4} | {r['lin_std']:>12.4f} | {r['bin_std']:>12.4f} | {cv_lin:>10.1f} | {cv_bin:>10.1f}")


if __name__ == "__main__":
    run_benchmark()
