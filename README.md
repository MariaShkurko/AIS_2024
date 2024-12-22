# Composition

**Курс**: Архитектура информационных систем \
**Студент**: Шкурко Мария Алексеевна \
**Группа**: М8О-101СВ-24

## Запуск приложения

```commandline
docker network create composition_network
docker-compose up -d
```

Swagger - http://localhost:8080/docs#

OpenAPI документация - http://localhost:8080/openapi.json

Доступные аккаунты для тестирования авторизации:
```commandline
login: user1
password: Qweasd123

login: user2
password: Rtyfgh456

login: user3
password: Uiojkl789
```

Сервис score работает по принципу рандома.