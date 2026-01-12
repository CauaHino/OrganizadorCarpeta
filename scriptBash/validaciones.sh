#!/bin/bash

comprobar(){
    if [[ $nombre == ""]]; then
        echo "La variable esta vacia"
        read -n1 -p "Pulsa una tecla para continuar..."
        exit 1
    fi
}

# Primer parametro que recibe el script
# Variable local, se puede usar en todo el script

nombre=$1
comprobar