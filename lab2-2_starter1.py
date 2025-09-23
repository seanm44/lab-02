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

    with open(LOGFILE, "r") as f:
        for line in f:
            print (ip_parse(line.strip()))

unique_ips = set(ip_parse)

# Print each unique IP
print("Unique IPs:")
for ip in unique_ips:
    print(ip)
    