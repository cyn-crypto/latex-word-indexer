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

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/latex-word-indexer.git
cd latex-word-indexer
