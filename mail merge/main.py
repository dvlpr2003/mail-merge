with open("./input/names/name.txt" ,mode="r") as names:
  read_name = names.readlines()
with open("./output/mail-output/mail.txt",mode="r" ) as mail:
  mail_read = mail.read()
  for _ in read_name:
    replaced_name = mail_read.replace("[name]",_)
    with open(f"./output/final_output/{_}.txt",mode="w") as output_mail:
      final_output = output_mail.write(replaced_name)