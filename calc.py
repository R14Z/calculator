# python calculator 

print('python calculator made by riaz')


choice = input('add,subtract,multiply or divide? ').lower()

if choice == 'add' or choice == '+' or choice == 'addition':
  add_first_num = float(input('Enter the first number you would like to add: '))
  add_second_num = float(input('Enter the second number you would like to add: '))
  add_num = add_first_num + add_second_num
  print(f'Answer = {add_num}')
elif choice == 'subtract' or choice == '-' or choice == 'sub' or choice == 'subtraction':
    sub_first_num = float(input('Enter the first number you would like to subtract: '))
    sub_second_num = float(input('Enter the second number you would like to subtract: '))
    sub_num = sub_first_num - sub_second_num
    print(f'Answer = {sub_num}')
elif choice == 'multiply' or choice == 'x' or choice == 'times' or choice == 'multiplication':
    mult_first_num = float(input('Enter the first number you would like to multiply: '))
    mult_second_num = float(input('Enter the second number you would like to multiply: '))
    mult_num = mult_first_num * mult_second_num
    print(f'Answer = {mult_num}')    
elif choice == 'divide' or choice == '÷' or choice == 'division':
    div_first_num = float(input('Enter the first number you would like to divide: '))
    div_second_num = float(input('Enter the second number you would like to divide: '))
    div_num = div_first_num / div_second_num
    print(f'Answer = {div_num}')   
else:
    print('Error') 