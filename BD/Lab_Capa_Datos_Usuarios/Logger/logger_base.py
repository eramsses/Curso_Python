import logging as log

#Se muestran solo los mensajes desde el nivel configurado, por
#defecto es WARNING
log.basicConfig(level=log.DEBUG,
                format="%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt="%I:%M:%S %p",
                handlers=[
                    log.FileHandler("capa_datos.log", encoding="UTF8"),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.debug("Mensaje de nivel DEBUG")
    log.info("Mensaje de nivel INFO")
    log.warning("Mensaje de nivel de WARNING")
    log.error("Mensaje de nivel de ERROR")
    log.critical("Mensaje de nivel CRÍTICO")




