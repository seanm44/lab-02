import re

with open("auth.log" , "r") as f:
    for line in f:
        print(line)

ips = [] 
pattern = r"\d+\.\d+\.\d+\.\d+"
found_ips = re.findall(pattern, line)
for ip in found_ips:
        ips.append(ip)

unique_ips = set(ips)
print("Unique IPs:")
for ip in unique_ips:
    print(ip)