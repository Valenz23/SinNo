# Hito 5: Diseño y test de un microservicio.


 
## Índice
    Valoración:

    2 puntos: Justificación técnica del framework elegido para el microservicio.
    2 puntos: Diseño en general del API, las rutas (o tareas), tests y documentación de todo, justificando como se ajustan a las historias de usuario, de forma que reflejen correctamente un diseño por capas que desacopla la lógica de negocio del API.
    2 puntos: uso de logs, incluyendo justificación del framework y herramienta elegida.
    2 puntos: tests correctos y de acuerdo con las historias de usuario.


    Entrega:
    
    Debe incluir, al menos, un servicio de configuración que considere las diferentes posibilidades.
    Debe tener la estructura general de las clases que se vayan a servir con el API correcta, incluyendo en su caso diseño de excepciones que puedan ocurrir en el curso normal de ejecución de la aplicación.
    No deben incluir ningún tipo de acceso a datos, pero si lo hacen debe hacerse a través de una single source of truth usando inyección de dependencias. El test de la misma se debe hacer de la misma forma.
    No es necesario, ni se solicita, que haya una "aplicación" lanzable y se prefiere que no la haya. El código debe ser única y exclusivametne el necesario para testear las rutas, y es conveniente que, en el diseño por capas, se separe la lógica de negocio de la lógica del API y esta, a su vez, del programa o aplicación desde las que se van a usar ambos.
    En este punto la aplicación puede estar potencialmente en Internet. La comprobación de tipos debe ser exhaustiva, tanto la que provea el sistema de tipos del lenguaje como la que se haga por parte del usuario en caso de que no sea así.
    Si no se incluye un test de prestaciones, al menos se debe de tener en cuenta que un hito posterior puede incluirlo, por lo que el diseño se tendrá que haber hecho teniendo en cuenta esta posibilidad.



[Ir a inicio](../../README.md)
