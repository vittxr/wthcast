#coisas para melhorar: 
   #- Colocar os dados da requisições em um arquivo.csv, para agilizar a busca desses dados quando necessário. Quando o browser for fechado, exclui-lo. 
   

import os  
import app   
from app import create_app 
 
app = create_app()
app.config['SECRET_KEY'] = 'qualquercoisa'

if __name__ == "__main__":
    app.run(debug=True)