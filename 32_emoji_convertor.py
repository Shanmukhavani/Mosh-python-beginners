# press windows logo + ; for emojis in vscode
emojis = {
    ":)" : "😀",
    ":(" : "😞"

}
command = input ("> ")
word = command.split(" ")
output = ''
for i in word:
    output+=emojis.get(i,i)+" "
print(output)
