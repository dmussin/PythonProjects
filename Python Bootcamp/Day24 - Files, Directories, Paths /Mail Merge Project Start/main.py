#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



#Return all lines in the file, as a str:
with open('/Users/t_daniyarm/PycharmProjects/pythonProject1/Day24 - Files, Directories, Paths /'
          'Mail Merge Project Start/Input/Letters/starting_letter.txt') as file:
    content = file.read()

#Return all lines in the file, as a list where each line is an item in the list object:
with open('Input/Names/invited_names.txt') as file:
    names_list = file.readlines()

strripped_list = []

for name in names_list:
    strip_name = name.strip()
    readylist = content.replace("[name]", strip_name)
    with open('/Users/t_daniyarm/PycharmProjects/pythonProject1/Day24 - Files, Directories, Paths'
              f' /Mail Merge Project Start/Output/ReadyToSend/letter_for_{strip_name}.txt', mode='w') as file:
        file.write(readylist)

