import os

log_file_path = os.path.join('..', 'logs', 'system_logs.txt')
suspicious_log_path = os.path.join('..', 'logs', 'suspicious_logs.txt')

suspicious_keywords = ["Failed password", "Invalid user", "authentication failure", "Connection closed"]

with open(log_file_path, 'r') as file:
    lines = file.readlines()

suspicious_entries = []

for line in lines:
    if any(keyword in line for keyword in suspicious_keywords):
        suspicious_entries.append(line.strip())

print("🔍 Checking log file for suspicious activity...\n")

if suspicious_entries:
    print(f"⚠️ {len(suspicious_entries)} suspicious entries found:")
    for entry in suspicious_entries:
        print(f"  🔸 {entry}")

    with open(suspicious_log_path, 'w') as suspicious_file:
        for entry in suspicious_entries:
            suspicious_file.write(entry + '\n')

    print(f"\n📁 Suspicious logs saved to '{suspicious_log_path}'")
else:
    print("✅ No threats detected. All looks good!")
