import os
import fileinput

path = "D:\Workplace\INS_567.adoc"

mada = "== New Year 234Round"
with open(path) as f:
    string = f.readline().strip()
    
with fileinput.FileInput(path, inplace=True) as file:
    for line in file:
        print(line.replace(string, mada), end='')
