import os
from email.parser import Parser
rootdir = "D:/webinfo/exp1/dataset/maildir/lay-k/family"


def email_analyse(inputfile, subject_email_list,MID_email_list, email_body):
    with open(inputfile, "r") as f:
        data = f.read()

    email = Parser().parsestr(data)

    subject_email_list.append(email['subject'])
    MID_email_list.append(email['Message-ID'])
    email_body.append(email.get_payload())

subject_email_list = []
MID_email_list = []
email_body = []

for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        email_analyse(os.path.join(directory, filename), subject_email_list, MID_email_list, email_body )

with open("subject_email_list.txt", "w") as f:
    for subject_email in subject_email_list:
        if subject_email:
            f.write(subject_email)
            f.write("\n")

with open("MID_email_list.txt", "w") as f:
    for MID_email in MID_email_list:
        if MID_email:
            f.write(MID_email)
            f.write("\n")

with open("email_body.txt", "w") as f:
    for email_bod in email_body:
        if email_bod:
            f.write(email_bod)
            f.write("\n")