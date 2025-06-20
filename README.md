# CleanerVV 🧹⚙️

[![License: MIT](https://img.shields.io/github/license/CSDC-K/CleanerVV?style=for-the-badge)](LICENSE)
![Platform: Windows](https://img.shields.io/badge/Platform-Windows%2010%2B-00adee?style=for-the-badge&logo=windows)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge)

<p align="center">
  <img src="docs/cleaner_demo.gif" alt="CleanerVV Demo" width="1200" height="600">
</p>

> **CleanerVV** is a powerful, fully offline Python-based cleaner for Windows. It offers user-selectable cleaning operations including temp folders, startup folder, SoftwareDistribution, and DNS flushing. Configuration is managed via an interactive CLI and saved to `config.json`, while all actions are logged in `LOG.txt`.

---

## ✨ Features

|  | Capability |
|:--|:--|
| 🧹 **Temp Folder Cleanup** | Deletes user-level and Windows temp directories. |
| 🚫 **Startup Folder Wipe** | Removes files from the startup folder to prevent auto-launch programs. |
| 🔄 **SoftwareDistribution Flush** | Cleans cached Windows Update files. |
| 🌐 **DNS Cache Flush** | Runs `ipconfig /flushdns` automatically. |
| ⚙️ **Interactive CLI Config** | Toggle cleaning targets using a styled checkbox menu (via InquirerPy). |
| 🪵 **Auto Logging** | All cleanup results are logged to `LOG.txt` with timestamped summaries. |
| 🐍 **Lightweight Python Script** | No GUI required — runs smoothly in terminal. |

---

## 🗂️ Project Layout

```text
CleanerVV/
├── vv clean.py         # Main CLI logic, cleanup engine & menus
├── config.json         # Stores toggleable cleanup options
├── requirements.txt    # Python dependencies
├── LOG.txt             # Latest cleanup log with actions taken
└── README.md           # You're reading it.
```

---

## 🚀 Getting Started

### Prerequisites

- Windows 10/11
- Python 3.10 or newer

### Installation

```bash
# 1. Clone the repo
$ git clone https://github.com/CSDC-K/CleanerVV.git
$ cd CleanerVV

# 2. (Optional) Set up virtual environment
$ python -m venv .venv
$ .\.venv\Scripts\activate

# 3. Install required packages
$ pip install -r requirements.txt

# 4. Run the program
$ python "vv clean.py"
```

---

## 🧼 Usage Overview

- On launch, you'll see a terminal-based ASCII UI.
- Use arrow keys to choose:
  - `Start Clean`: Performs cleanup based on `config.json`
  - `Options`: Toggle folders and actions to be cleaned
  - `Credits`: Display author/company info
  - `Exit`: Quit the app

> Results of each clean are saved to `LOG.txt` with date and time.

---

## 🧾 Requirements

Dependencies as defined in [`requirements.txt`](requirements.txt):

```txt
InquirerPy
pystyle
ctypes
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

## ✨ Developed With Precision By

<p align="center">
  <strong style="font-size: 1.3em; letter-spacing: 1px;">⚡ VV / KUZEY ⚡</strong><br>
  <em>Cleaning your system with elegance and raw Python power.</em>
</p>
