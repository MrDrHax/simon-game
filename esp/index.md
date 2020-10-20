># Instrucciones

**SIMON is a really easy and fun game to play**

## Dependencias

*Necesitas:*

* pyglet

* python 3.8.x

### Para instalar pyglet

`pip install pyglet`

_Descargar el juego [aquí](https://github.com/MrDrHax/simon-game/releases/tag/official) _

_Descomprime el juego_

_Guardalo en una carpeta conocida_

## Para correr el juego

_abrir `main.py`

_Correr el juego_

_Ahora ¡a jugar!_

### Instrucciones rápidas para jugar

_Escucha y ve con cuidado la ventana_

_Los **sonidos y colores** te indicaran la secuencia a seguir_

_Solo es cuestión de que des **clic** a los colores para recrear la secuencia_

_Si fallas, tu marcador volverá a cero (es el que está en el centro) y se repetirá hasta que tu quieras terminar_

_Pero si tu secuencia es correcta:_

**¡Tu marcador irá aumentando!**

_El reto del juego es poner aprueba tu **memoria, agilidad y ver si eres capaz de superar tus propios marcadores**_


# Proyecto Integrador: Juegos Cognitivos 

Ver  que  nuestro  país  tiene  potencial  pero  que  no  sea  reconocido  de  esa  forma  o impulsado, hace que el talento sea desperdiciado y sea utilizado en otras cosas.  Se sabe que el estudio es importante, más que hoy en día poder llevar una buena vida, es necesario el estudio, pero el estudio sigue siendo necesario aún después de haber ejercido para mantenerse actualizado e irse innovando. 

Por  eso  mismo,  el  aprendizaje  desde  pequeños  es  fundamental, al igual  que  conocer nuestras habilidades y debilidades para irlas puliendo y ser grandes en la vida.  

Actualmente, la tecnología es como una extremidad más. Esta presente en nuestro día a día, y todo eso se hizo gracias al ingenio de ciertas personas para poder obtener una vida más cómoda, usando la tecnología como base para la siguiente fase de evolución. 


Como  se  dijo  anteriormente,  la  educación  es  esencial  para  la  vida,  solo  que  luego  el estilo  de  educación  no  se  va  innovando,  haciendo  que  para  los  jóvenes  sea  más complicado  tratar  de  mantenerse  conforma  esas  ideas  educativas  anteriores.  Por  eso mismo,  si  intentamos  usar  la  tecnología  como  apoyo,  pudiera  haber  más  interés  para las  nuevas  generaciones  que  viven  en  un  mundo  digital  y  tecnológico,  de  seguir estudiando y poder impulsar aquel talento que se tiene perdido.  

Dado  eso,  se  propone  un  juego  digital  en  el  cual  se  esta  ayudando  al  cerebro  a reaccionar de forma más rápida, usando los sentidos y la tecnología de forma divertida como una nueva forma de aprender.  

El código del juego ejecuta un bucle principal, donde se almacenan todas las variables, aquí  es  donde  se  ejecuta  el  bucle  principal  de  pyglet.  Después  se  crean  2  estados diferentes para cada color, por lo que son 8 batches(terminología de pyglet)  en total, y cada vez que se refresca la pantalla se re dibuja todos los colores, todas las líneas se pre-renderizan todas la líneas y solamente se dibujan cuando sea necesario a la hora de correr. 

Dependiendo  de  la  luz  del  color,  se  colorea  un  segmento  de  líneas  con  un  color  más brillante a la hora de ser presionado. Luego se deja que un script controle las notas, y la  otra  parte  del  código  hace  todas  las  comprobaciones  de  la  información  dentro  del código.  Al  final,  estas  partes  del  código  permanecen  en  diferentes  archivos  y  se importan al principal. 


#### SIMON:
es  un  juego  creado  en  pyglet  en  donde  al  correr  el  código  se  despliega  un tablero en donde se ven 4 colores oscuros al rededor de un contador que inicia en 0. El juego comienza dando un patrón de colores y sonidos para que pueda ser seguido por el  jugador,  si  se  realiza  correctamente  el  patrón,  el  contador  marcará  un  punto  y  así sucesivamente.  Pero  si  no  se  realiza  bien  el  patrón,  el  contador  volverá  a  su  valor original y se tendrá que empezar de nuevo.  El punto del juego es poner a prueba la memoria usando los sentidos y la diversión de un sencillo juego con colores y sonidos. A su vez, de que el juego puede ser usado en turnos  con  otros  jugadores  para  ver  quien  llega  más  lejos,  haciendo  una  competencia saludable, como nuevo reto el cual se puede ir superando. De esta forma, se ejercita el cerebro y se puede lograr una gran reflexión de como usar la tecnología para el bien y la educación.  

Se  tuvo  la  idea  de  realizar  este  juego  al  pensar  en  poner  a  prueba  la  memoria  de  los jugadores,  junto  con  la  emoción  y  deseo  de  crear  algo  divertido  con  la  finalidad  de seguir aprendiendo.  

Como ingenieros en que aspiramos ser, hacer este tipo de proyectos nos da una nueva visión  de  como  usar  nuestras  herramientas  aprendidas  a  lo  largo  de  la  carrera  para  ir innovando  el  mundo  con  nuestras  creaciones  sin  perder  de  vista  nuestro  sentido humano
