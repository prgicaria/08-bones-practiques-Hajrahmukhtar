#!/usr/bin/env python
dividend = int(input("Escriu el dividend (nombre enter)"))
divisor = int(input("Escriu el divisor (nombre enter)"))

quocient = dividend // divisor
residu = dividend % divisor

print(f"La divisió és: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
