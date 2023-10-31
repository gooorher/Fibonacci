#Hacemos un test de fibonacci.py
import time
from fibonacci import fibonacci_recursive_with_memory as fib

start = time.time()


def test_fibonacci():
    assert fib(174)==1033628323428189498226463595560281832
    
test_fibonacci()

end = time.time()

print(start)
print(end)
print("Ha tardado:", end-start, "segundos")
print("OK!")


#Para ejecutar el test, desde la terminal, en el directorio donde se encuentra el archivo test.py, ejecutamos: