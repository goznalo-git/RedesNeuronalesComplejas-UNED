# Códigos y simulaciones de la asignatura "Redes Neuronales y Complejas" de la UNED

En este repositorio se encuentran los códigos empleados para la realización de las simulaciones requeridas en los problemas de la asignatura. Las explicaciones, modelos teóricos, etc se encontrarán principalmente en el documento final a entregar. Aquí simplemente están los códigos, y alguna que otra breve explicación/comentario/descripción de por qué cada cosa.

Todas ellas las he llevado a cabo con Python (versión 3.5 mínimo) y Jupyter Notebooks. Paso ahora a concretar más los componentes de cada una. 


## Problema 2: Simulación del modelo Leaky Integrate-and-Fire

En este modelo necesitamos resolver una ecuación diferencial, junto con una condición a evaluar tras cada iteración hacia adelante en el tiempo. Para ello, he programado el método de Runge-Kutta de cuarto orden que calcula únicamente un paso hacia adelante (función _RK4_). Metiendo esto en un bucle, podemos ir avanzando en el tiempo, comprobando si pasamos o no el umbral, en cuyo caso reiniciamos al valor de reposo (función _solve___system_)

Para una elección de parámetros basada en la literatura, obtenemos gráficas de Intensidad frente a tiempo y Voltaje frente a tiempo.

Las funciones en sí se encuentran en el archivo _LIF.py_, pero el ejecutable de Python es realmente _LeakyIntegrate-and-Fire.py_, que las va llamando en orden y luego pinta las gráficas.

Hay un notebook de Jupyter con el mismo nombre (_LeakyIntegrate-and-Fire.ipynb_) que fue el que usé para ir diseñando y testeando las funciones, y tiene alguna que otra aclaración.


## Problema 4: Simulación de redes asociativas de Hopfield para un patrón


