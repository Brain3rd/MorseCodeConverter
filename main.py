MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', 'Ä': '.-',
                   'Ö': '---', 'Å': '---'}


def main():
    word_list = []
    morse_code_list = []
    while True:
        user_input = input("What message do you want to convert?")
        input_words = list(user_input.upper())
        for morse_code in input_words:
            if morse_code in MORSE_CODE_DICT:
                word_list.append(morse_code)
                morse_code_list.append(MORSE_CODE_DICT[morse_code])
            else:
                print(f"{morse_code} is invalid morse code character!")

        final_word = '  '.join(word_list)
        final_morse_code = '  '.join(morse_code_list)
        print(f"Your word: {user_input}")
        print(f"Valid letters from your word: {final_word}\nTranslated to the morse code: {final_morse_code}\n")
        if input("Do you want to translate another word into morse code? Type 'y' or 'n':").upper() == 'N':
            break
        else:
            word_list.clear()
            morse_code_list.clear()


if __name__ == '__main__':
    main()
