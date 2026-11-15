
# ==========================================
# AVANCE 3 - CARPETA DE PRODUCCION DIGITAL
# COMPOSICION Y MODULARIZACION
# ==========================================


# 1. CLASE AUXILIAR: SOFTWARE DE POSTPRODUCCION
class SoftwarePostproduccion:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_software(self):
        return f"{self.nombre} - {self.tipo}"


# 2. CLASE BASE: PRODUCCION AUDIOVISUAL
class ProduccionAudiovisual:

    def __init__(self, nombre, tipo_proyecto, productora,
                 etapa, estado, fecha_entrega):

        self.nombre = nombre
        self.tipo_proyecto = tipo_proyecto
        self.productora = productora
        self.etapa = etapa
        self.estado = estado
        self.fecha_entrega = fecha_entrega

    # Encapsulamiento mediante propiedad
    @property
    def fecha_entrega(self):
        return self.__fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, nueva_fecha):

        if not isinstance(nueva_fecha, str) or not nueva_fecha.strip():
            raise ValueError("La fecha de entrega no puede estar vacia.")

        self.__fecha_entrega = nueva_fecha

    # Mostrar informacion general
    def mostrar_informacion(self):

        print(f"\nProyecto: {self.nombre}")
        print(f"Tipo: {self.tipo_proyecto}")
        print(f"Productora: {self.productora}")
        print(f"Etapa: {self.etapa}")
        print(f"Estado: {self.estado}")
        print(f"Fecha de entrega: {self.fecha_entrega}")

    # Cambiar etapa
    def cambiar_etapa(self, nueva_etapa):

        self.etapa = nueva_etapa
        print(f"{self.nombre} cambio a la etapa de {self.etapa}.")

    # Cambiar estado
    def cambiar_estado(self, nuevo_estado):

        self.estado = nuevo_estado
        print(f"El estado de {self.nombre} ahora es: {self.estado}.")

    # Cambiar fecha de entrega
    def cambiar_fecha_entrega(self, nueva_fecha):

        self.fecha_entrega = nueva_fecha
        print(f"Nueva fecha de entrega: {self.fecha_entrega}")


# 3. CLASE HIJA: PRODUCCION DE POSTPRODUCCION
class ProduccionPostproduccion(ProduccionAudiovisual):

    def __init__(
        self, nombre, tipo_proyecto, productora, etapa, estado,
        fecha_entrega, software_principal, entregable_principal
    ):

        # Herencia: inicializar los atributos de la clase base
        super().__init__(
            nombre, tipo_proyecto, productora,
            etapa, estado, fecha_entrega
        )

        # Composicion: la produccion tiene un objeto de software
        self.software_principal = software_principal

        self.entregable_principal = entregable_principal

    # Polimorfismo: sobrescritura del metodo
    def mostrar_informacion(self):

        super().mostrar_informacion()

        # Delegacion: utilizar un metodo del objeto contenido
        print(f"Software: {self.software_principal.mostrar_software()}")

        print(f"Entregable: {self.entregable_principal}")

    # Actualizar software
    def actualizar_software(self, nuevo_software):

        if not isinstance(nuevo_software, SoftwarePostproduccion):
            raise TypeError(
                "Se necesita un objeto de tipo SoftwarePostproduccion."
            )

        self.software_principal = nuevo_software

        print(
            f"Software de {self.nombre}: "
            f"{self.software_principal.mostrar_software()}"
        )
