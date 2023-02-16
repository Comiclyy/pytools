import translate

while True:
    # Prompt the user to enter the target language
    target_language = input("Enter the language you want to translate to (e.g. 'es' for Spanish), or 'exit' to quit: ")

    # Check if the user wants to exit
    if target_language.lower() == "exit":
        break

    # Create a Translator object with the target language
    translator = translate.Translator(to_lang=target_language)

    # Prompt the user to enter the text to translate
    input_text = input("Enter the text you want to translate: ")

    # Translate the text using the Translator object
    translation = translator.translate(input_text)

    # Print the translated text
    print(f"The translated text is: {translation}")
