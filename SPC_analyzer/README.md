# SPC Quality Control Analyzer with Python & SQLite

##  Overview
This projetc demonstrates a **Statistical Process Control (SPC)** workflow using Python. It simulates a manufacturing process, stores measurement data in a **SQLite database**, and performs quality analysis using **Pandas** and **Matplotlib**.

## 🚀 Features
* **Data Simulation:** Generates realistic manufacturing data (Normal Distribution).
* **Database Management:** Uses `sqlite3` to store and retrieve process data.
* **Statistical Analysis:** Calculates Mean, Standard Deviation, and Contrlo Limits (UCL/LCL).
* **Process Capability:** Computes the Cpk index to evaluate process performance against specification limits (USL/LSL).
* **Visualization:** Generates an automated **Control Chart (X-bar)**.

## 🛠️ Tech Stack
* **Python** (Core Logic)
* **SQLite** (Data Storage)
* **Pandas** (Data Manipulation)
* **Matplotlib** (Data Visualization)

## Output 
 script generates a Control Chart visualizing the process stability and highlighting any outliers outside the 3-sigma limits.
