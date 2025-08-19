# 🧠 latex-word-indexer

**Automatically index words in your LaTeX documents using a simple Python 3 script and a CSV word list.**

Save time and avoid manual tagging by inserting `\index{}` commands programmatically — cleanly and accurately.

---

## 🚀 Features

- ✅ Automatically inserts `\index{}` entries into your LaTeX `.tex` file
- 📄 Reads index terms from a CSV file (multiple columns or rows)
- 🧠 Avoids duplicating already indexed words
- 🧪 Case-insensitive matching
- ⚙️ Sorts words by length to avoid partial matches (e.g., "net" before "network")
- 💡 Outputs a new LaTeX file with all index tags added

---

## 📂 How It Works

You provide:
- `INDEX_LIST.csv` — a CSV file with words/phrases to index  
- `MAIN.tex` — your LaTeX source file

The script:
1. Loads and cleans the word list
2. Finds the **first appearance** of each word in the LaTeX file
3. Inserts `\index{Word}` **right after** the word (preserving casing)
4. Skips words already indexed with `\index{}` nearby
5. Writes the result to `main_indexed.tex`

---

## 🛠 Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/cyn-crypto/latex-word-indexer.git
cd latex-word-indexer
```

---

### 2️⃣ Prepare Your Input Files

#### 🗂 `INDEX_LIST.csv`

A CSV file containing the list of words or phrases you want to index.

- Words can be listed in rows or comma-separated in a single line
- Duplicates and extra spaces will be removed automatically

**Example:**
```csv
machine learning, neural network, Python
artificial intelligence
deep learning
```

#### 📄 `MAIN.tex`

Your original LaTeX document where the words appear.

**Example:**
```latex
Machine learning is a core area in AI.
Neural networks are widely used in deep learning.
Python is often used to implement models.
```

---

### 3️⃣ Run the Script

Make sure you're using Python 3:

```bash
python3 indexer.py
```

By default, the script looks for the following files in the same directory:

- `INDEX_LIST.csv`
- `MAIN.tex`

It will create a new file named:

```text
main_indexed.tex
```

This file includes all matched words tagged with LaTeX `\index{}` commands.

---

### 🧪 Output Example

**Output (`main_indexed.tex`):**
```latex
Machine learning\index{Machine Learning} is a core area in AI.
Neural networks\index{Neural Network} are widely used in deep learning.
Python\index{Python} is often used to implement models.
```

> 🧠 **Note**:  
> - Index terms are inserted using **Title Case**  
> - If a word is already indexed (i.e., `\index{}` is already present), it is **skipped** to prevent duplication
