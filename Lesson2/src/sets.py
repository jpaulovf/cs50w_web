# Empty set
s = set()

# Adding elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

# Adding 3 again
s.add(3)
print(s)

# Remove from set
s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")