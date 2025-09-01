# Aplicación Multimedia Interactiva para Terapia Motora-Sensitiva en Niños con TEA

Este repositorio contiene el código fuente y los materiales del proyecto "Aplicación Multimedia Interactiva para Terapia Motora-Sensitiva en Niños con Trastorno del Espectro Autista", desarrollado en la Universidad Politécnica de Chiapas.

El proyecto consiste en un videojuego terapéutico, desarrollado en **Pygame**, que se controla mediante los movimientos del jugador, capturados por un sensor externo (acelerómetro/IMU) que se comunica con la aplicación a través de un puerto serial. El objetivo es estimular la coordinación motora y el procesamiento sensorial en niños con TEA de una manera lúdica y atractiva.

Este trabajo fue presentado y reconocido en la **14ª edición de ExpoCiencias, Chiapas 2024**.

## Características

-   Juego interactivo 2D para la recolección de objetos.
-   Control del personaje mediante un sensor físico externo (comunicación serial).
-   Sistema de temporizador y conteo de colisiones.
-   Análisis de movimiento para detectar patrones repetitivos.
-   Diseñado para ser una herramienta de apoyo en terapias de rehabilitación.

## Requisitos

-   Python 3.8+
-   Un sensor (acelerómetro/IMU) capaz de enviar datos JSON a través de un puerto COM.
-   Las librerías de Python listadas en `requirements.txt`.

## Instalación

1.  Clona este repositorio:
    ```bash
    git clone [https://github.com/tu-usuario/TherapyGame-ASD-UPChiapas.git](https://github.com/tu-usuario/TherapyGame-ASD-UPChiapas.git)
    ```
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Asegúrate de configurar el puerto COM correcto en el script `Juego_final.py` (actualmente configurado en 'COM7').

## Créditos

Este proyecto fue desarrollado por los estudiantes:
-   Selina Linette Vázquez Durante
-   [Nombre del otro estudiante si aplica]

Bajo la asesoría del **Dr. Christian Roberto Ibáñez Nangüelú**.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.
