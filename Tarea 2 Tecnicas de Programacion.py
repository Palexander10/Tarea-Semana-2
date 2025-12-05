# 1. CLASE PADRE (Abstracción)
# Definimos la plantilla general. Todos los empleados tienen nombre y sueldo base.
class Empleado:

    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    # Este método será compartido por todos, pero algunos lo modificarán.
    def calcular_sueldo(self):
        return self.sueldo_base

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Sueldo a pagar: ${self.calcular_sueldo()}")


# 2. HERENCIA
# 'Desarrollador' hereda todo de 'Empleado' (no necesitamos reescribir nombre o sueldo_base).
class Desarrollador(Empleado):

    def __init__(self, nombre, sueldo_base, horas_extra):
        # Usamos super() para aprovechar el constructor del padre
        super().__init__(nombre, sueldo_base)
        self.horas_extra = horas_extra

    # 3. POLIMORFISMO (Sobrescritura de métodos)
    # Aunque se llama igual que en el padre, aquí el cálculo cambia:
    # El desarrollador cobra su base + horas extra.
    def calcular_sueldo(self):
        pago_extra = self.horas_extra * 20  # $20 por hora extra
        return self.sueldo_base + pago_extra


# 2. HERENCIA
# 'Vendedor' también es un Empleado, pero tiene una lógica distinta.
class Vendedor(Empleado):

    def __init__(self, nombre, sueldo_base, ventas_mes):
        super().__init__(nombre, sueldo_base)
        self.ventas_mes = ventas_mes

    # 3. POLIMORFISMO
    # El vendedor cobra su base + una comisión del 10% de sus ventas.
    def calcular_sueldo(self):
        comision = self.ventas_mes * 0.10
        return self.sueldo_base + comision


# --- SIMULACIÓN (Similar a tu función 'combate') ---

def procesar_nomina(lista_empleados):
    print("=== REPORTE DE NÓMINA ===")
    total_empresa = 0
    
    # Aquí vemos el Polimorfismo en acción:
    # Tratamos a todos como 'empleados', sin importar si son Vendedores o Desarrolladores.
    # Python sabe automáticamente qué versión de 'calcular_sueldo' usar.
    for emp in lista_empleados:
        emp.mostrar_info()
        total_empresa += emp.calcular_sueldo()
        
    print("=========================")
    print(f"Total a desembolsar: ${total_empresa}")


# Creación de Objetos
empleado_1 = Desarrollador("Ana", 2000, 10)    # Base 2000 + 10 horas extra
empleado_2 = Vendedor("Carlos", 1500, 5000)    # Base 1500 + 10% de 5000 en ventas

# Ejecución
mis_empleados = [empleado_1, empleado_2]
procesar_nomina(mis_empleados)