# Как развернуть проект
## Для разработки / For development
#####  Сборка пересборка запуск
```sh
docker-compose up -d --build
```
#####  при последующих запусках 
```sh
docker-compose up -d runserver
```
##### Dev superuser:
- auto cteates from fixtures
###### login: toha
###### passwd: bqyuio

------------------------
### Примеры вызовов API
### API examples
#### Только для чтения / Only for  read only 
######  /api/v1/ 
- Корневой зарос к API, возвращает список дочерних запросов

###### /api/v1/pages/
- список страниц, каждый элемент которого содержит url на API c детальной информацией
- list of pages, each element contains API - url to detail info

###### /api/v1/contents/
- список контента всех страниц, каждый элемент которого содержит url на API c детальной информацией
- list of contents, each element contains API - url to detail info