import threading
def calc_square(number):
    print('Square', number**2)

def calc_quad(number):
    print('Quad', number**4)

if __name__ == "__main__":
    number = 7
    result = None
    thread1 = threading.Thread(target=calc_square, args=(number,))
    thread2 = threading.Thread(target=calc_quad, args=(number,))

    #Ejecutar en paralelo
    thread1.start()
    thread2.start()

    #Une los hilos al proceso padre
    thread1.join()
    thread2.join()