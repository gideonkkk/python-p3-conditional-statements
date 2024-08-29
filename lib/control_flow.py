#!/usr/bin/env python3


def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
      return "Access granted"
    else:
      return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    else:
        if 40 <= temperature <= 65:
          return "It's a little chilly out there!"
        else:
           if temperature > 85:
              return "It's too dang hot out there!"
           else:
              return "It's perfect out there!"


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    else:
        if number % 3 == 0:
          return "Fizz"
        else:
            if number % 5 == 0:
              return "Buzz"
            else:
              return number

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    else:
        if operation == '-':
          return num1 - num2
        else:
          if operation == '*':
            return num1 * num2
          else:
            if operation == '/':
              return num1 / num2 if num2 != 0 else "Error: Division by zero!"
            else:
             print("Invalid operation!")
        return None
