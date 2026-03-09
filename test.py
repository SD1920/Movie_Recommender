import numpy as np

print("=== WITHOUT SEED (Random Results) ===")
print("Run 1:")
print("Random numbers:", np.random.rand(5))
print("Random integers:", np.random.randint(1, 100, 3))

print("\nRun 2:")
print("Random numbers:", np.random.rand(5))
print("Random integers:", np.random.randint(1, 100, 3))

print("\n=== WITH SEED (Reproducible Results) ===")
print("Run 1 with seed=23:")
np.random.seed(23)
print("Random numbers:", np.random.rand(5))
print("Random integers:", np.random.randint(1, 100, 3))

print("\nRun 2 with seed=23:")
np.random.seed(23)  # Reset to same seed
print("Random numbers:", np.random.rand(5))
print("Random integers:", np.random.randint(1, 100, 3))

print("\n=== PRACTICAL EXAMPLE: Data Splitting ===")
# Imagine you're splitting data for machine learning
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Without seed - different splits each time:")
shuffled1 = np.random.permutation(data)
train1, test1 = shuffled1[:7], shuffled1[7:]
print(f"Train: {train1}, Test: {test1}")

shuffled2 = np.random.permutation(data)
train2, test2 = shuffled2[:7], shuffled2[7:]
print(f"Train: {train2}, Test: {test2}")

print("\nWith seed - identical splits every time:")
np.random.seed(42)
shuffled1 = np.random.permutation(data)
train1, test1 = shuffled1[:7], shuffled1[7:]
print(f"Train: {train1}, Test: {test1}")

np.random.seed(42)  # Same seed
shuffled2 = np.random.permutation(data)
train2, test2 = shuffled2[:7], shuffled2[7:]
print(f"Train: {train2}, Test: {test2}")

print("\n=== KEY POINTS ===")
print("1. Without seed: Results change every time you run")
print("2. With seed: Same results every time (reproducible)")
print("3. Different seed values give different sequences")
print("4. Essential for scientific reproducibility!")