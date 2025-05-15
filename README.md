# 🧠 ShortNote — Local Markdown Note Search WebApp

A minimal web application for quickly searching and previewing your markdown notes with a beautiful Visual Studio Code–like UI.

I created this tool to search through my personal notes saved using Obsidian, directly in a browser on my local machine — fast, pretty, and no cloud required.

---

## ✨ Features

- ⚡ Fast local keyword search in `.md` notes
- 🧪 Supports multiple comma-separated keywords
- 💻 Beautiful VS Code–style markdown preview
- 📋 Code blocks with syntax highlighting + copy button
- 🔒 Fully local – No cloud, no data leaks

---

## 📂 Folder Structure

```
shortnote/
├── backend/
│ ├── main.py
│ └── utils.py ← Set your markdown notes directory here
├── frontend/
│ └── index.html
├── venv/
└── shortnote.sh ← One-click script to run everything
```


---

## ⚙️ Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/yourusername/shortnote.git
cd shortnote
```

##3 2. Add Your Notes Path

In backend/utils.py, set the correct path to your Obsidian notes folder:

```
# backend/utils.py

NOTES_DIR = "/your/obsidian/notes/folder"
```

### 3. Setup Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

### 4. Make the Script Executable

```
chmod +x shortnote.sh
sudo mv shortnote.sh /usr/bin/
```

### 5. Start the Application

Now you can launch the entire app with:

```
shortnote.sh
```
You’ll see:

- 🟢 Backend running at: http://localhost:8000

- 🟢 Frontend running at: http://localhost:5500


## 🌐 How It Works

- Backend: FastAPI filters your markdown files from the keywords.

- Frontend: HTML + TailwindCSS UI shows live results as you type.

Code blocks in your notes (bash, python, etc.) are rendered with VS Code–style themes and copy buttons.

## 🛠️ Technologies Used

- FastAPI (Backend)
- Python 3
- Tailwind CSS (CDN)
- Markdown-it.js + Highlight.js
- Vanilla JavaScript
- Bash (shortnote.sh script)

## 📝 Why I Built This

I use Obsidian for managing my knowledge base. But I needed a clean, minimal local tool to quickly filter notes using keywords — without opening the app every time. So I built this tool with a simple UI, VS Code feel, and a 1-click launch system.

## 🧠 Author

Made with ❤️ by `AATHIL DUCKY`

If you find this useful, please ⭐ the repo.
