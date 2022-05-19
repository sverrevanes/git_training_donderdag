ABC = "abcdefghijklmnopqrstuvwxyz"


def shift_letter(letter, shift):
    abc = ABC[:]
    if letter in abc:
        need_to_make_upper = False
        if letter.isupper():
            need_to_make_upper = True
        original_index = abc.index(letter.lower())
        new_index = (original_index + shift) % 26
        new_letter = abc[new_index]
        if need_to_make_upper:
            new_letter = new_letter.upper()
    else:
        new_letter = letter
    return new_letter


def decrypt_message(shift, message):
    """
    Needs some implementation
    """
    return message


if __name__ == "__main__":
    git_encrypted_message = 'Gpa aopz, npa aoha, qbza npa pa vcly dpao wslhzl!'

    """
    the 'input' python function makes it possible to interact with the user. Try using it to ask for someone's 
    name. 
    """
    message_1 = f"Git says: hi {name}, can you decrypt my message?"

    print(message_1)
    print(git_encrypted_message)

    shift = input(f"Please, {name}, give decryption shift key (integer number please): ")
    if type(shift_back) != int:
        raise Exception("input value not supported!")
    decrypted_message = decrypt_message(shift=shift, message=git_encrypted_message)
    print(f"Nice try {name}, this is your decrypted message:")
    print(decrypted_message)










