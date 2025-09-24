def emoji(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return (text)

text = input ("what are your thoughts? ")
text = emoji(text)
print(text)