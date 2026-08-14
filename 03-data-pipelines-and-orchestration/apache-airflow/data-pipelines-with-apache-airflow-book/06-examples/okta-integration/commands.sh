#!/bin/bash

OPCION="${1:-}"

usage() {
    echo "Usage: $0 {1|2|3|4}"
    echo "  1: Levantar Contenedores"
    echo "  2: Copiar archivos desde el contenedor"
    echo "  3: Bajar Contenedores"
    echo "  4: Reiniciar"
    exit 1
}

if [[ -z "$OPCION" ]]; then
    usage
fi

case "$OPCION" in
    1|4)
        echo "--- Levantando contenedores ---"
        docker compose up -d
        ;;

    2)
        echo "--- Copiando archivos de configuración ---"
        CONTAINER_ID=$(docker compose ps -q airflow-webserver)
        
        if [[ -n "$CONTAINER_ID" ]]; then
            docker cp "$CONTAINER_ID:/opt/airflow/webserver_config.py" ./permissions/webserver_config.py
            echo "Archivos copiados con éxito."
	    echo "Modificar los archivos."
        else
            echo "Error: No se encontró el contenedor 'airflow-webserver'. ¿Está encendido?"
            exit 1
        fi
        ;;

    3)
        echo "--- Bajando contenedores ---"
        docker compose down
        ;;

    *)
        echo "Opción no válida: $OPCION"
        usage
        ;;
esac
