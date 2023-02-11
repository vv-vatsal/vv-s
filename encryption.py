

charures = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Taking input for text from user.
text = input("Enter your text here : ")

'''Taking input for key from user.
key = int(input("Enter the key here : "))
'''

#As a static key.
key = 5

encrypred = []
#Encrypting
length_text = len(text)
for i in range(len(charures)):
    for j in range(len(text)):
        if text[j] == charures[i]:
            if (i + key)<26:
                encrypred_ch =  charures[i+key] 
                encrypred.append(encrypred_ch)
            else:
                encrypred_ch =  charures[i+key-26] 
                encrypred.append(encrypred_ch)

                
print("Encrypted text : ",end="")
for i in range(len(encrypred)):
    print(encrypred[i],end="")
