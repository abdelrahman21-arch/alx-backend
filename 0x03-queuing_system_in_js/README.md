# Redis README

## Introduction
Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, geospatial indexes, and streams.

## Key Features
- **In-Memory Storage**: Extremely fast read and write operations.
- **Persistence**: Data persistence through RDB snapshots and AOF logs.
- **Replication**: Master-slave replication for redundancy.
- **High Availability**: Redis Sentinel for monitoring, automatic failover, and notifications.
- **Clustering**: Redis Cluster for automatic data sharding.
- **Rich Data Types**: Strings, lists, sets, sorted sets, hashes, bitmaps, hyperloglogs, geospatial indexes.
- **Transactions**: Support for atomic operations through MULTI, EXEC, DISCARD, and WATCH.
- **Pub/Sub Messaging**: Built-in publish/subscribe capabilities.
- **Lua Scripting**: Execute complex operations atomically using Lua scripts.
- **Extensive Ecosystem**: Numerous client libraries and integrations.

## Installation

### Using Package Managers
#### Debian/Ubuntu
```sh
sudo apt update
sudo apt install redis-server
```

#### macOS (Homebrew)
```sh
brew update
brew install redis
```

### From Source
```sh
wget http://download.redis.io/releases/redis-6.2.5.tar.gz
tar xzf redis-6.2.5.tar.gz
cd redis-6.2.5
make
```

## Basic Usage

### Starting Redis Server
```sh
redis-server
```

### Starting Redis Client
```sh
redis-cli
```

### Basic Commands
```sh
SET key value        # Set the value of a key
GET key              # Get the value of a key
DEL key              # Delete a key
INCR key             # Increment the integer value of a key
LPUSH key value      # Prepend a value to a list
LRANGE key start stop  # Get a range of elements from a list
```

### Persistence
#### RDB Snapshot
Redis can create point-in-time snapshots of your dataset, stored in binary files.

#### AOF (Append Only File)
Redis can log every write operation received by the server.

## Configuration
Redis configuration is done via a configuration file, typically located at `/etc/redis/redis.conf`.

### Example Configuration
```sh
bind 127.0.0.1
protected-mode yes
port 6379
tcp-backlog 511
timeout 0
tcp-keepalive 300
loglevel notice
databases 16
save 900 1
save 300 10
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb
dir ./
```

## Advanced Features

### Transactions
```sh
MULTI
SET key value
INCR key
EXEC
```

### Pub/Sub
```sh
# Subscribe to a channel
SUBSCRIBE channel

# Publish a message to a channel
PUBLISH channel message
```

### Lua Scripting
```sh
# Run a Lua script
EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 key value
```

### Replication
In `redis.conf`:
```sh
slaveof <masterip> <masterport>
```

### Sentinel
Redis Sentinel provides high availability and monitoring.
```sh
# Start Sentinel
redis-sentinel /etc/redis/sentinel.conf
```

## Redis Cluster
Redis Cluster allows you to run a Redis installation where data is automatically sharded across multiple Redis nodes.

### Setting Up a Cluster
```sh
# Create cluster nodes
redis-server --cluster-enabled yes --cluster-config-file nodes.conf --cluster-node-timeout 5000

# Add nodes to the cluster
redis-cli --cluster create <node1>:6379 <node2>:6379 <node3>:6379 --cluster-replicas 1
```

## Resources
- [Official Redis Documentation](https://redis.io/documentation)
- [Redis GitHub Repository](https://github.com/redis/redis)
- [Redis Community](https://redis.io/community)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
Redis is released under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

---

This README provides a high-level overview of Redis, its features, and basic usage. For more detailed information, refer to the official Redis documentation and community resources.