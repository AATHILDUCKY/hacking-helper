# backend/utils.py

import os
import markdown2

NOTES_DIR = "notes"

def load_notes():
    notes = []
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith(".md"):
            path = os.path.join(NOTES_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                notes.append({
                    "filename": filename,
                    "content": content,
                    "html": markdown2.markdown(content)
                })
    return notes

def search_notes(keywords):
    keyword_list = [k.strip().lower() for k in keywords.split(",") if k.strip()]
    all_notes = load_notes()
    matched = []

    for note in all_notes:
        text = note["content"].lower()
        if all(keyword in text for keyword in keyword_list):
            matched.append(note)

    return matched
