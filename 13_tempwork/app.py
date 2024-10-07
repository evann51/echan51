#Leon Huang, Evan Chan, Ethan Sie
#The Grizzly Bears
#SoftDev
#K13 - Combine
#2024-9-30
#Time Spent: 2

from flask import Flask, render_template
import random
import csv

################################# Code from Dancing Elmos!

def fileParser(file): #reads csv
    with open(file, newline='') as csvfile:
        csvFile = csv.reader(csvfile, delimiter='\n')
        data = []
        for line in csvFile:
            data.append(line) # Puts all of the data from the csv into the list
    return data

def splitHeaders(dataSet):  # Converts data to dictionary
    combined_data = []  # List to hold the combined data
    for data in dataSet:
        for string in data:
            for count, letter in enumerate(string[:len(string)-1]):
                if letter == ',' and string[count + 1].isnumeric():
                    job_title = string[:count]
                    percentage = float(string[count + 1:].split(",", 1)[0])
                    link = string[count + 1:].split(",", 1)[1]
                    # Append a dictionary to combined_data
                    combined_data.append({
                        'job': job_title,
                        'percentage': percentage,
                        'link': link
                    })
    return combined_data  # Return the combined data


def randomizeJob(combined_data):  # Randomizes job based on the combined data
    total_weight = sum(item['percentage'] for item in combined_data)  # Calculate total weight
    randVal = random.uniform(0, total_weight)  # Random value in the range of total weights
    for item in combined_data:
        randVal -= item['percentage']  # Decrease by each item's percentage
        if randVal <= 0:  # When the random value is less than or equal to 0, return the job
            return item['job']  # Return the job title


###################################################

app = Flask(__name__)           #create instance of class Flask

CSV_FILE_PATH = 'data/occupations.csv'

@app.route("/")
def showHome():
    return "Welcome to the abyss"

@app.route("/wdywtbwygp")
def showT():
    jobData = fileParser(CSV_FILE_PATH)  # Parses csv data
    headers = jobData[0][0].split(',')  # Initial delimit
    numJobData = jobData[1:len(jobData) - 1]  # Cuts out the header and "Total"
    combined = splitHeaders(numJobData)  # Converts into dictionary
   # randJob = randomizeJob(listValues[0])  # Finds random job
    team = ["Ethan Sie", "Evan Chan", "Leon Huang"]
    # Pass job names, percentages, and links to the template
    return render_template('tablified.html', 
                           teamMembers=team, 
                           foo="Grow up", 
                           teamname="The Grizzly Bears", 
                           combined_data=combined,
                           job = randomizeJob(combined))
    


if __name__ == "__main__":
    app.debug = True
    app.run()
