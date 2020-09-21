import pill
print("Right now only the lexer, parser and the interpreter are implemented. Try typing in 1 + 2 "
      "or any arithmetic condition to see them work. \n"
      "Write 'exit' or 'quit' to exit pill. ")

while True:
    text = input('pill > ')
    if text == "exit" or text == "quit":
        print("Goodbye")
        break

    result, error = pill.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)