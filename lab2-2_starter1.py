# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed

def ip_parse(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if "from" in line:
        ip = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = ip.index("from")    # Find the position of the token "port", our anchor
            ips = ip[anchor+1]          # the port value will be next token, anchor+1
            return ips.strip()             # strip any trailing punctuation
    # Convert to a set to remove duplicates
    
        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":
    unique_ips = set()   
    total = 0

    with open(LOGFILE, "r") as f:
        for line in f:
            total += 1
            ip = ip_parse(line.strip())
            if ip:
                unique_ips.add(ip)

print(f"Total lines read: "{total}")
print(f"Number of unique IPs: {len(unique_ips)}")
sorted_ips = sorted(unique_ips)[:10]  
print("First 10 unique IPs:")
for ip in sorted_ips:
        print(ip)

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

import time

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

with open ("sample_auth_small.log") as f:
    for line in f:
        

  
        

start = time.time()
# run counting
end = time.time()
print("Top 5 attackers IPS:")
print()
print("Elapsed:", end-start, "seconds")