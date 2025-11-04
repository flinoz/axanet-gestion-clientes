📂 Sistema de Gestión de Clientes Axanet

Este repositorio contiene el código fuente para un sistema de gestión de clientes desarrollado en Python para la empresa Axanet. La aplicación permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los archivos de los clientes.

El proyecto también incluye una configuración de GitHub Actions para la automatización de flujos de trabajo basados en Issues.

✨ Características Principales

Crear Cliente: Genera un nuevo archivo para un cliente con su primera solicitud de servicio.

Actualizar Cliente: Agrega nuevas solicitudes de servicio a un cliente existente.

Visualizar Cliente: Muestra el historial completo de un cliente específico.

Listar Clientes: Muestra una lista de todos los clientes registrados.

Eliminar Cliente: Borra permanentemente el archivo de un cliente.

Optimización: Utiliza un mapa hash (diccionario de Python) para búsquedas de clientes en tiempo $O(1)$.

🚀 Requisitos e Instalación

Para ejecutar este proyecto, solo necesitas tener Python 3.x instalado en tu sistema.

Clona el repositorio:

git clone [https://github.com/TU_USUARIO/axanet-gestion-clientes.git](https://github.com/TU_USUARIO/axanet-gestion-clientes.git)


Navega al directorio del proyecto:

cd axanet-gestion-clientes


▶️ Cómo Usar el Sistema

Simplemente ejecuta el script principal desde tu terminal:

python gestion_clientes.py


El script se iniciará, cargará los clientes existentes (o creará el directorio axanet_clients/ si es la primera vez) y te presentará un menú interactivo.

🤖 Flujo de Trabajo (GitHub Actions)

Este proyecto utiliza GitHub Actions para notificar al equipo sobre nuevas solicitudes de trabajo. El flujo se activa cuando se crea un Issue con una de las siguientes etiquetas:

accion: crear-cliente

accion: actualizar-cliente

accion: consultar-cliente

Cuando se detecta, el bot publicará automáticamente un comentario en el Issue, mencionando a los miembros del equipo.

📄 Licencia

Este proyecto está protegido bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.