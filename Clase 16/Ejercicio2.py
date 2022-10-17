def main():
    while True:
        pot = input('Ingrese un valor de potencia a transformar en dB: ')
        try:    
            decib = db2(float(pot))
        except (ValueError, TypeError, KeyboardInterrupt)  as e:
            print(f'Error: {e}')
        except:
            print('No se puede realizar la operacion')
        else:
            print(f'{pot} watts son {decib} dB')
            break

def main2():
    while True:
        pot = input('Ingrese un valor de potencia a transformar en dB: ')
        try:    
            decib = db(pot) # uso mal la funcion
        except (AssertionError, KeyboardInterrupt) as e:
            print(f'Error: {e}')
        except:
            print('No se puede realizar la operacion')
        else:
            print(f'{pot} watts son {decib} dB')
            break
    
if __name__ == "__main__":
    main()
