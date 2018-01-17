# Payroll

# Input
name = input("Enter name: ")
hour = float(input("Enter number of hours worked weekly: "))
pay = float(input("Enter hourly pay rate($): "))
cpf = float(input("Enter CPF contribution rate(%): "))

# main
gross = hour * pay
cpf_amt = gross * cpf / 100
rev = gross - cpf_amt

# Output
print("Payroll statement for '" + name + "'")
print("Number of hours worked in week: ",(hour))
print("Hourly pay rate: ",(pay))
print("Gross pay: ",(gross))
print("CPF contribution at 20%: ",(cpf_amt))
print("Net pay: ",(rev))