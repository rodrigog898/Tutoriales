# Kafka Topics Management

Este documento describe los comandos esenciales para la gestión de tópicos en Apache Kafka utilizando Docker.

## Listar Tópicos

Para listar los tópicos disponibles en el clúster de Kafka, ejecuta el siguiente comando:

```sh
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
```

## Escuchar un Tópico

Para consumir mensajes de un tópico específico desde el principio, usa el siguiente comando:

```sh
docker exec -it kafka kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic Interview_Preparing \
  --from-beginning
```

## Crear un Tópico

Para crear un tópico en Kafka, utiliza el siguiente comando:

```sh
docker exec -it kafka kafka-topics --create --topic <nombre_del_topico> --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

Ejemplos de creación de tópicos:

```sh
docker exec -it kafka kafka-topics --create --topic Interview_Preparing --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

Este proceso se puede repetir para otros tópicos requeridos en el sistema.

