print("To end this app enter: .")

def main():
    print("Приввет, нигга")
    print("Для твича осудим на всякий нигера")
    print("Для твича осудим на всякий не ниггера")
    while True:
         symbol = input("Operation sing (+, -, *, /): ")
         if symbol == '.':
             break
         if symbol in ('+', '-', '*', '/'):
             a = float(input("First number: "))
             b = float(input("Second number: "))
             if symbol == '+':
                 print(a+b)
             elif symbol == '-':
                 print(a-b)
             elif symbol == '*':
                 print(a*b)
             elif symbol == '/':
                 if b != 0:
                     print(a/b)
                 else:
                     print("Please, don't divide by zero to avoid the collapse of Universe!")
         else:
             print("Hey, write a supported sign!")