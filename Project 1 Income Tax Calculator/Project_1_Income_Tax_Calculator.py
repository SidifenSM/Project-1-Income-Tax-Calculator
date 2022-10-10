#Project 1 - Income Tax Calculator
#20% fixed tax rate
#$10,000 standard deduction
#Each dependent = additional $3000 deduction
#Neared penny, expressed as a decimal number


print ("Enter the gross income: ", end=' ')
grossinput = float(input())

print ("Enter the number of dependents : ", end=' ')
dependinput = int(input())

#dependents * 3000 + the standard deduction
dependinput = (dependinput * 3000) + 10000

#tax is 20%
tax = 20 * 0.01

incometax = (grossinput - dependinput) * tax

print("The income tax is $" f'{incometax:.1f}')

