#lab 8-2
import sys 
import lab06_6 as countVowels


def CountVowelIsInFile(fname):
    vowels = 0
    fileObj = open(fname)
    try:
        for line in fileObj:
            vowels += countVowels.CountVowels(line)   
    finally:
        fileObj.close()
    return vowels


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = input("file name:")
    if not fname:
        fname = "cats.txt"
    try:
        print("There are %d vowels in the %s."
              %(CountVowelIsInFile(fname),fname))
    except IOError:
        sys.stderr.write (info)
        sys.exit(1)
        
                                                 

if __name__ == "__main__":
    main()
        
    

