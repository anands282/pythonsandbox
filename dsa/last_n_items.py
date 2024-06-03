from collections import deque

def search(lines, pattern, history =5):
    previous_lines = deque(maxlen=history)
    #creates a fixed length queue when new items are added
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

