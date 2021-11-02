

![image-20211028234935213](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211028234935213.png)

Self dentro de um construtor é a referência que sabe onde encontra a localização do objeto criado em memória:

![image-20211028234953102](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211028234953102.png)

Como pode ser visto na imagem abaixo:

![image-20211028235035271](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211028235035271.png)

Caso não se deseje repetir código podemos utilizar um valor default que seria passado todas as vezes na criação dos registros de atributos de objetos. No exemplo abaixo foi fixo como default o valor de limite de 1000.0:

![image-20211029000117369](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029000117369.png)



Utilizando UML para representar o sistemas em diagramas de classes:

![image-20211029000349725](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029000349725.png)



Com orientação a objeto posso acessar uma referência da seguinte maneira:

[referência].[nome do atritibuto] 

conta.saldo

![image-20211029000845264](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029000845264.png)

Os atributos são os que o objeto tem e os métodos são aquilo que o objeto sabe fazer.

Mostrando como ficaria a UML da nossa classe, com atributos e métodos:

![image-20211029005808849](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029005808849.png)

None e Coletor de lixo:

Se você cria dois objetos com o mesmo nome, o primeiro fica perdido e você não tem mais acesso a ele. Ele vira simplesmente lixo:

![image-20211029010211994](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029010211994.png)

![image-20211029010236633](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029010236633.png)

![image-20211029010339809](C:\Users\jeffe\AppData\Roaming\Typora\typora-user-images\image-20211029010339809.png)



Para retirar a referência feita basta fazer o comando None: 

outraRef = None.

