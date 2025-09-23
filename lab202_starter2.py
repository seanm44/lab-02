import time

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

with open ("sample_auth_small.log") as f:
    for line in f:
        





start = time.time()
# run counting
end = time.time()
print("Elapsed:", end-start, "seconds")