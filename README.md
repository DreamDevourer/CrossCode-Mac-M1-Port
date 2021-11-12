<h1 align="center">CrossCode Mac M1 Native Patcher 🦿</h1>

<p align="center">This is just a simple patcher for CrossCode to work natively on M1 Macs. This patch contains compiled darwin aarch64 binaries of NWJS.</p>

<p align="center">
  <a href="./LICENSE">License</a>
</p>

<img src="./sample.jpg" alt="Native ARM64 build.">

## ⚙️ Instructions

Before starting make sure you have Python 3.7 or later installed.

```bash
brew install python3
```

1 - Download the zip of master branch manually or by running:

```bash
git clone https://github.com/DreamDevourer/CrossCode-Mac-M1-Port.git
```

2 - Extract the files inside the aarch64/NWJS.xz, the folder structure needs to look like this after the extraction:

```bash
aarch64
├── MacOS
├── Frameworks
├── Resources
├── PkgInfo
└── info.plist
```

3 - move the installer.py with the aarch64 folder to where the CrossCode.app is located (Your steam default installation folder probably).

4 - Open the terminal where the script is located and run:

```bash
python3 installer.py
```

5 - After the patch is done, you can run CrossCode.app normally. Also make sure to test it in Activity Monitor.


## 📄 License

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

| Permissions | Restrictions | Conditions
| --- | --- | --- 
&check; Commercial Use | &times; Liability | &#x1f6c8; License and Copyright Notice
&check; Modification   | &times; Warranty | &#x1f6c8; State changes
&check; Distribution |  | &#x1f6c8; Disclose source
&check; Patent Use |  | &#x1f6c8; Same license
&check; Private Use
