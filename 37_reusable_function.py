#creating reusable function for emoji convertor 
# press windows logo + ; for emojis in vscode
def emoji_convertor(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😀",
        ":(" : "😞"

    }
    output = ""
    for i in words:
       output +=emojis.get(i,i)+" "
    return output
command = input ("> ")
print(emoji_convertor(command))

