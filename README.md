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