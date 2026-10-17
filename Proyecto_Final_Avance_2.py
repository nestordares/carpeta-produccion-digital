
# AVANCE 2 - CARPETA DE PRODUCCIÓN DIGITAL
# Este sistema permite registrar proyectos audiovisuales y consultar o modificar
# sus datos. Se utilizan clases, encapsulamiento, herencia y polimorfismo.

# 1. CLASE BASE Y ENCAPSULAMIENTO
class ProduccionAudiovisual:
    # El constructor inicializa los datos que comparten todos los proyectos.
    # El atributo fecha_entrega se administra mediante una propiedad
    # para controlar los valores que se pueden guardar.
    def __init__(self, nombre, tipo_proyecto, productora, etapa, estado, fecha_entrega):
        self.nombre = nombre
        self.tipo_proyecto = tipo_proyecto
        self.productora = productora
        self.etapa = etapa
        self.estado = estado
        self.fecha_entrega = fecha_entrega

    # Esta propiedad permite consultar la fecha de entrega sin acceder
    # directamente al atributo privado __fecha_entrega.
    @property
    def fecha_entrega(self):
        return self.__fecha_entrega

    # El setter valida que la fecha sea texto y no esté vacía.
    # Así se evita guardar una fecha sin información.
    @fecha_entrega.setter
    def fecha_entrega(self, nueva_fecha):
        if not isinstance(nueva_fecha, str) or not nueva_fecha.strip():
            raise ValueError("La fecha de entrega no puede estar vacía.")
        self.__fecha_entrega = nueva_fecha

    # Muestra la información general de un proyecto audiovisual.
    def mostrar_informacion(self):
        print(f"\nProyecto: {self.nombre}")
        print(f"Tipo: {self.tipo_proyecto}")
        print(f"Productora: {self.productora}")
        print(f"Etapa: {self.etapa}")
        print(f"Estado: {self.estado}")
        print(f"Fecha de entrega: {self.fecha_entrega}")

    # Permite actualizar la etapa de un proyecto sin modificar los demás.
    def cambiar_etapa(self, nueva_etapa):
        self.etapa = nueva_etapa
        print(f"{self.nombre} cambió a la etapa de {self.etapa}.")

    # Actualiza el estado actual del proyecto, por ejemplo, su proceso de edición.
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado de {self.nombre} ahora es: {self.estado}.")

    # Cambia la fecha usando la propiedad, por lo que también se aplica
    # la validación definida en el setter.
    def cambiar_fecha_entrega(self, nueva_fecha):
        self.fecha_entrega = nueva_fecha
        print(f"Nueva fecha de entrega: {self.fecha_entrega}")


# 2. HERENCIA: CLASE ESPECIALIZADA EN POSTPRODUCCIÓN
# Esta clase hereda los datos y métodos de ProduccionAudiovisual.
# Se especializa en proyectos de postproducción y agrega información
# sobre el software utilizado y el entregable principal.
class ProduccionPostproduccion(ProduccionAudiovisual):
    def __init__(
        self, nombre, tipo_proyecto, productora, etapa, estado,
        fecha_entrega, software_principal, entregable_principal
    ):
        # super() llama al constructor de la clase padre para inicializar
        # los atributos generales sin tener que repetir ese código.
        super().__init__(
            nombre, tipo_proyecto, productora, etapa, estado, fecha_entrega
        )

        # Estos atributos son propios de los proyectos de postproducción.
        self.software_principal = software_principal
        self.entregable_principal = entregable_principal

    # Sobrescritura de método (polimorfismo):
    # se conserva la información general del método heredado y se añaden
    # los datos específicos de postproducción.
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Software: {self.software_principal}")
        print(f"Entregable: {self.entregable_principal}")

    # Permite actualizar el software utilizado y evita guardar un texto vacío.
    def actualizar_software(self, nuevo_software):
        if not nuevo_software.strip():
            raise ValueError("El software no puede estar vacío.")
        self.software_principal = nuevo_software
        print(f"Software de {self.nombre}: {self.software_principal}")


# 3. INSTANCIACIÓN Y PRUEBAS
# Se crean tres objetos independientes para representar proyectos diferentes.
# El primero utiliza la clase base y los otros dos utilizan la clase hija.
serie_vampiros = ProduccionAudiovisual(
    "Serie de Vampiros", "Serie", "Producción independiente",
    "Postproducción", "Edición", "30 de octubre de 2026"
)

podcast_terror = ProduccionPostproduccion(
    "Podcast de Terror", "Podcast", "Producción independiente",
    "Postproducción", "Edición de audio", "15 de octubre de 2026",
    "Reaper", "Mezcla final de audio"
)

cortometraje_personal = ProduccionPostproduccion(
    "Cortometraje Personal", "Cortometraje", "Proyecto personal",
    "Postproducción", "Primer corte", "20 de noviembre de 2026",
    "DaVinci Resolve", "Corte final de video"
)

# Prueba de polimorfismo:
# se llama al mismo método en objetos de clases diferentes.
# Cada objeto muestra la información que le corresponde según su clase.
print("=== INFORMACIÓN DE LOS PROYECTOS ===")
serie_vampiros.mostrar_informacion()
podcast_terror.mostrar_informacion()
cortometraje_personal.mostrar_informacion()

# Prueba de actualización:
# se modifican el estado de un proyecto y el software de otro.
print("\n=== ACTUALIZACIONES ===")
serie_vampiros.cambiar_estado("Corrección de color")
podcast_terror.actualizar_software("Adobe Audition")

# Prueba de encapsulamiento y validación:
# se consulta la fecha mediante la propiedad y se intenta asignar
# un valor vacío para comprobar que el setter lo rechaza.
print("\n=== ENCAPSULAMIENTO ===")
print(f"Fecha actual: {podcast_terror.fecha_entrega}")

try:
    podcast_terror.fecha_entrega = ""
except ValueError as error:
    print(f"Validación: {error}")

# Prueba de independencia:
# se cambia la etapa del cortometraje y se consultan los tres proyectos
# para verificar que modificar un objeto no cambia los otros.
print("\n=== INDEPENDENCIA ===")
cortometraje_personal.cambiar_etapa("Entrega")

print(f"{serie_vampiros.nombre}: {serie_vampiros.etapa}")
print(f"{podcast_terror.nombre}: {podcast_terror.etapa}")
print(f"{cortometraje_personal.nombre}: {cortometraje_personal.etapa}")
