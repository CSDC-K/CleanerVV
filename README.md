# CleanerVV 🧹⚙️

[![License: MIT](https://img.shields.io/github/license/CSDC-K/CleanerVV?style=for-the-badge)](LICENSE)
![Platform: Windows](https://img.shields.io/badge/Platform-Windows%2010%2B-00adee?style=for-the-badge&logo=windows)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge)

<p align="center">
  <img src="docs/cleaner_demo.gif" alt="CleanerVV Demo" width="1200" height="600">
</p>

> **CleanerVV** is a sleek, offline Python utility to clean up temporary files, broken registry paths, and general PC junk. Built with CustomTkinter for a modern look and feel.

---

## ✨ Features

|  | Capability |
|:--|:--|
| 🧹 **Deep System Cleaning** | Automatically deletes temp files, recent files, and other unnecessary clutter. |
| 📂 **Targeted Folder Cleanup** | Removes contents from common junk locations like `%temp%`, `prefetch`, and more. |
| 🧠 **Registry Cleaner (Static)** | Predefined cleanup of known problematic registry entries. |
| 🧼 **One-Click Clean** | Simplified user interface with just a single click to start cleanup. |
| 🖼️ **Modern UI** | Uses CustomTkinter for a stylish and minimal interface. |
| 🔐 **Offline Operation** | Runs entirely offline with no dependencies on external services. |

---

## 🗂️ Project Layout

```text
CleanerVV/
├── main.py                 # GUI entry point
├── core/
│   ├── clean_temp.py       # Handles deletion of temp files
│   ├── clean_registry.py   # Registry logic (static)
│   └── paths.py            # Common junk paths definitions
├── assets/
│   └── icons/              # Optional icons for UI
├── docs/
│   └── cleaner_demo.gif    # Demonstration visual
├── requirements.txt        # Dependency list
└── LICENSE
```

---

## 🚀 Getting Started

### Prerequisites

* Windows 10/11
* Python **3.10+**

### Installation

```bash
# 1. Clone the repository
$ git clone https://github.com/CSDC-K/CleanerVV.git
$ cd CleanerVV

# 2. Set up a virtual environment (optional but recommended)
$ python -m venv .venv
$ .\.venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Launch the cleaner
$ python main.py
```

---

## 🧼 How It Works

1. Launch the program.
2. Click the **Clean** button.
3. The system will clean up temp files and optionally target known junk folders.
4. Optionally, registry keys are purged from known static problem areas.
5. Progress is shown in real time.

> **Note:** The tool avoids aggressive registry editing. It is safe for general use, but advanced users can modify `clean_registry.py`.

---

## 🧾 Requirements

Dependencies are listed in [`requirements.txt`](requirements.txt):

```text
customtkinter
ctypes
shutil
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Roadmap

- [ ] Add optional aggressive registry cleaner
- [ ] Add scheduling support to clean periodically
- [ ] System tray minimization
- [ ] GUI themes (dark/light mode)

---

## 🤝 Contributing

1. Fork the repo & create your branch: `git checkout -b feature/cleanup-enhancement`
2. Commit your changes: `git commit -m "✨ Add feature"`
3. Push to GitHub: `git push origin feature/cleanup-enhancement`
4. Open a **Pull Request** ✅

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## ✨ Developed With Precision By

<p align="center">
  <strong style="font-size: 1.3em; letter-spacing: 1px;">⚡ VV / KUZEY ⚡</strong><br>
  <em>Cleaning your system with elegance and raw Python power.</em>
</p>
