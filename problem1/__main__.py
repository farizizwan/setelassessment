import sys
import csv

def converttoupper(strInput):
    result = strInput.upper()
    return result

def alternate(strInput):
    result = ""
    for (i,v) in enumerate(strInput):
        if i == 0 or i%2==0:
            result += v.upper()
        else:
            result += v.lower()
    return result

def main():
    strInput = input("Sample input:")
    resutl = converttoupper(strInput)
    print(resutl)
    result2 = alternate(strInput)
    print(result2)

if __name__ == '__main__':
    main()