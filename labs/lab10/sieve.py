# Sieve of Eratosthenes
import os
import sys

def print_dir_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}|-- {os.path.basename(root)}/" if root != startpath else f"{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}|-- {f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dir_tree.py [directory]")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    print("HELLO")
    print_dir_tree(directory)
    
def getprimes(n):

    L = list(range(n+1))
    p = 2

    while p**2 <= n:
        for m in range(p, n//p+1):
            L[m*p] = 0
        q = p + 1
        while (q <= n) and (L[q] == 0):
            q = q + 1
        if q <= n:
            p = q
        else:
            break

    return list(filter(lambda x: x > 0, L))
