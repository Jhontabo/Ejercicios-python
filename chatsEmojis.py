##😀 😃 😄 😁 😆  😂 🤣 😇   🙂 🙃
continuarChat=True

while continuarChat:
    text=input('>')
    if text=='salir':
        continuarChat=False
    text=text.replace(':)','😊')
    text=text.replace(':(','🙃')
    text=text.replace(':P','😉')
    text=text.replace(':p','😉')
    text=text.replace(':S','😅')
    text=text.replace(':s','😅')
    print(text)

