import random

messages_list = [
    "You're doing great!",
    "Sometimes life just feels hard, it doesn't mean that you're doing anything wrong.",
    "Everything happens at the right time, trust the process.",
    "Comparing ourselves to others robs us of joy."
]


def get_random_number():
    random_number = random.randint(0, 1000000000000000000000)
    return random_number


def get_image_by(number):
    number = number % len(messages_list)
    return messages_list[number]


def peek_at_file():
    with open('helpMe.txt') as f:
        line = f.readline()
        if line == "help":
            return True


def write_file(help_message):
    with open("helpMe.txt", "w") as f:
        f.write(help_message)


def main():

    while True:
        if peek_at_file():
            print("Retrieving a helpful message for the user...")
            random = int(get_random_number())
            msg = get_image_by(random)
            write_file(msg)
            print("Message sent!")


if __name__ == "__main__":

    main()
