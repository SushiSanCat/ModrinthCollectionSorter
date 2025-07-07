<p align="center">
  <img src="https://github.com/user-attachments/assets/99c145f7-25fe-4718-b5f3-23d7955684aa" width="600" alt="ModrinthCollectionSorter Logo"/>
</p>

<h1 align="center">🔃 Modrinth Collection Sorter</h1>

<p align="center">
  <a href="https://github.com/arvinjay/ModrinthCollectionSorter/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/arvinjay/ModrinthCollectionSorter?style=flat-square" alt="MIT License" />
  </a>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square" alt="Python 3.10+"/>
  <img src="https://img.shields.io/badge/platform-Windows-blue?style=flat-square" alt="Platform: Windows"/>
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square" alt="PRs Welcome"/>
</p>

---

> **✨ A Python script to _compare and sort mods between two Modrinth collections_, check for updates, and log results with a simple command-line interface.**

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔍 Mod Update Check | See which mods in a collection have updates for a target Minecraft version/loader |
| 🔄 Collection Comparison | Compare two collections: see which mods are already in the target collection |
| 📝 Logging | Results saved to easy-to-read text files |
| 🌐 Browser Integration | Optionally open all updated mod links in your browser |
| 🖥️ CLI | Simple command-line interface |

---

## ⚡ Quick Start

```bash
python modrinth_collection_sorter.py -cv 1.21.6 -tv 1.21.7 -l fabric -c HO2OnfaY -t SXY7IKoq
```

> **💡 Tip:** You can set default values for Minecraft version, loader, and collection IDs in the script or use command-line arguments as above.

---

## 📦 Requirements

- Python 3.10 or newer
- Internet connection
- Modrinth Collection IDs (source and target)

---

## 🛠️ Usage

1. Download `modrinth_collection_sorter.py`.
2. Set default values in the script or use command-line arguments:
   - `CURRENT_MINECRAFT_VERSION`
   - `TARGET_MINECRAFT_VERSION`
   - `LOADER`
   - `COLLECTION_ID` (source)
   - `TARGET_COLLECTION_ID` (target)
3. Open a terminal and navigate to the script's directory.
4. Run the script (see Quick Start above).
5. The script logs results in the `modrinth_collection_sorter_logs` directory and prints a summary.
6. If there are mods with updates, you can choose to open all their Modrinth pages in your browser.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/d994276c-6a2c-4746-8f1a-23a0333c88ba" alt="Example Configuration Screenshot" width="600" />
</p>

---

## 💡 Example Configuration

| Setting | Example Value |
|---------|--------------|
| Current Minecraft Version | `1.21.6` |
| Target Minecraft Version  | `1.21.7` |
| Loader                   | `fabric`  |
| Source Collection ID      | `HO2OnfaY`|
| Target Collection ID      | `SXY7IKoq`|

---

## 📖 Example

```bash
python modrinth_collection_sorter.py -cv 1.21.6 -tv 1.21.7 -l fabric -c HO2OnfaY -t SXY7IKoq
```

---

<h2 align="center">❓ Frequently Asked Questions</h2>

<p align="center">
  <b>Have questions? Find your answers below!</b>
</p>

<details>
<summary><b>🔗 What is a Modrinth collection?</b></summary>

A Modrinth collection is a curated group of mods on the Modrinth platform, making it easy to share and manage sets of mods for Minecraft.

</details>

<details>
<summary><b>⚙️ Can I use this script for Forge mods?</b></summary>

Absolutely! Just set the loader to <code>forge</code> (or any supported loader) and ensure your mods are compatible.

</details>

<details>
<summary><b>🧩 What if a mod is missing from the target collection?</b></summary>

The script highlights mods not present in your target collection, so you can easily spot and add them.

</details>

<details>
<summary><b>🛡️ Is this a virus?</b></summary>

No, this is <b>not</b> a virus! The script simply interacts with the Modrinth API to fetch, compare, and log mod information between collections. It does not perform any malicious actions, install unwanted software, or harm your computer in any way. You can review the code yourself for transparency and peace of mind.

</details>

<details>
<summary><b>💻 What does the code in <code>modrinth_collection_sorter.py</code> do?</b></summary>

The script is a command-line tool that helps you compare and sort mods between two Modrinth collections. Here's what it does in detail:

- <b>Connects to the Modrinth API</b> to fetch information about the mods in your source and target collections.
- <b>Checks each mod in your source collection</b> to see if there is an available update for your specified target Minecraft version and mod loader (like fabric, forge, etc).
- <b>Compares the source and target collections</b> to determine which mods are already present in the target collection and which are not.
- <b>Logs the results</b> to easy-to-read text files in a <code>modrinth_collection_sorter_logs</code> directory, showing which mods have updates and which are already in the target collection.
- <b>Optionally opens mod pages in your browser</b> for mods that have updates and are not yet in the target collection.
- Uses command-line arguments for configuration, or you can set default values in the script itself.
- Handles errors gracefully and provides a summary of the results at the end.

The script does <b>not</b> download or install any mods, nor does it modify your system in any way. It is purely a tool for comparing, checking updates, and logging information about your Modrinth collections.

</details>

---

<h2 align="center">🛠️ Supported Loaders</h2>

<p align="center">
  <b>This tool supports the most popular Minecraft mod loaders:</b>
</p>

<p align="center" style="font-size:1.2em;">
  <code>fabric</code> &nbsp;|&nbsp; <code>forge</code> &nbsp;|&nbsp; <code>quilt</code> &nbsp;|&nbsp; <code>neoforge</code>
</p>

<p align="center">
  <i>Need another loader? <a href="#contributing">Open an issue or contribute!</a></i>
</p>

---

<h2 align="center">🤝 Contributing</h2>

<p align="center">
  <b>Want to make this project even better?</b><br/>
  Contributions, ideas, and suggestions are always welcome!
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square" alt="PRs Welcome" />
</p>

<p align="center">
  <b>How to contribute:</b>
</p>

<ul align="center">
  <li>🍴 Fork this repository</li>
  <li>🌱 Create a new branch for your feature or fix</li>
  <li>💡 Make your changes and commit them</li>
  <li>🚀 Open a pull request describing your changes</li>
</ul>

<p align="center">
  <i>Please follow the existing style and add helpful documentation where needed.</i>
</p>

---

<h2 align="center">📄 License</h2>

<p align="center">
  <img src="https://img.shields.io/github/license/arvinjay/ModrinthCollectionSorter?style=flat-square" alt="MIT License" />
</p>

<p align="center">
  <b>This project is licensed under the MIT License.</b><br/>
  <a href="LICENSE">View full license &rarr;</a>
</p>
