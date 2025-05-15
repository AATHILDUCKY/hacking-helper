# backend/utils.py

import os
import markdown2

# Change this path to your own Obsidian notes folder
NOTES_DIR = "/home/ducky/Documents/Obsidian Vault/ethical_hacking_notes"

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

    scored_notes = []

    for note in all_notes:
        content_lower = note["content"].lower()
        matched_keywords = [kw for kw in keyword_list if kw in content_lower]
        match_score = len(matched_keywords)

        if match_score > 0:
            note_copy = note.copy()
            note_copy["match_score"] = match_score
            note_copy["matched_keywords"] = matched_keywords
            scored_notes.append(note_copy)

    # Sort by match_score descending, then filename ascending
    scored_notes.sort(key=lambda note: (-note["match_score"], note["filename"]))

    return scored_notes
