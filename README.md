# Segmentacion-clientes

1) Hacer lo del codo, lo de la silueta (lo que se ve de lao xd) y eso
2) Ver el cluster, y si no sale bien tener un PCA preparado (PCA es un analisis estadistico, con los autovectores para ver si las variables son importantes) --> Solo para variables numericas (no vale convertirlas con un encoder)
3) No lo pille pero vamos con esto vamos bomba


Meterse dentro de los clusters y ver que varables son las wenas

Una vez tenemos el cluster hecho (sabemos que van a ser 5 por ejemplo)
Sacar nuestras propias metricas --> + imp --> Index (variable y con respecto la media del cluster)
					      Otro index (valor de mi variabel y con respecto mi base de datos)
					      Si salen > 1 son muy importantes y si salen < 1 no son tan importantes
Una vez tenemos los index sacamos los perfiles, para poder hacerles una oferta para venderles algo


Cosa que tenemos que hacer fijo:
- Analizar lo que hay dentro de cada cluster (Si hay personas de 25 años, si su poder adquisitivo es alto, etc.)
- Entonces hacemos un Index para sacar los perfiles --> Index(c) = I(i) / I(cluster) imaginar que sale 1.5 (variable muy significativa)
	* Puede ser un index de un cluster o puede ser un Index total con respecto a la media de la base de datos --> Index(t) = I(i) / I(db)


Empezamos con un aprendizaje no supervisado, Sacamos las variables importantes y hacemos una evaluacion (ley del codo y silueta), y ver cuantos clusters nos salen como solucion (ej. 8)

Pero esto no es una solucion optimizada, es una ataque directo

Segunda opcion, una vez tengo los 8 clusters, me voy a negocio y veo las variables + representativas (no hace falta mirarlas todas)
--> Hay un truquito para ver las variables + represent. --> Hacer un arbol por cada cluster que hicimos antes, y ver las variables + imp de cada cluster, y explicarlas a negocio.

Una vez tenemos las var + imp hacer un Feature Engineering --> Y hacer otro kmeans, que normalmente tendra menos clusters que los primeros clusters inicialemente (porque hemos toqueteado los datos), y ahora salen por ejemplo 5.

Y a partir de ahi hacer un analisis mucho mas detallado (calcular los indices, analizar tendencias, etc.)

Una vez esto ya tenemos la parte de diseño, pero falta la parte de produccion ---|
																				 |
Un cluster es constante en el tiempo si esta bien hecho, no hace falta estar haciendolo constantemente, se hace cada cierto tiempo --> Por eso es muy importante la silueta y la evaluacion           |
																				 |
																				 |
																				 |
Como se pone en produccion? Pos mu fasi   <--------------------------------------|

Tengo mi CRM y hago una extracción obteniendo una base de datos, y esa tabla cada 2 o 3 meses la paso a entrenamiento y calculo el kmeans, que nos da un algoritmo con una serie de reglas en un arbol (chico alto, ojos azules, guapete --> pibon) que nos clasifican a los clientes en base a sus caracteristicas

Y el algoritmo se lo aplico a la persona, aplicandole unas rules y me dan un cluster, y lo devolvemos al CRM

El kmeans tiene un grado de confianza, lo veremos + adelante en el caso practico