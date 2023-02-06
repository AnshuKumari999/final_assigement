# get the occurence of all vowels and consonent from the large given string.

vowel_count = 0;  
consonent_count = 0;  
str = "Counting The Vowels And Consonent";  
   
#converting the string to lower case to reduce the comparisons. 
str = str.lower();  
for i in range(0,len(str)):   
    #Checking whether a character is a vowel  
    if str[i] in ('a',"e","i","o","u"):  
        vowel_count = vowel_count + 1 
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        consonent_count = consonent_count + 1
print("Total number of vowel and consonant are" ) 
print("Vowel Occuerence is : " , vowel_count) 
print("Consonent Occuerence is : " , consonent_count)

