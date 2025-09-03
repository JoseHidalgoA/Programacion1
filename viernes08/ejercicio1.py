def es_vocal(letra):
	return letra.lower() in 'aeiou'

def contar_subcadenas(cadena, modo):
	n = len(cadena)
	contador = 0
	for i in range(n):
		if modo == 'A' and es_vocal(cadena[i]):
			contador += n - i
		elif modo == 'B' and not es_vocal(cadena[i]):
			contador += n - i
	return contador

def main():
	cadena = input("Ingrese la cadena de partida: ")
	puntos_A = contar_subcadenas(cadena, 'A')
	puntos_B = contar_subcadenas(cadena, 'B')
	print(f"Puntaje A (vocales): {puntos_A}")
	print(f"Puntaje B (consonantes): {puntos_B}")
	if puntos_A > puntos_B:
		print("Gana el jugador A (vocales)")
	elif puntos_B > puntos_A:
		print("Gana el jugador B (consonantes)")
	else:
		print("Empate")

if __name__ == "__main__":
	main()
