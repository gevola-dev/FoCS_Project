
import re

#  The file ex-data/numbers.txt contains 10000 lines. Each line contains either a number or a string, find how many even number are in the file.
print('\n', 'Exercise 1', '\n')

def count_even_numbers():
    even_count = 0
    pattern = re.compile("^\\d+$") # ^ start of the line; \d digit; + more occurrencies of the digit; $ the end of theline 

    with open('../dataframes/numbers.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):  # Check if the line is a number
                number = int(line)
                if number % 2 == 0:  # Check if the number is even
                    even_count += 1
    return even_count

print("Number of even numbers in the file:", count_even_numbers())


# The file ex-data/email.txt contains 80000 lines. Each line might begin with some whitespaces (>=0), is followed by an email address, a number (>0) of spaces, and an age. 
# Using REs and the concepts from previous lessons, find how many times each domain was used.
print('\n', 'Exercise 2', '\n')

def count_domains():
    
    domains = {}
    email_pattern = re.compile(r'\w+@\w+\.\w+')
    
    with open('../dataframes/email.txt', 'r') as file:
        for line in file:
            # Extract email using regex pattern
            match = email_pattern.search(line)
            if match:
                email = match.group()
                # Extract domain part of the email after '@'
                domain = email.split('@')[1]
                if domain in domains:
                    domains[domain] += 1
                else:
                    domains[domain] = 1

    return domains

output = count_domains()

for domain, count in output.items():
    print(domain, count)


# The file ex-data/exp_nums.txt contains 100 lines. Each line contains a number in E-notation. Convert each number to its decimal representation.
print('\n', 'Exercise 3', '\n')

def enotation_to_decimal():

    decimals = {}
    enotation_pattern = re.compile(r"\d+\.\d+e[-+]?\d+")

    with open('../dataframes/exp_nums.txt', 'r') as file:
        for line in file:
            line = line.strip()
            match = enotation_pattern.search(line)
            if match:
                # Convert the matched E-notation number to a decimal number
                enotation = match.group()
                decimal = float(enotation)
                decimals[decimal] = enotation
    
    return decimals

output = enotation_to_decimal()

for decimal, enotation in output.items():
    print(decimal, enotation)


# CamelCase and snake_case two different ways to name variables. Write a function (camel_to_snake) that converts a string in CamelCase to snake_case.
print('\n', 'Exercise 4', '\n')

def camel_to_snake(camelString):
    
    # Step 1: Find all places where a lowercase letter is followed by an uppercase letter
    # and insert an underscore between them. For example, "camelCase" becomes "camel_Case".
    intermediate_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camelString)
    
    snake_string = intermediate_str.lower()
    
    return snake_string

camelString = 'CamelCamelCamel'
print(camelString, camel_to_snake(camelString))
