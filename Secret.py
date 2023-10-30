def solution(s):
    # Convert the input string to lowercase
    s = s.lower()
    
    if s:
        # Split the string into a list of words
        s = s.split()
        print(s)
        
        # Reverse the list of words
        reversed = s[::-1]
        print("-----")
        print(reversed)
        
        # Reverse each word in the list
        reversed = [word[::-1] for word in reversed]
        
        # Join the reversed words back into a single string, separated by spaces
        reversed_string = ' '.join(reversed)
        
        # Capitalize the first letter of the resulting string
        reversed_string = reversed_string.capitalize()
        
        return reversed_string
    else:
        return "String can't be empty or contain uppercase letters"

s = "Hello Love"
result = solution(s)
print(result)
