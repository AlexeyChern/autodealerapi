JSON-Schemas:

Cars:

    {
        "id": {
          "type": "integer",
          "required": true
        },
        "ModelName": {
          "type": "string",
          "required": true
        },
        "BrandName": {
          "type": "string",
          "required": false
        }
    }

Dealers:
    {
      "id": {
        "type": "integer",
        "required": true
      },
      "CompanyName": {
        "type": "string",
        "required": true
      }
    }

Comparing:

    {
        "id": {
          "type": "integer",
          "required": true
        },
        "DealerId": {
          "type": "integer",
          "required": true
        },
        "CarId": {
          "type": "integer",
          "required": true
        },
        "Price": {
          "type": "number",
          "required": true
        },
        "Quantity": {
          "type": "integer",
          "required": true
        },
        "IsNew": {
          "type": "boolean",
          "required": false
        }
    }


Примеры запросов:

Получение данных:
Все авто: /api/cars
Получение авто по id: /api/onecar/<int:pk>

Все дилеры: /api/dealers
Дилер по id: /api/onedealer/<int:pk>

Все записи учета: /api/comparings
Запись учета по id: /api/onecomparing/<int:pk>

Добавление автомобиля
POST: /api/cars
Body: {"car": {"BrandName":"Toyota", "ModelName":"Celica"}} ИЛИ  {"car":{"ModelName":"Celica"}}

Добавление дилера:

POST: /api/dealers
Body: {"dealer": {"CompanyName":"DATSUN PROFI"}}

Добавление записи учета авто у дилера
POST: /api/comparings
Body: {"compares": {"DealerId":2, "CarId": 6, "Price": 1100.5, "Quantity": 10}} ИЛИ {"compares": {"DealerId":2, "CarId": 6, "Price": 1100.5, "Quantity": 10, "IsNew": "False"}}


Редактирование записи по id:

Авто: /api/cars/<int:pk>
Body: {"car":{"ModelName":"Celica"}}

Дилер: /api/dealers/<int:pk>
Body: {"dealer": {"CompanyName":"DATSUN PROFI"}}

Запись учета: /api/comparings/<int:pk>
Body: {"compares": {"DealerId":3}}

Удаление записей по id:

Авто: /api/cars/<int:pk>
Дилер: /api/dealers/<int:pk>
Запись учета: /api/comparings/<int:pk>

Удаление связи по названию компании дилера, марке и модели.
POST: /api/optionaldeletecompares
Body: {"CompanyName": "DATSUN PROFI", "ModelName": "Celica", "BrandName": "Toyota"}
