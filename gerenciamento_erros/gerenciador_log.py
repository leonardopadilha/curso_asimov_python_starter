import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

#lembrar dos diferentes níveis
logging.basicConfig(filename="app.log", level=logging.DEBUG, format=LOG_FORMAT) 
log = logging.getLogger()
log.info("Log de Teste")
log.critical("Erro grave")
log.error("Error")