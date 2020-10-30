# MCOC2020-Proyecto-3
Informe Verificar código 1-D:
El siguiente informe tiene como finalidad presentar los resultados obtenidos al verificar el código 1-D. 
Los pasos para obtener la discretización de la condición de borde natural en el extremo izquierdo del dominio son:

du(t,0)/dx = 5
=>(u(t,1) - u(t,0))/dx = 5  / *dx
=> -u(t,0) = 5dx - u(t,1)  / *(-1)
=> u(t,0) = -5dx + u(t,1)

¿Convergió la solución?

¿En qué casos cree ud. que se puede aplicar una condición de borde natural del tipo estudiado hasta ahora?

Los casos en que se puede aplicar una condición de borde natural del tipo estudiado serían los casos definidos en la memoria como del cuarto tipo, es decir, los que tienen contacto directo entre superficies de dos sólidos diferentes. A pesar de que este no sea el tipo que mejor representa la transferencia entre la superficie del hormigón y el medio contiguo.
![deltat1](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2020-Proyecto-3/main/x%3D0.104%20delta%20tiempo.png)
![deltat2](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2020-Proyecto-3/main/x%3D0.208%20delta%20tiempo.png)
![deltat3](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2020-Proyecto-3/main/x%3D0.416%20delta%20tiempo.png)
Figura 1: Evolución térmica en diferentes Delta t.
![deltamalla1](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2020-Proyecto-3/main/x%3D0.104%20malla.png)
![deltamalla2](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2020-Proyecto-3/main/x%3D0.208%20malla.png)
![deltamalla3](https://raw.githubusercontent.com/IgnacioInostroza/MCOC2020-Proyecto-3/main/x%3D0.416%20malla.png)
Figura 2: Evolución térmica en diferentes mallas.
