# **Bitwise Operators in Python - Complete Tutorial**

Bitwise operators are used to perform operations on binary numbers at the bit level. These operators are essential in low-level programming, cryptography, and optimization tasks.

---

## **1. Understanding Binary Numbers**
Before diving into bitwise operators, let's briefly recap binary numbers:
- Binary numbers are base-2 (only `0` and `1`).
- Example: `5` in binary is `0101`.

Python provides built-in functions to convert between binary and decimal:
```python
num = 5
binary = bin(num)  # '0b101' (0b prefix indicates binary)
decimal = int('101', 2)  # 5
```

---

## **2. Bitwise Operators in Python**
Python supports the following bitwise operators:

| Operator | Name               | Description                                                                 |
|----------|--------------------|-----------------------------------------------------------------------------|
| `&`      | AND                | Sets each bit to `1` if both bits are `1`.                                  |
| `\|`     | OR                 | Sets each bit to `1` if at least one of the bits is `1`.                   |
| `^`      | XOR                | Sets each bit to `1` if only one of the bits is `1`.                       |
| `~`      | NOT                | Inverts all bits (unary operator).                                         |
| `<<`     | Left Shift         | Shifts bits to the left, filling with `0`s.                                |
| `>>`     | Right Shift        | Shifts bits to the right, filling based on sign bit.                       |

---

## **3. Bitwise Operator Examples**
Let's explore each operator with examples.

### **3.1 Bitwise AND (`&`)**
Returns `1` only if both bits are `1`.

**Example:**
```python
a = 5    # 0101
b = 3    # 0011
result = a & b  # 0001 (1 in decimal)
print(result)   # Output: 1
```

### **3.2 Bitwise OR (`|`)**
Returns `1` if at least one bit is `1`.

**Example:**
```python
a = 5    # 0101
b = 3    # 0011
result = a | b  # 0111 (7 in decimal)
print(result)   # Output: 7
```

### **3.3 Bitwise XOR (`^`)**
Returns `1` if the bits are different.

**Example:**
```python
a = 5    # 0101
b = 3    # 0011
result = a ^ b  # 0110 (6 in decimal)
print(result)   # Output: 6
```

### **3.4 Bitwise NOT (`~`)**
Inverts all bits (including sign bit, so it's equivalent to `-x - 1`).

**Example:**
```python
a = 5    # 0101
result = ~a  # Inverts to 1010 (but in 2's complement, this is -6)
print(result)   # Output: -6
```

### **3.5 Left Shift (`<<`)**
Shifts bits left, filling with `0`s. Equivalent to multiplying by `2^n`.

**Example:**
```python
a = 5    # 0101
result = a << 1  # 1010 (10 in decimal)
print(result)    # Output: 10
```

### **3.6 Right Shift (`>>`)**
Shifts bits right, filling based on sign bit. Equivalent to dividing by `2^n`.

**Example:**
```python
a = 5    # 0101
result = a >> 1  # 0010 (2 in decimal)
print(result)    # Output: 2
```

---

## **4. Practical Applications**
Bitwise operators are useful in:
1. **Flags & Permissions** (e.g., `READ = 1`, `WRITE = 2`, `EXECUTE = 4`).
2. **Efficient Multiplication/Division** (using `<<` and `>>`).
3. **Cryptography & Hashing** (XOR is common in encryption).
4. **Optimized Storage** (packing multiple values into a single integer).

**Example: Checking if a number is even or odd using `&`**
```python
num = 6
if num & 1:
    print("Odd")
else:
    print("Even")  # Output: Even
```

---

## **5. Summary Table**
| Operation | Example | Result (Binary) | Result (Decimal) |
|-----------|---------|------------------|------------------|
| `a & b`   | `5 & 3` | `0001`           | `1`              |
| `a | b`   | `5 | 3` | `0111`           | `7`              |
| `a ^ b`   | `5 ^ 3` | `0110`           | `6`              |
| `~a`      | `~5`    | `1010` (2's comp)| `-6`             |
| `a << 1`  | `5 << 1`| `1010`           | `10`             |
| `a >> 1`  | `5 >> 1`| `0010`           | `2`              |

---

## **6. Common Pitfalls**
1. **Sign Bit Handling**: `~` (NOT) works on signed integers, leading to negative results.
2. **Operator Precedence**: Bitwise operators have lower precedence than arithmetic operators.
   ```python
   result = 5 + 3 << 1  # Equivalent to (5 + 3) << 1 = 16
   ```
3. **Overflow**: Shifting beyond bit limits can lead to unexpected results.

---

## **7. Conclusion**
Bitwise operators are powerful tools for low-level manipulation. They are widely used in:
- Performance optimizations
- Embedded systems
- Network protocols
- Cryptography

Practice these operations to master them!

Would you like additional examples or explanations on any specific part? 😊
