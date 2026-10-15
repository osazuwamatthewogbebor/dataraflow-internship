# dataraflow-cohort-2

6-month intense learning experience that unites determination with personal development. The program teaches data science and ML and Gen AI through daily learning objectives and weekly assignments and peer accountability systems which lead to mastery of these subjects. This is not self-paced. This is self-forged.

## Environment setup (do this first)

Follow the steps for **your operating system**. By the end you'll have VS Code, Python, and
a virtual environment with Jupyter ready to run the course notebooks.

### 1. Install VS Code

VS Code is the code editor we use to open and run the `.ipynb` notebooks.

- **Windows & Mac:** download from <https://code.visualstudio.com/> and run the installer.
  - *Windows:* during install, tick **"Add to PATH"** and **"Register Code as an editor for supported file types."**
  - *Mac:* drag **Visual Studio Code** into your **Applications** folder.
- Open VS Code, go to the **Extensions** panel (the four-squares icon), and install the
  **Python** and **Jupyter** extensions (both by Microsoft).

### 2. Install Python

We recommend **Python 3.11 or newer**.

**Windows**
1. Download the installer from <https://www.python.org/downloads/windows/>.
2. Run it and — importantly — check **"Add python.exe to PATH"** on the first screen, then
   click **Install Now**.
3. Verify in a new terminal (PowerShell):
   ```powershell
   python --version
   pip --version
   ```

**Mac**
1. The easiest route is [Homebrew](https://brew.sh/). Install Homebrew (if you don't have
   it), then:
   ```bash
   brew install python
   ```
   *(Alternatively, download the macOS installer from <https://www.python.org/downloads/macos/>.)*
2. Verify in Terminal:
   ```bash
   python3 --version
   pip3 --version
   ```

### 3. Open the project in VS Code

Download/clone this project, then in VS Code choose **File → Open Folder…** and select the
`dataraflow-cohort-2` folder. Open a terminal inside VS Code with **Terminal → New Terminal**.
Run the remaining commands from that terminal (it starts in the project folder).

### 4. Create a virtual environment

A virtual environment (`venv`) keeps this project's packages separate from the rest of your
system. Create one named `.myenv` in the project folder:

**Windows (PowerShell)**
```powershell
python -m venv .myenv
```

**Mac (Terminal)**
```bash
python3 -m venv .myenv
```

### 5. Activate the virtual environment

You must **activate** the environment each time you open a new terminal for this project.
When it's active, your prompt shows `(.myenv)` at the start.

**Windows (PowerShell)**
```powershell
.myenv\Scripts\Activate.ps1
```
> If PowerShell blocks the script with an execution-policy error, run this once, then
> activate again:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> On **Command Prompt (cmd)** instead of PowerShell, use: `.myenv\Scripts\activate.bat`

**Mac (Terminal)**
```bash
source .myenv/bin/activate
```

To leave the environment later, just run `deactivate`.

### 6. Install Jupyter and register the kernel

With the environment **active**, upgrade `pip` and install Jupyter, the notebook kernel
(`ipykernel`), and the core data libraries. Use `pip` after activation (not `pip3`):

```bash
pip install --upgrade pip
pip install jupyter ipykernel pandas numpy matplotlib seaborn scikit-learn
```

Register this environment as a Jupyter kernel so VS Code (and Jupyter) can find it:

```bash
python -m ipykernel install --user --name dataraflow --display-name "Python (dataraflow)"
```

### 7. Select the kernel and run a notebook

1. Open any `.ipynb` file in VS Code.
2. Click **Select Kernel** in the top-right of the notebook.
3. Choose **Python (dataraflow)** (the kernel you just registered).
4. Run a cell with **Shift + Enter**. You're ready!

> **Database access:** to pull the course datasets you'll also install `pymssql`,
> `sqlalchemy`, and `python-dotenv` — see the next section.

## Working with the cohort database

From **Week 6 onward**, the datasets you need are in a cloud **SQL database**, and you retrieve them yourself with
SQL. Learning to query a database is a core data skill, and you'll build it a little at a
time alongside each week's topic.

**Start here:** [`Week-3 (Python - 3)/7-Introduction to SQL.md`](<Week-3 (Python - 3)/7-Introduction to SQL.md>) — a from-scratch SQL primer.

### Where each week's data lives

| Schema | Week(s) |
|--------|---------|
| `week06` | Week 6 — Numpy & Pandas-1 (airport weather, WHO TB) |
| `week07` | Week 7 — Data Analysis Pandas-2 (London weather) |
| `week08` | Week 8 — Advanced Pandas-1 (World Bank GDP/LE/POP) |
| `week09` | Week 9 — Advanced Pandas-2 (UN Comtrade milk trade) |
| `week14`–`week19` | Regression, Classification, Clustering & NLP task/assignment/assessment datasets |

Every data-bearing week has a **`Data Access (SQL).md`** file listing that week's tables
and worked examples for pulling, joining, aggregating, and exporting its data.

### Getting connected (once)

1. **Whitelist your IP.** The database firewall blocks unknown computers. Find your public
   IP (search "what is my IP") and send it to your program admin to be added to the
   allow-list.
2. **Install the driver:**
   ```bash
   pip install pymssql pandas sqlalchemy python-dotenv
   ```
3. **Create a `.env`** in the project root with the read-only credentials your admin gives
   you:
   ```
   SQL_SERVER_NAME=df-cohort2.database.windows.net
   SQL_SERVER_DATABASE=assessmentDB
   SQL_READONLY_USERNAME=intern_readonly
   SQL_READONLY_PASSWORD=<given to you by the admin>
   ```

### Pulling data in a notebook

```python
import sys, pathlib
_p = pathlib.Path.cwd()
while _p != _p.parent and not (_p / "db" / "dataraflow_db.py").exists():
    _p = _p.parent
sys.path.insert(0, str(_p))
from db.dataraflow_db import run_query

df = run_query("SELECT * FROM week08.wb_gdp_2013")
df.head()
```

Your read-only login can `SELECT` freely but cannot change any data, so experiment away.

# dataraflow-internship
# dataraflow-internship
