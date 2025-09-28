# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parse(line):
    """
    looks for the substring ' from ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        ip = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = ip.index("from")    # Find the position of the token "port", our anchor
            ips = ip[anchor+1]          # the port value will be next token, anchor+1
            return ips.strip()             # strip any trailing punctuation
    # Convert to a set to remove duplicates
    
        except (ValueError, IndexError):
            return None

    return None

count = 0
with open ("sample_auth_small.log", "r") as f:
    for line in f:
        count += 1
print("Lines read:", count)

# Convert to a set to remove duplicates
unique_ips = set()
count_uni = 0
firstTen = 0

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":
    with open(LOGFILE, "r") as f:
        for line in f:
            ip = ip_parse(line.strip())
            if ip:
                unique_ips.add(ip)

for ip in unique_ips:
    count_uni += 1

print("Unique IPs:", count_uni)

print("First 10 IPS:")    
for ip in unique_ips:
    if firstTen < 10:
        print(ip)
        firstTen += 1
            
from collections import defaultdict

counts = defaultdict(int)           # Create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
print(counts)

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

import time
start = time.time()
# run counting
end = time.time()
print("Elapsed:", end-start, "seconds")