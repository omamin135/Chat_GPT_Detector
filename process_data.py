import pandas as pd
import os

'''
process raw text input into formatted structure for use in nural network
'''

#input text file to get the text from
inputFile = "text.txt"

# output excel file
excelFile = "Data.xlsx"

#clean inputed line string by removeing any punctuation or unneeded characters
def cleanLine(line):
    clean = line.replace(',', '')

    return clean

with open(inputFile, 'r') as inFile:

    textArray = []
    for line in inFile:
        
        #remove punctuation and extraneous chars from line
        clean = cleanLine(line)

        #spead the line split at every '.' into the array
        senArr = [sentence.strip() for sentence in clean.split(".")]
        
        #move all non-blank entires from sentence array into main data array
        for sen in senArr:
            if (sen != ''):
                textArray.append(sen)

#export the sentence data to excel spreadsheet
marks_data = pd.DataFrame({"sentences":textArray})
marks_data.to_excel(excelFile)

os.startfile(excelFile) 