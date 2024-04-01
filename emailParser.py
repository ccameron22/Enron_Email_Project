
import os
import operator

#####
# Chase Cameron
# 4/1/24
#####

#########
# This is currently set to test a single folder called 'power' in the specified parent folder
# This test is a starting point. The code will be modified to search each folder in each parent folder
# The word bank contains 'start' as it is a known word in several emails in this test
#########

#####
# The Enron email corpus can be obtained here https://www.cs.cmu.edu/~enron/
# There are instructions in the repository for where to place this script after the corpus is unzipped
#####

# Set path to folder "EnronEmails\maildir\baughman-d"
maildir_path = r"Your Path"
# Create dictionary to hold file location and number of hits
ranking = {}
#sortedRank = {}

# Create list of search word and list of folder to skip
wordList = ["Death Star", "death star", "Death star", 'pump', "start"]

# This list will be used during the full run. It is not necessary during the test
#skipFolders = ["all_documents", "contacts", "calendar"]

def parseEmails():

    # Cycle through each folder/file
    for root, dirs, files in os.walk(maildir_path):
        # Check if the current folder is named "power"
        # This will be removed in the running version so all folders will be searched
        if os.path.basename(root) == "power":
            # Check each file in the matching folder
            for file in files:
                # Reset the path and then set it to the current file
                file_path = ""
                file_path = os.path.join(root, file)
                score = 0
                # Open the file, read in the data and convert it to lower case
                with open(file_path, 'r') as f:
                    contents = f.read()
                    contents = contents.lower()
                    # Check each word in the search list against the file contents
                    for word in wordList:
                        # For a match increment the score
                        if word in contents:
                            score += 1
                # If the score is positive add the file location and score to the dictionary
                if score > 0:
                    ranking[file_path] = score
            # If there are no files in the current folder, check for subfolders
            # This is currently set for the specific known example. It will be altered
            # to work with unknown layers
            for folder in dirs:
                # Set the folder path
                folder_path = os.path.join(root, folder)
                # Check each file in the folder
                for file in os.listdir(folder_path):
                    # Set the file path
                    file_path = os.path.join(root, folder)
                    file_path = os.path.join(file_path, file)
                    score = 0
                    # Read in the contents and convert to lower case
                    with open(file_path, 'r') as f:
                        contents = f.read()
                        contents = contents.lower()
                        # Check each word in search list
                        # On a match increment the score
                        for word in wordList:
                            if word in contents:
                                score += 1
                    # If the score is positive, add the location and score to the dictionary
                    if score > 0:
                        ranking[file_path] = score
    #sortedRank = sorted(ranking.items(), key=operator.itemgetter(1))

"""
    for topFolder in maildir:
        for folder in topFolder:
            if folder == "power":
                for subFolder in folder:
                    for file in subFolder:
                        score = 0
                        lines = fp.readlines()
                        for row in lines:
                            for word in wordList:
                                if row.find(word):
                                    score += 1
                        if score > 0:
                            temp = os.path.abspath(__file__)
                            ranking[temp] = score
"""


if __name__ == '__main__':
    parseEmails()
    for key, value in ranking.items():
        print("Location: ", key, ", Score: ", value)
    print("done")
