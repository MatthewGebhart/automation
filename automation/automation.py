import re

# context manager
with open("../assets/potential-contacts.txt", "r") as f:
    # we logic and stuff with the file f
    text_from_file = f.read()

# print(text_from_file)

# Same pattern as before:
phone_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
phone_pattern2 = r"^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
email_pattern = r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

# re.findall() returns a list of matches
phone_nums = re.findall(phone_pattern, text_from_file)
email_adds = re.findall(email_pattern, text_from_file)

# then remove duplicates and sort the list in ascending order
phone_nums_no_dups = sorted(list(dict.fromkeys(phone_nums)))
email_adds_no_dups = sorted(list(dict.fromkeys(email_adds)))

# seperate each item on a new line
phone_nums_to_print = '\n'.join(phone_nums_no_dups)
email_adds_to_print = '\n'.join(email_adds_no_dups)
# print(phone_nums_to_print)

# write to new files
with open('../assets/phone_numbers.txt', 'w') as new_file:
    new_file.write(phone_nums_to_print)

with open('../assets/emails.txt', 'w') as new_file:
    new_file.write(email_adds_to_print)



# print(phone_nums_no_dups)
# print(f" there are {len(phone_nums_no_dups)} unique phone numbers")
#
# print(email_adds_no_dups)
# print(f" there are {len(email_adds_no_dups)} unique email addresses")




