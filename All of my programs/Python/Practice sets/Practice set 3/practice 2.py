letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
name_ = input("Enter your name : ")
print(letter.replace("<|Name|>",name_).replace("<|Date|>","7-11-24"))
