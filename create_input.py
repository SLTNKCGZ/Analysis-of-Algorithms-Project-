'''
import random

def generate_input_file(size):
    def first_element_majority():
        majority = 1
        rest = [random.randint(2, 100) for _ in range(size // 2 - 1)]
        arr = [majority] * (size // 2 + 1) + rest
        random.shuffle(arr[1:])
        return arr

    def no_majority():
        arr = []
        for i in range(1, size // 10 + 1):
            arr.extend([i] * 10)
        random.shuffle(arr)
        return arr[:size]

    def reversed_majority():
        majority = 7
        majority_count = size // 2 + 1
        rest_count = size - majority_count
        rest = list(range(100, 100 + rest_count))
        arr = [majority] * majority_count + rest
        arr.sort(reverse=True)
        return arr


    def random_majority():
        majority = 99
        rest = [random.randint(1, 98) for _ in range(size - (size // 2 + 1))]
        arr = [majority] * (size // 2 + 1) + rest
        random.shuffle(arr)
        return arr

    def sorted_array():
        return list(range(1, size + 1))

    def reversed_array():
        return list(range(size, 0, -1))

    def fixed_percentage_same_value(percentage):
        repeat_count = int(size * percentage)
        fixed_value = random.randint(1, 50)
        
        rest = []
        while len(rest) < size - repeat_count:
            val = random.randint(51, 100)
            if val != fixed_value:
                rest.append(val)

        arr = [fixed_value] * repeat_count + rest
        return arr
    
    scenarios = {
        "# First Element is Majority": first_element_majority(),
        "# No Majority": no_majority(),
        "# Reversed with Majority": reversed_majority(),
        "# Randomly Distributed Majority": random_majority(),
        "# Sorted Ascending": sorted_array(),
        "# Sorted Descending": reversed_array(),
        "# 10% Same Value": fixed_percentage_same_value(0.10),
        "# 20% Same Value": fixed_percentage_same_value(0.20),
        "# 30% Same Value": fixed_percentage_same_value(0.30),
        "# 40% Same Value": fixed_percentage_same_value(0.40),
        "# 50% Same Value": fixed_percentage_same_value(0.50),
    }

    with open(f"input_{size}.txt", "w") as f:
        for title, arr in scenarios.items():
            f.write(f"{title}\n")
            f.write(str(arr) + "\n\n")

# Dosyaları oluşturma
sizes = [1000, 3000, 5000, 10000, 12500, 15000, 20000, 25000, 37500, 50000]
for size in sizes:
    generate_input_file(size)

''' 
import random

def generate_input_file(size):
    def pure_majority():
        """Tüm elemanlar aynı (tam majority)"""
        return [random.randint(1,100)] * size
    
    def balanced_pairs():
        """Elemanlar çiftler halinde (hiç majority yok)"""
        pairs = [(i, i) for i in range(1, size//2 + 1)]
        arr = [item for pair in pairs for item in pair]
        if len(arr) < size:
            arr.append(size//2 + 1)
        random.shuffle(arr)
        return arr
    
    def first_element_majority():
        """Majority element array'ın başında"""
        majority = random.randint(1,20)
        majority_count = size//2 + 1
        rest = [random.randint(20, 100) for _ in range(size - majority_count)]
        arr = [majority] * majority_count + rest
        random.shuffle(arr[1:])  # Sadece ilk elemandan sonrasını karıştır
        return arr

    def last_element_majority():
        """Majority element array'ın sonunda"""
        majority = random.randint(1,20)
        majority_count = size//2 + 1
        rest = [random.randint(20, 100) for _ in range(size - majority_count)]
        arr = rest + [majority] * majority_count
        return arr

    def all_unique_elements():
        """Tüm elemanlar unique"""
        return random.sample(range(1, size*2), size)

    def balanced_half_elements():
        """Tam yarı yarıya bölünmüş durum"""
        half = size // 2
        val1, val2 = random.sample(range(1,101), 2)
        return [val1] * half + [val2] * (size - half)

    def random_early_majority():
        """Majority element rastgele yerde"""
        majority = random.randint(1,100)
        majority_count = size//2 + 1
        rest = [random.randint(1, 100) for _ in range(size - majority_count)]
        arr = [majority] * majority_count + rest
        random.shuffle(arr)
        return arr

    def random_late_majority():
        """Majority element genelde array'ın sonlarına doğru"""
        majority = random.randint(1,100)
        majority_count = size//2 + 1
        rest = [random.randint(1, 100) for _ in range(size - majority_count)]
        # Majority elemanlarını son %25'e yerleştir
        pos = int(size * 0.75)
        arr = rest[:pos] + [majority] * majority_count + rest[pos:]
        return arr

    def periodic_distribution():
        """Majority element belirli periyotlarla dağılmış"""
        majority = random.randint(1,100)
        arr = []
        majority_count = 0
        target = size//2 + 1
        
        for i in range(size):
            if i % 3 == 0 and majority_count < target:
                arr.append(majority)
                majority_count += 1
            else:
                arr.append(random.randint(1, 100))
        
        # Eksik majority elemanlarını rastgele pozisyonlara ekle
        while majority_count < target:
            idx = random.randint(0, size-1)
            if arr[idx] != majority:
                arr[idx] = majority
                majority_count += 1
        return arr

    
    def sorted_ascending():
        return list(range(1, size + 1))

    def sorted_descending():
        return list(range(size, 0, -1))

    scenarios = [
        ("Pure Majority", pure_majority),
        ("Balanced Pairs", balanced_pairs),
        ("First Element Majority", first_element_majority),
        ("Last Element Majority", last_element_majority),
        ("All Unique Elements", all_unique_elements),
        ("Balanced Half Elements", balanced_half_elements),
        ("Random Early Majority", random_early_majority),
        ("Random Late Majority", random_late_majority),
        ("Periodic Distribution", periodic_distribution),
        ("Sorted Ascending", sorted_ascending),
        ("Sorted Descending", sorted_descending)
    ]

    with open(f"input_{size}.txt", "w") as f:
        for name, func in scenarios:
            f.write(f"# {name}\n")
            f.write(str(func()) + "\n\n")

# Farklı boyutlarda dosyalar oluştur
sizes = [1000, 3000, 5000, 10000, 12500, 15000, 20000, 25000, 37500, 50000]
for size in sizes:
    generate_input_file(size)