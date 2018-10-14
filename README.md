# flask-mysql-restful-on-docker

PythonのFlaskでMySQLを利用したRESTfulなAPIをDocker環境で実装する  

## Install

```sh
> git clone https://github.com/kai-kou/flask-mysql-restful-api-on-docker.git
> cd flask-mysql-restful-api-on-docker
> docker-compose up -d
> docker-compose exec api bash
>> flask db init
>> flask db migrate
>> flask db upgrade
```

## Usage

```sh
# POST
> curl -X POST http://localhost:5000/hoges \
  -H "Content-Type:application/json" \
  -d "{\"name\":\"hoge\",\"state\":\"hoge\"}"

# PUT
> curl -X PUT http://localhost:5000/hoges/[id] \
  -H "Content-Type:application/json" \
  -d "{\"name\":\"hogehoge\"}"

# GET
> curl http://localhost:5000/hoges/[id]

# GET List
> curl http://localhost:5000/hoges

# DELETE
> curl -X DELETE http://localhost:5000/hoges/[id]
```

## Test

```sh
> docker-compose exec api pytest
```
