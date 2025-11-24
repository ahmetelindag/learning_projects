import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Connect to SQLite database (creates file if not exists)
db_name = 'quality_control.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Columns: ID, Timestamp, Value, Operator Name
cursor.execute('''
CREATE TABLE IF NOT EXISTS measurements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP,
    value REAL,
    operator TEXT
)
''')
conn.commit()

print(f" Database '{db_name}' and table  are ready!")

cursor.execute('DELETE FROM measurements')

print(" Simulating manufacturing data and writing to SQLite...")

# Simulation Parameters
np.random.seed(42)  # For reproducibility
target_value = 10.0 # Target diameter in mm
std_dev = 0.1       # Process standard deviation
sample_size = 100   # Number of samples
start_time = datetime.now()

for i in range(sample_size):
    # Generate random value based on normal distribution
    measured_val = np.random.normal(target_value, std_dev)
    
    # Simulate time intervals (e.g., every 5 minutes)
    record_time = start_time + timedelta(minutes=i*5)
    
    # Insert into Database
    cursor.execute('INSERT INTO measurements (timestamp, value, operator) VALUES (?, ?, ?)', 
                   (record_time, measured_val, 'Operator_Ahmet'))

conn.commit()
print(f" {sample_size} records successfully inserted into database.")





query = "SELECT * FROM measurements"
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()


mean = df['value'].mean()
sigma = df['value'].std()

# Calculate Control Limits (3-Sigma Rule)
UCL = mean + (3 * sigma) # Upper Control Limit
LCL = mean - (3 * sigma) # Lower Control Limit

# Calculate Process Capability Index (Cpk)
# Customer Specs: USL = 10.3mm, LSL = 9.7mm
USL, LSL = 10.3, 9.7
cpu = (USL - mean) / (3 * sigma)
cpl = (mean - LSL) / (3 * sigma)
cpk = min(cpu, cpl)

print(f"\n--- SPC REPORT ---")
print(f"Process Mean : {mean:.4f}")
print(f"Process Sigma: {sigma:.4f}")
print(f"Cpk Value    : {cpk:.2f}")
print(f"Status       : {'CAPABLE' if cpk >= 1.33 else 'fail'}")

# VISUALIZATION 
plt.figure(figsize=(12, 6))

# Plot Data Points
plt.plot(df['id'], df['value'], marker='o', linestyle='-', color='royalblue', label='Measurements', alpha=0.7)

# Plot Limits
plt.axhline(mean, color='green', linestyle='-', linewidth=2, label=f'Mean ({mean:.2f})')
plt.axhline(UCL, color='red', linestyle='--', linewidth=2, label='UCL (+3σ)')
plt.axhline(LCL, color='red', linestyle='--', linewidth=2, label='LCL (-3σ)')
plt.axhline(USL, color='black', linestyle=':', linewidth=1.5, label='USL (Spec)')
plt.axhline(LSL, color='black', linestyle=':', linewidth=1.5, label='LSL (Spec)')

# Highlight Outlier
outliers = df[(df['value'] > UCL) | (df['value'] < LCL)]
if not outliers.empty:
    plt.scatter(outliers['id'], outliers['value'], color='orange', s=100, zorder=5, label='Outlier')

# Labels and Title
plt.title(f"X-bar Control Chart (Cpk: {cpk:.2f})", fontsize=14)
plt.xlabel("Sample ID")
plt.ylabel("Measured Value (mm)")
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

# Show Plot
plt.tight_layout()
plt.show()
