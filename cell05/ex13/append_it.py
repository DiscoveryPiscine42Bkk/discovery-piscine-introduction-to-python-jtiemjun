import sys
def append_it():
    if len(sys.argv) == 1:
        print("none")
        return

    for arg in sys.argv[1:]:
        if not arg.endswith("ism"):
           print(f"{arg}ism")
if __name__ == "__main__":
    append_it()