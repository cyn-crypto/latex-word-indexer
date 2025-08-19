# 🧠 latex-word-indexer

**Automatically insert `\index{}` commands into your LaTeX documents using a CSV word list. Save time, stay consistent, and simplify your indexing process.**

---

## 📌 Overview

Indexing in LaTeX can be tedious — especially when you're dealing with long documents like theses, technical books, or research papers. `latex-word-indexer` is a Python 3 tool that scans your LaTeX file and inserts `\index{}` commands for words listed in a CSV file.

No more manually tagging entries. Just give it your word list and LaTeX source — it does the rest.

---

## 🚀 Features

- ✅ **Automatic indexing**: Add `\index{}` commands throughout your LaTeX file
- 📄 **CSV input**: Easily manage index terms in a spreadsheet
- ⚙️ **Customizable**: Clean Python code, easy to tweak
- 💨 **Fast**: Processes large files in seconds
- 🧪 **Accurate**: Avoids re-indexing already tagged terms

---

## 📂 How It Works

### You provide:
- A **CSV file** with words or phrases to be indexed (one per line or as comma-separated)
- A **LaTeX `.tex` file** where those words should be indexed

### The script:
- Scans the LaTeX file
- Searches for occurrences of each word
- Inserts `\index{word}` right after the first occurrence of each word
- Outputs a modified LaTeX file ready for use with `makeindex` or `imakeidx`

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/latex-word-indexer.git
cd latex-word-indexer
python3 indexer.py
