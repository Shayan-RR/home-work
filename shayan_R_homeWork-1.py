def show_options(options, level=0):
    
    if level >= len(options):
        return

    # Display the options for the current level.
    print("Options at level {}:".format(level + 1))
    for i in range(len(options[level])):
        print("{}. {}".format(i + 1, options[level][i]))

    # select an option.
    choice = int(input("Enter your choice: "))

    
    if 1 <= choice <= len(options[level]):
        show_options(options, level + 1)
    else:
        #error message.
        print("Invalid choice")


# Example usage:

options = [
    ["Option 1", "1.1", "1.2", "1.3", "1.4"],
    ["Option 2", "2.1", "2.2", "2.3", "2.4"],
    ["Option 3", "3.1", "3.2", "3.3", "3.4"],
    ["Option 4", "4.1", "4.2", "4.3", "4.4"],
]

show_options(options)
