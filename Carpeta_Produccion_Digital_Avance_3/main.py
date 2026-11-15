
# ==========================================
# AVANCE 3 - CARPETA DE PRODUCCION DIGITAL
# INSTANCIACION Y PRUEBAS
# ==========================================

# 1. IMPORTAR LAS CLASES
from modelos import (
    SoftwarePostproduccion,
    ProduccionAudiovisual,
    ProduccionPostproduccion
)


# 2. INSTANCIACION DE LOS SOFTWARES

software_podcast = SoftwarePostproduccion(
    "Audacity",
    "Edicion de audio"
)

software_cortometraje = SoftwarePostproduccion(
    "DaVinci Resolve",
    "Edicion de video"
)


# 3. INSTANCIACION DE LOS PROYECTOS

# Proyecto creado con la clase base
serie_vampiros = ProduccionAudiovisual(
    "Serie de Vampiros",
    "Serie",
    "Produccion independiente",
    "Postproduccion",
    "Edicion",
    "30 de octubre de 2026"
)


# Proyecto creado con la clase hija
podcast_terror = ProduccionPostproduccion(
    "Podcast de Terror",
    "Podcast",
    "Produccion independiente",
    "Postproduccion",
    "Edicion de audio",
    "15 de octubre de 2026",
    software_podcast,
    "Mezcla final de audio"
)


# Otro proyecto creado con la clase hija
cortometraje_personal = ProduccionPostproduccion(
    "Cortometraje Personal",
    "Cortometraje",
    "Proyecto personal",
    "Postproduccion",
    "Primer corte",
    "20 de noviembre de 2026",
    software_cortometraje,
    "Corte final de video"
)


# 4. PRUEBA DE HERENCIA Y POLIMORFISMO

print("=== INFORMACION DE LOS PROYECTOS ===")

proyectos = [
    serie_vampiros,
    podcast_terror,
    cortometraje_personal
]

for proyecto in proyectos:
    proyecto.mostrar_informacion()


# 5. PRUEBA DE COMPOSICION

print("\n=== PRUEBA DE COMPOSICION ===")

print(
    "Software del podcast:",
    podcast_terror.software_principal.mostrar_software()
)

print(
    "Software del cortometraje:",
    cortometraje_personal.software_principal.mostrar_software()
)


# 6. PRUEBA DE ACTUALIZACIONES

print("\n=== ACTUALIZACIONES ===")

serie_vampiros.cambiar_estado("Correccion de color")

podcast_terror.cambiar_etapa("Mezcla de audio")


# 7. PRUEBA DE ENCAPSULAMIENTO

print("\n=== PRUEBA DE ENCAPSULAMIENTO ===")

print("Fecha actual:", podcast_terror.fecha_entrega)

try:
    podcast_terror.fecha_entrega = ""
except ValueError as error:
    print("Validacion:", error)


# 8. ACTUALIZACION DEL SOFTWARE

print("\n=== ACTUALIZACION DE SOFTWARE ===")

nuevo_software = SoftwarePostproduccion(
    "Adobe Audition",
    "Edicion de audio"
)

podcast_terror.actualizar_software(nuevo_software)


# 9. PRUEBA DE INDEPENDENCIA

print("\n=== INDEPENDENCIA DE LOS PROYECTOS ===")

cortometraje_personal.cambiar_etapa("Entrega")

print(serie_vampiros.nombre, ":", serie_vampiros.etapa)
print(podcast_terror.nombre, ":", podcast_terror.etapa)
print(cortometraje_personal.nombre, ":", cortometraje_personal.etapa)


print("\nPRUEBAS FINALIZADAS CORRECTAMENTE.")
