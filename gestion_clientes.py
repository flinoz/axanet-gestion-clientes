import os
import datetime

# --- CONFIGURACIÓN ---
# Directorio donde se guardarán los archivos de los clientes.
CLIENTS_DIR = "axanet_clients"
# Mapa en memoria (Tabla Hash) para asociar nombre de cliente -> nombre de archivo
mapa_clientes = {}

# --- FUNCIONES DE SERVICIO (Lógica de Archivos y Mapa) ---

def _normalizar_nombre(client_name):
    """Convierte un nombre en un nombre de archivo válido."""
    # Quita espacios al inicio/final, reemplaza espacios internos con _ y añade .txt
    return client_name.strip().replace(" ", "_") + ".txt"

def _cargar_mapa_clientes():
    """
    (Re)Carga el mapa de clientes (Tabla Hash) desde el directorio.
    Esto escanea el disco y puebla nuestro diccionario en memoria.
    """
    print("Iniciando sistema...")
    if not os.path.exists(CLIENTS_DIR):
        print(f"Creando directorio de datos en: {os.path.abspath(CLIENTS_DIR)}")
        os.makedirs(CLIENTS_DIR)
        
    mapa_clientes.clear()
    for filename in os.listdir(CLIENTS_DIR):
        if filename.endswith(".txt"):
            # Obtenemos el nombre del cliente desde el nombre del archivo
            client_name = filename.replace("_", " ").replace(".txt", "")
            # La llave del mapa es el nombre en minúsculas para búsquedas fáciles
            mapa_clientes[client_name.lower()] = filename
            
    print(f"[Sistema] Mapa de clientes cargado: {len(mapa_clientes)} clientes encontrados.")
    input("Presiona Enter para continuar...")

def _get_filepath(client_name):
    """Usa la tabla hash para encontrar el path de un archivo rápidamente."""
    # Busca usando el nombre en minúsculas
    filename = mapa_clientes.get(client_name.strip().lower())
    if filename:
        return os.path.join(CLIENTS_DIR, filename)
    return None

def _log_servicio(filepath, descripcion):
    """Añade una línea de servicio estandarizada a un archivo."""
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"Fecha: {fecha_hora} | Descripción: {descripcion}\n")

# --- FUNCIONES DE NEGOCIO (Lógica de Clientes) ---

