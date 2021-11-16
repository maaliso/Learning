number = input ("Please write your phone number below!")
while not number.isnumeric():
    print ("Please enter only numbers!")
    number = input ("Please enter your phone number!")
Translator= {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
Output = ""
i = ""
for i in number:
    Output += Translator["i"]
print (Output)