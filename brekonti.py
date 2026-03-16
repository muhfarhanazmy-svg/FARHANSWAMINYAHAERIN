print("instruksi break:")
for i in range(1,6):
    if i == 3:
        break
    print("bagian ini ada di dalam loop", i)
print("bagian ini ada di luar loop")

print("\ninstruksi continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("bagian ini ada di dalam loop", i)
print("bagian ini ada di luar loop")