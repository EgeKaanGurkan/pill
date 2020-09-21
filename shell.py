import pill
print("Write 'exit' or 'quit' to exit pill")

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