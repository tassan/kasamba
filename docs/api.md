# Kasamba API

## Description

TODO: Write description

## Endpoints (Public)

### Auth

`POST /auth/register`

Request

```json
{
    "username": "johndoe",
    "email": "johndoe@mail.com",
    "password": "hashed-password"
}
```

Response

`200 OK`

```json
{
    "username": "johndoe",
    "email": "johndoe@mail.com",
    "created_at": "2020-01-01T00:00:00Z",
    "is_email_verified": false,
}
```

`400 Bad Request`

```json
{
    "error": "username is already taken"
}
```

`POST /auth/login`

Request

```json
{
    "username": "johndoe",
    "password": "hashed-password"
}
```

Response

`200 OK`

```json
{
    "username": "johndoe",
    "token": "jwt-token"
}
```

`400 Bad Request`

```json
{
    "error": "invalid username or password"
}
```

`POST /auth/logout`

Request

```json
{}
```

Response

`200 OK`

```json
{
    "message": "logged out"
}
```

`POST /auth/verify-email`

Request

```json
{
    "token": "email-verification-token"
}
```

Response

`200 OK`

```json
{
    "username": "johndoe",
    "email": "johndoe@mail.com",
}
```

`400 Bad Request`

```json
{
    "error": "invalid token"
}
```

`POST /auth/reset-password`

```json
{
    "email": "johndoe@mail.com"
}
```

Response

`200 OK`

```json
{
    "message": "password reset"
}
```

`400 Bad Request`

```json
{
    "error": "invalid email"
}
```
