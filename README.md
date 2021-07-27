# api_bast

## Описание
* После авторизации, пользователь может создать аккаунт с параметрами:
    - Имя,
    - Фамилия,
    - Адрес,
    - Фото пользователя.
* Можно редактировать созданный аккаунт.

Работа с аккаунтами пользователя с помощью запросов: 
 
  GET  http://localhost:8000/api/v1/users/        #Посмотреть всех пользователей 
   
  GET  http://localhost:8000/api/v1/users/{id}/   #Получить конкретного пользователя по id 
        
  POST  http://localhost:8000/api/v1/users/       #Создание пользователя
   
  PUT   http://localhost:8000/api/v1/users/{id}/  #Обновить данные о пользователе по id 
   
  PATCH http://localhost:8000/api/v1/users/{id}/  #Частично обновить данные о пользователе по id 
   
  DELETE http://localhost:8000/api/v1/users/{id}/ #Удалить публипользователякацию по id 
  

   JWT-токен: 
    
   http://localhost:8000/api/v1/token/           #Получить JWT-токен 
    
   http://localhost:8000/api/v1/token/refresh/   #Обновить JWT-токен 