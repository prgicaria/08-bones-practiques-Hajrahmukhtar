#!/usr/bin/env python
dividend = int(input("Escriu el dividend (nombre enter)"))
divisor = int(input("Escriu el divisor (nombre enter)"))

quocient = dividend // divisor
residu = dividend % divisor

print(f"divisió: {dividend}/{divisor}")
print(f"quocient: {quocient}")
print(f"residu: {residu}")
