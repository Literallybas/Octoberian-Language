# Octoberian Language Translator

This Python project translates inputted sentences into a fictional language called **Octoberian**. The translation follows a specific rule set to create a unique language.

## Language Rules

1. Take the **last syllable** of each word.
2. Move the last syllable to the **beginning** of the word.
3. Add **"awy"** to the end of the word.
4. Capitalize the new word if the original word was capitalized.

### Example
- **Input:** `Hello World`
- **Output:** `Lohelawy Ldworawy`

## How to Use

1. Run the Python script.
2. Enter a sentence when prompted.
3. The program will print the sentence translated into Octoberian.

### Code

```python
import re

def fun1(w):
    x = re.search(r"[

