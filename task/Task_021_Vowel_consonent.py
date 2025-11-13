#Count vowels and consonants in a String


input_string = "Hello, World!"
#a,e,i,o,U
# vowel= e,o,o?
def count_vowels(input_string):
 vowels="aeiou"
 vowels_count= 0
 vowels_consonents = 0
 result= list()

 for char in input_string:
    if char in vowels:
        vowels_count= vowels_count + 1
        result.append(char)
    elif char not in vowels:
        if char !=" " and char!=","and char !="!" and char!=".":
         vowels_consonents = vowels_consonents + 1
        result.append(char)

 print(vowels_count)
 print(vowels_consonents)
print(count_vowels(input_string))