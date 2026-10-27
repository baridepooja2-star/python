#Write a program to print numbers from 1 to 20 but skip the number 10
for i in range(1, 21):
    if i == 10:
        continue
    print(i)