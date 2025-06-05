#Email Addresses Extracter implementation in Python
print("Hello and Welcome to the Email Addresses Extracter") 
file_path=input("Please Enter the path of your text file ") #file_path input for input file
output_path=input("Please Enter the name of the text file you want to write the extracted emails to ")#file name input for output file
extracted_emails=[] #list to store the extracted emails from the input file
with open(file_path,"r") as file: #Opening the input file in reading mode
    file_content=file.read()  #Reading the input file and storing its content in file_content
    for word in file_content.split(): #Accessing each word by splitting by " " in the input file 
        clean_word=word.strip(".!?:;") #Stripping each word from the following punctuations
        if clean_word.endswith(("gmail.com","ac.in","outlook.com","rediffmail.com")) and clean_word not in extracted_emails: #Checking if the word is an email address and also checking whether it is already in extracted enails list to avoid repetition
            extracted_emails.append(clean_word) #Appending each word in the extracted emails list
with open(output_path+".txt","a") as file1: #Creating the output file with the file name entered by the user and opening it in append mode
    for email in extracted_emails: #Accessing each email in extracted emails list 
        file1.write(email+"\n") #Writing each email in a new line in the output file
        
