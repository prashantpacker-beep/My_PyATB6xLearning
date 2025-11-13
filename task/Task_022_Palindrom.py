# # ✅Palidrome of String
#
# 🧩 Example Walkthrough
# Let’s take the word "level":
# Forward: "level"
# Backward: "level"
# Both are identical → Palindrome ✅
# Now, "hello":
# Forward: "hello"
# Backward: "olleh"
# Not the same → Not a palindrome ❌

string= "Level"

def palindrome_char(char):
    char = char.lower()
    if char == char[::-1]:
        return True
    else:
        return False
print(palindrome_char(string))