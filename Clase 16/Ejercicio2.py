from datetime import datetime

def enter_int_number():
    for _ in range(3):
        try:
            value = int(input("Enter an integer number: "))
        except ValueError:
            print('Must be integer')
        else: return value

    with open('log.txt','a') as f:
        t = datetime.now()
        stamp = t.strftime('%d/%m/%Y %H:%M:%S')
        f.write(f'{stamp} Error: maximum attempts reached\n')
    raise ValueError('You\'ve reached the maximum attempts')

if __name__=='__main__':
    print(enter_int_number())


# %%
from datetime import datetime

def enter_int_number():
    max_attempt = 3
    with open('log.txt','a') as f:
        for i in range(max_attempt):
            try:
                value = int(input("Enter an integer number: "))
                
            except ValueError:
                if i == max_attempt-1:
                    msj = 'Error: maximum attempts reached'
                    raise ValueError(msj)
                else:
                    msj = f'Attempt {i+1}: Invalid Number'                    
            else: 
                msj = 'Access succeeded'
                return value

            finally:
                t = datetime.now()
                stamp = t.strftime('%d/%m/%Y %H:%M:%S')
                f.write(f'{stamp} {msj}\n')
                print(msj)

if __name__=='__main__':
    print(enter_int_number())
