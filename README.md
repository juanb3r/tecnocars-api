- API para los mantenimientos correctivos y preventivos vehicular de las empresas asociadas a TecnoCars.
- En esta API tenemos un superusuario que es la empresa TecoCars, la cual puede editar, borrar, crear y consultar a los usuarios (empresas asociada) y a los clientes (carros de las empresas asociadas).
- Los usuarios los cuales tienen la información de sus vehículos en la API, pueden consultar y descargar la información de los mantenimientos correcticos y preventivos, tener la ficha técnica de la bimensual de los vehículos (estos son dos archivos).

### TecnoCars-API

![](https://github.com/DaggerAlmanza/tecnocars-api/blob/main/FotoTecno.jpg)

**Tabla de contenido**

    |      Login        | Close Login   |
    | -------------     | ------------- |
    | 1) username: str  |               |    
    | 2) password: str  |               |
    .....................................


User


    |      Create        |       Edit         |      Delete        |       Show         |
    | ------------------ |  ------------------| ------------------ | ------------------ |
    | 1) name: str       | 1) name: str       | 1) Delete_id: int  |                    |
    | 2) username: str   | 2) username: str   |                    |                    |
    | 3) password: str   | 3) password: str   |                    |                    |
    | 4) access: bool    | 4) access: bool    |                    |                    |
    |                    | 5) number_id: int  |                    |                    |
     ....................................................................................

Client


    |         Create          |           Edit          |      Delete        |       Show         |
    | ----------------------- |  ---------------------- | ------------------ | ------------------ |
    | 1) empresa: str         | 1) empresa: str         | 1) Delete_id: int  |                    |
    | 2) placa_empresa: str   | 2) placa_empresa: str   |                    |                    |
    | 3) placa: str           | 3) placa: str           |                    |                    |
    | 4) bimensual: date      | 4) bimensual: date      |                    |                    |
    | 5) bimensual: date      | 5) bimensual: date      |                    |                    |
    | 6) tecnomecanica: date  | 6) tecnomecanica: date  |                    |                    |
    | 7) poliza: date         | 7) poliza: date         |                    |                    |
    | 8) fecha_registro: date | 8) fecha_registro: date |                    |                    |
    | 9) aprobado: bool       | 9) aprobado: bool       |                    |                    |
    |                         | 10) number_id           |                    |                    |
     .............................................................................................
     
    
