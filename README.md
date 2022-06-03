# Códigos y simulaciones de la asignatura "Redes Neuronales y Complejas" de la UNED

En este repositorio se encuentran los códigos empleados para la realización de las simulaciones requeridas en los problemas de la asignatura. Las explicaciones, modelos teóricos, etc se encontrarán principalmente en el documento final a entregar. Aquí simplemente están dichos códigos, y alguna que otra breve explicación/comentario/descripción.

Todas ellas las he llevado a cabo con Python (versión 3.5 mínimo) y Jupyter Notebooks. Paso ahora a concretar más los componentes de cada una. 


## Problema 2: Simulación del modelo Leaky Integrate-and-Fire

Carpeta LeakyIntegrateFire. Consiste en 9 archivos:
- LeakyIntegrate-and-Fire.ipynb: hoja de Jupyter donde fui diseñando y testeando las funciones.
- LIF.py: script que contiene las funciones para que las importe el script principal.
- LeakyIntegrate-and-Fire.py: script principal, ejecutable, que genera las gráficas con los resultados.
- El resto son 6 figuras en formato PNG, resultado del código.

## Problema 4: Simulación de redes asociativas de Hopfield para un patrón

Carpeta HopfieldHebb. Consiste en dos archivos:
- Hopfield-Hebb.ipynb: hoja de Jupyter donde fui diseñando y escribiendo los resultados. Este problema es más una exposición de resultados que una simulación que ejecutar una y otra vez, por tanto no vi necesario generar un archivo ejecutable .py, los resultados son el mismo notebook. En cualquier caso, he exportado el notebook a formato HTML, visible en cualquier navegador, para facilidad de acceso.
- Hopfield-Hebb.html: notebook exportado para abrir en navegador.


## Problemas 7B y 8: Entrenamiento de una red neuronal con un dataset real y análisis crítico de la velocidad de aprendizaje

Carpeta Mushroom-NeuralNet. Consiste en varios archivos y carpetas:
- README.md: breve descripción del dataset y sus campos.
- 4 notebooks .ipynb: cada uno con uno de los pasos en el proceso de análisis de los datos, preprocesado y entrenamiento de la red neuronal (problema 7b), y uno último que es una versión modificada del de entrenamiento, con el código para el entrenamiento manual y figuras de los gradientes por capa y epoch.
- 4 archivos .html: exportados de los notebooks para abrir en navegador.
- Data/: carpeta conteniendo el dataset en formato .csv, una explicación de cada atributo en attributes.txt, y los archivos intermedios resultado del preprocesado. 
- Figures/: carpeta con las figuras obtenidas a lo largo de los notebooks.



## Problema 9: Análisis de una red compleja real

Carpeta ComplexNetwork. Consiste en varios archivos y carpetas:
- ComplexNetworkAnalysis.ipynb: Notebook con todo el proceso, desde la carga del dataset, procesamiento para convertirlo en redes, y luego cálculo de propiedades.
- ComplexNetworkAnalysis.html: exportado para abrir en el navegador.
- CElegans_multiplex.pkl: red multicapa guardada con el módulo pickle para poder cargarse en un futuro
- CElegans_Multiplex_Neuronal/: carpeta que contiene el dataset
- Figures/: carpeta con las figuras obtenidas a lo largo del notebook
