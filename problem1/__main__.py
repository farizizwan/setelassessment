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

def createcsv(strInput):
    with open('problem1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        temarr = []
        for c in strInput:
            temarr.append(c)
        writer.writerow(temarr)
    return "CSV Created!"

def main():
    strInput = input("Sample input:")
    resutl = converttoupper(strInput)
    print(resutl)
    result2 = alternate(strInput)
    print(result2)
    result3 = createcsv(strInput)
    print(result3)

if __name__ == '__main__':
    main()