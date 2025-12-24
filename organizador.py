import os
import shutil as sh

rutaOrigen = input('Ponga la ruta que desea organizar')

extensiones = {
    'Imagenes' : ['.jpg', '.jpeg', '.png','.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos' : ['.mp4', '.mov', '.avi'],
    'Instaladores' : ['.exe', '.dmg', '.pkg']
}

def organizar(): 
    os.chdir(rutaOrigen)

    for archivo in os.listdir():
        nombre, ext = os.path.splitext(archivo)
        
        for categoria, listaExt in extensiones.items():
            if ext.lower() in listaExt:
                if not os.path.exists(categoria):
                    os.makedirs(categoria)

                sh.move(archivo, f"{categoria}/{archivo}")
                print(f"Movido: {archivo} para {categoria}")

if __name__ == "__main__":
    organizar()
    print('Carpeta Organizada!')


    

