# This is a Python script to check if you are bro with someone

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import utils
import emoji


if __name__ == '__main__':

    print("|      Are We Bro?        |")
    print("--------------------------\n")

    my_name = input("Enter your name: ")
    friend_name = input("Enter your friend's name: ")

    check = input(f"Type 1 to check if you are bro with {friend_name}\n")
    if check == "1":
        if utils.are_we_bro(my_name, friend_name):
            handshake = emoji.emojize(":handshake:")
            print(f"{handshake} YES, YOU AND {friend_name.upper()} ARE BRO! {handshake}")
        else:
            beuark = emoji.emojize(":face_vomiting:")
            print(f"{beuark} No, you and {friend_name} are not BRO! {beuark}")
