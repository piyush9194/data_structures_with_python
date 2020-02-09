def disemvowel(string):
   vowels = {'a','e','i','o','u'}
   string2 = ''
   for char in string:
       if char not in vowels:
           string2= string2+char
   return(string2)



print(disemvowel("My name is Piyush"))