def get_line(x0, y0, x1, y1):
    points = []# lista para almacenar puntos generados
    
    # 1er paso: dx, dy, obtendremos el valore absoluto
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # variables para iterar xk, yk
    if x0 < x1:
        x_step = 1
    else:
        x_step = -1

    if y0 < y1:
        y_step = 1
    else:
        y_step = -1

    # 2do paso: parametro de decision Pk
    Pk = dx - dy

    # 3er paso: iterar hasta el punto final, 
    # hay que tomar en consideracion si estamos avanzado/retorcediendo, subiendo/bajando
    while (x0 != x1) or (y0 != y1):

        #Agregamos el punto 
        points.append((x0, y0))
        Pk2 = 2 * Pk #lo hacemos para evitar trabajar con fracciones y mejorar la resistencia a errores

        #realizamos el ajuste 
        if Pk2 > -dy:
            Pk -= dy
            x0 += x_step 

        if Pk2 < dx:
            Pk += dx
            y0 += y_step 

    points.append((x0, y0))
    return points

def poligono(puntos):
    resultados = []
    max_index = len(puntos) - 1 
    for i in range(0, max_index):
        print(i)
        resultados.append(get_line(puntos[i][0], puntos[i][1], puntos[i+1][0], puntos[i+1][1]))

    resultados.append(get_line(puntos[max_index][0], puntos[max_index][1], puntos[0][0], puntos[0][1]))
    return resultados




if __name__ == "__main__":

    print(poligono([(15, 15), (30, 30), (15, 45)]))

