def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

def grep_lines(lines, needle):
    for line in lines:
        if needle in line:
            yield line

# Example usage:
matches = grep_lines(read_lines("big.log"), "ERROR")
for line in matches:
    print(line)
    if (line == "ERROR"):
        break