def crear_cliente():
    """Crea un nuevo archivo de cliente."""
    print("--- 1. Creación de Nuevo Cliente ---")
    client_name = input("Introduce el nombre completo del nuevo cliente: ").strip()
    
    if not client_name:
        print("\nError: El nombre del cliente no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    filepath = _get_filepath(client_name)
    
    # Validación usando la tabla hash
    if filepath:
        print(f"\nError: ¡El cliente '{client_name}' ya existe en '{filepath}'!")
        input("Presiona Enter para continuar...")
        return
        
    service_desc = input("Introduce la descripción del primer servicio solicitado: ")
    
    # Creación del archivo
    filename = _normalizar_nombre(client_name)
    filepath = os.path.join(CLIENTS_DIR, filename)
    
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("=============================================\n")
            f.write(f"Cliente: {client_name}\n")
            f.write(f"Fecha de Alta: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
            f.write("=============================================\n\n")
            f.write("--- Historial de Servicios ---\n")
        
        _log_servicio(filepath, service_desc)
        
        # Actualizar la tabla hash en memoria
        mapa_clientes[client_name.lower()] = filename
        
        print(f"\n¡Cliente '{client_name}' creado exitosamente en '{filepath}'!")
        
    except IOError as e:
        print(f"\nError al escribir el archivo: {e}")
        
    input("Presiona Enter para continuar...")

def modificar_cliente():
    """Agrega un nuevo servicio a un cliente existente."""
    print("--- 2. Agregar Servicio a Cliente Existente ---")
    client_name = input("Introduce el nombre del cliente a modificar: ")
    
    filepath = _get_filepath(client_name)
    
    # Validación usando la tabla hash
    if not filepath:
        print(f"\nError: ¡El cliente '{client_name}' no fue encontrado!")
        input("Presiona Enter para continuar...")
        return

    print("\nCliente encontrado. Mostrando historial actual:")
    print("-" * 30)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
        input("Presiona Enter para continuar...")
        return
        
    print("-" * 30)
    service_desc = input("Introduce la descripción del NUEVO servicio: ")
    
    if not service_desc:
        print("\nOperación cancelada. La descripción no puede estar vacía.")
        input("Presiona Enter para continuar...")
        return
        
    try:
        _log_servicio(filepath, service_desc)
        print("\n¡Nuevo servicio agregado exitosamente!")
    except IOError as e:
        print(f"\nError al agregar servicio: {e}")
        
    input("Presiona Enter para continuar...")

def visualizar_cliente():
    """Muestra la información de un cliente específico."""
    print("--- 3. Visualizar Información de Cliente ---")
    client_name = input("Introduce el nombre del cliente a visualizar: ")
    
    filepath = _get_filepath(client_name)
    
    # Validación usando la tabla hash
    if not filepath:
        print(f"\nError: ¡El cliente '{client_name}' no fue encontrado!")
        input("Presiona Enter para continuar...")
        return

    print(f"\nMostrando información de '{client_name}':")
    print("=" * 40)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    except IOError as e:
        print(f"Error al leer el archivo: {e}")
    print("=" * 40)
    input("Presiona Enter para continuar...")

def listar_clientes():
    """Muestra todos los clientes de la tabla hash en memoria."""
    print("--- 4. Lista de Todos los Clientes ---")
    if not mapa_clientes:
        print("No hay clientes registrados.")
    else:
        # Itera sobre las llaves (nombres en minúsculas) pero muestra el nombre de archivo formateado
        for client_name_lower in sorted(mapa_clientes.keys()):
            # Obtenemos el nombre de archivo real
            filename = mapa_clientes[client_name_lower]
            # Convertimos el nombre de archivo de nuevo a un nombre legible
            client_name_capitalized = filename.replace("_", " ").replace(".txt", "")
            print(f"- {client_name_capitalized}")
            
    print("-" * 30)
    input("Presiona Enter para continuar...")

def eliminar_cliente():
    """Elimina el archivo de un cliente y lo saca del mapa."""
    print("--- 5. Eliminar Cliente ---")
    client_name = input("Introduce el nombre del cliente a ELIMINAR: ")
    
    filepath = _get_filepath(client_name)
    
    # Validación usando la tabla hash
    if not filepath:
        print(f"\nError: ¡El cliente '{client_name}' no fue encontrado!")
        input("Presiona Enter para continuar...")
        return

    # Confirmación de seguridad
    print(f"\nADVERTENCIA: Estás a punto de eliminar permanentemente a '{client_name}'.")
    confirmacion = input("¿Estás seguro de que deseas continuar? (escribe 'si' para confirmar): ").lower()
    
    if confirmacion == 'si':
        try:
            os.remove(filepath)
            # Eliminar de la tabla hash en memoria
            del mapa_clientes[client_name.strip().lower()]
            print(f"\n¡Cliente '{client_name}' eliminado exitosamente!")
        except IOError as e:
            print(f"\nError al eliminar el archivo: {e}")
    else:
        print("\nOperación cancelada.")
        
    input("Presiona Enter para continuar...")

# --- BUCLE PRINCIPAL (API Gateway) ---
def main():
    _cargar_mapa_clientes()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Limpiar pantalla
        print("=====================================")
        print("  Sistema de Gestión de Clientes AXANET (Python)")
        print("=====================================")
        print("1. Crear nuevo cliente")
        print("2. Agregar servicio a cliente existente")
        print("3. Visualizar información de un cliente")
        print("4. Listar todos los clientes")
        print("5. Eliminar cliente")
        print("6. Salir")
        print("-------------------------------------")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            modificar_cliente()
        elif opcion == '3':
            visualizar_cliente()
        elif opcion == '4':
            listar_clientes()
        elif opcion == '5':
            eliminar_cliente()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()