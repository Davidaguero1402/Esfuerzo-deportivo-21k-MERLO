from flask import Flask, render_template, request
#from foundrunner import found_runner
from buscarcooredor import found_runner
app = Flask(__name__)



# Conectar a la base de datos


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        dorsal = request.form.get('dorsal') #esto es el elemento name de la etiqueta del formulario
        print(dorsal)

        if dorsal is not None:
            
            datos_corredor = found_runner(dorsal)
            print(datos_corredor)

            if datos_corredor != 'Dorsal inexistente':

                print(datos_corredor)

                datos={'dorsal':datos_corredor[0], 'titulo': 'Tu tiempo','nombre':datos_corredor[1],'tiempo': datos_corredor[2]}
                #Devolvemos los datos del corredor
                return render_template('tutiempo.html', datos = datos)
                
            else:
                #sino encontramos al dorsal que se busco retornamos otra pagina dorsalnotfound
                datos={'dorsal':dorsal, 'titulo': 'Dorsal no encontrado', 'nombre':datos_corredor[1]}
                return render_template('dorsalnotfound.html', datos = datos)

    return render_template('index.html',titulo='Esfuerzo deportivo')
 



if __name__ == '__main__':
    print('Ejecutando la aplicación en el puerto 8000...')
    
    app.run(host='0.0.0.0' ,port=8000, debug=False)
