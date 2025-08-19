# -*- coding: utf-8 -*-
"""Indexing.ipynb
"""

#This script helps you to index words provided in csv file into the latex file.
import csv
import re
from pathlib import Path

def load_words_from_csv(csv_path):
    """Read words from a CSV file (deduplicate and trim spaces)."""
    words = set()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row:
                word = item.strip()
                if word:
                    words.add(word)
    # Sort by length (longest first) to avoid partial matches
    return sorted(words, key=lambda x: -len(x))

def index_latex_text(text, words):
    for word in words:
        # Skip if already indexed somewhere
        if re.search(rf"\\index\{{\s*{re.escape(word)}\s*\}}", text, re.IGNORECASE):
            continue

        # Find all matches of the word
        matches = list(re.finditer(rf"\b{re.escape(word)}\b", text, re.IGNORECASE))
        inserted = False

        for match in matches:
            start, end = match.span()
            # Check if substring near match is already indexed
            # Look around match to see if \index{word} follows immediately
            after_match = text[end:end + 20]  # look 20 chars after word

            if re.match(rf"\\index\{{\s*{re.escape(word)}\s*\}}", after_match, re.IGNORECASE):
                # Already indexed here, skip
                inserted = True
                break

            else:
                # Insert \index{word} after this occurrence and break
                text = text[:end] + f"\\index{{{word.title()}}}" + text[end:]
                inserted = True
                print(f"Indexed: {word}")
                break

        if not inserted:
            print(f"Skipped (not found): {word}")

    return text

if __name__ == "__main__":
    csv_file = r"INDEX_LIST.csv"       # replace "INDEX_LIST.csv" with the path of your csv file containing all the words to be indexed
    tex_file = r"MAIN.tex"             # replace "MAIN.tex" with the path of your latex(i.e. .tex file)
    output_file = "main_indexed.tex"  # new file to save with indexes

    # Load CSV words
    words_to_index = load_words_from_csv(csv_file)
    print(f"Loaded {len(words_to_index)} words from CSV.")

    # Read original .tex
    original_text = Path(tex_file).read_text(encoding='utf-8')

    # Process text
    indexed_text = index_latex_text(original_text, words_to_index)

    # Save new indexed .tex
    Path(output_file).write_text(indexed_text, encoding='utf-8')
    print(f"Indexed file saved as: {output_file}")