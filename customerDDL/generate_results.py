import random

i = 5
firstnames = []
lastnames = []
emails = []
address = []
for line in open("names.txt", "r"):
    firstname, lastname = line.split()
    firstnames.append(firstname)
    lastnames.append(lastname)
for line in open("address.txt", "r"):
    address.append(line)
for line in open("email.txt", "r"):
    emails.append(line)

for i in range(100):
    print(
        "insert into customer values ('{:03d}', '{} {}', '{}', '{}');".format(
            i,
            random.sample(firstnames, 1)[0],
            random.sample(lastnames, 1)[0],
            random.sample(address, 1)[0],
            random.sample(emails, 1)[0],
        )
    )
