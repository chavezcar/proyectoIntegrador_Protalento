import keyboard

def main():
    print("Presiona la tecla ↑ (flecha arriba) para salir.")

    while True:
        # Lee la tecla presionada
        tecla = keyboard.read_event(suppress=True).name

        # Imprime la tecla
        print(f"Tecla presionada: {tecla}")

        # Verifica si la tecla de flecha arriba fue presionada para salir del bucle
        if tecla == "up":
            print("¡Tecla de flecha arriba presionada! Saliendo del programa.")
            break

if __name__ == "__main__":
    main()
