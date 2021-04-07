import sys
import argparse
import os

def main():
    print("Please Enter Contest Round Name:")
    x = input()
    cmd1 = "xcopy tmp \"{0}\" /E /H /C /I".format(x)
    os.system(cmd1)

if __name__ == "__main__":
    main()