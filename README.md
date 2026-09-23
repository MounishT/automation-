# 🐍 Python Basic Programs

This repository contains three simple Python programs for practice:

1. Binary Numbers Divisible by 5
2. Count Letters and Digits in a Sentence
3. Factorial of a Number

---

## 📌 1. Binary Numbers Divisible by 5

### 🔹 Problem Statement

Write a Python program that accepts a sequence of comma-separated **4-digit binary numbers** and prints only those numbers which are **divisible by 5**.

---

### 🔹 Example

**Input:**

```
0100,0011,1010,1001
```

**Output:**

```
1010
```

---

### 🔹 Code

```python
binary_input = input("ENTER COMMA SEPARTED 4-DIGIT BINARY NUMBER: ")
binary_list = binary_input.split(',')

result = []

for b in binary_list:
    decimal = int(b, 2)
    if decimal % 5 == 0:
        result.append(b)

print(",".join(result))
```

---

### 🔹 Explanation Table

| Binary | Decimal | Divisible by 5 | Output |
| ------ | ------- | -------------- | ------ |
| 0100   | 4       | ❌ No           | -      |
| 0011   | 3       | ❌ No           | -      |
| 1010   | 10      | ✅ Yes          | ✔      |
| 1001   | 9       | ❌ No           | -      |

---

## 📌 2. Count Letters and Digits

### 🔹 Problem Statement

Write a Python program that accepts a sentence and counts the number of:

* Letters
* Digits

---

### 🔹 Example

**Input:**

```
hello world! 123
```

**Output:**

```
LETTERS 10
DIGITS 3
```

---

### 🔹 Code

```python
sentence = input("ENTER A SENTENCE: ")

letters = 0
digits = 0

for ch in sentence:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)
```

---

### 🔹 Explanation Table

| Character Type | Count   |
| -------------- | ------- |
| Letters        | 10      |
| Digits         | 3       |
| Others         | Ignored |

---

## 📌 3. Factorial of a Number

### 🔹 Problem Statement

Write a Python program to compute the **factorial of a given number**.

---

### 🔹 Example

**Input:**

```
8
```

**Output:**
``
