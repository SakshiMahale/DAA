import os
import heapq
from collections import defaultdict, namedtuple

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_codes(node, prefix='', codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_compress(data):
    root = build_huffman_tree(data)
    huffman_codes = build_codes(root)
    compressed_data = ''.join(huffman_codes[char] for char in data)
    return compressed_data, huffman_codes

def get_file_size(file_path):
    """Returns the size of the file in bytes."""
    return os.path.getsize(file_path)

def calculate_compression_ratio(original_size, compressed_size):
    """Calculates the compression ratio."""
    if compressed_size == 0:
        return float('inf')  # Avoid division by zero
    return original_size / compressed_size

def main(file_path):
    # Read the original file
    with open(file_path, 'r') as file:
        original_data = file.read()

    # Get the original size
    original_size = get_file_size(file_path)

    # Compress the data
    compressed_data, huffman_codes = huffman_compress(original_data)

    # Calculate the compressed size in bits
    compressed_size = len(compressed_data) / 8  # Convert bits to bytes

    # Calculate the compression ratio
    compression_ratio = calculate_compression_ratio(original_size, compressed_size)

    # Print the results
    print(f"Original Size: {original_size} bytes")
    print(f"Compressed Size: {compressed_size:.2f} bytes")
    print(f"Compression Ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    file_path = "input.txt"  # Change to your actual file path
    main(file_path)