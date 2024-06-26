# Cache Replacement Policies

Welcome to the Cache Replacement Policies repository! This repository contains Python scripts demonstrating various cache replacement policies, including FIFO, LIFO, LRU, MRU, and LFU. Each script is designed to help you understand how these policies work and how to implement them in Python.

## Table of Contents

- [Introduction](#introduction)
- [Cache Replacement Policies](#cache-replacement-policies)
  - [FIFO (First In First Out)](#fifo-first-in-first-out)
  - [LIFO (Last In First Out)](#lifo-last-in-first-out)
  - [LRU (Least Recently Used)](#lru-least-recently-used)
  - [MRU (Most Recently Used)](#mru-most-recently-used)
  - [LFU (Least Frequently Used)](#lfu-least-frequently-used)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Cache replacement policies determine how cache entries are managed and replaced. This repository provides Python scripts that implement and demonstrate the following cache replacement policies:

1. FIFO (First In First Out)
2. LIFO (Last In First Out)
3. LRU (Least Recently Used)
4. MRU (Most Recently Used)
5. LFU (Least Frequently Used)

## Cache Replacement Policies

### FIFO (First In First Out)

The FIFO policy evicts the oldest cache entry first. This policy is simple and straightforward but does not consider the frequency or recency of access.

- **Script**: `1-fifo_cache.py`
- **Usage**: Demonstrates how to implement and use the FIFO cache replacement policy.

### LIFO (Last In First Out)

The LIFO policy evicts the most recently added cache entry first. This policy is the opposite of FIFO and is useful in certain scenarios where the most recent entry is less likely to be used again.

- **Script**: `lifo_cache.py`
- **Usage**: Demonstrates how to implement and use the LIFO cache replacement policy.

### LRU (Least Recently Used)

The LRU policy evicts the least recently used cache entry first. This policy ensures that frequently accessed entries remain in the cache.

- **Script**: `lru_cache.py`
- **Usage**: Demonstrates how to implement and use the LRU cache replacement policy.

### MRU (Most Recently Used)

The MRU policy evicts the most recently used cache entry first. This policy is useful in scenarios where the most recent entry is less likely to be reused soon.

- **Script**: `mru_cache.py`
- **Usage**: Demonstrates how to implement and use the MRU cache replacement policy.

### LFU (Least Frequently Used)

The LFU policy evicts the least frequently used cache entry first. This policy ensures that entries accessed more frequently remain in the cache.

- **Script**: `lfu_cache.py`
- **Usage**: Demonstrates how to implement and use the LFU cache replacement policy.

## Getting Started

Follow the instructions below to get a copy of the scripts up and running on your local machine.

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdelrahman21-arch/alx-backend.git
   cd alx-backend/0x01-caching
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install any necessary dependencies (if applicable):

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Navigate to the desired script folder:

   ```bash
   cd 0x01-caching  # or lifo_cache, lru_cache, mru_cache, lfu_cache
   ```

2. Run the script:

   ```bash
   python 1-fifo_cache.py  # or lifo_cache.py, lru_cache.py, mru_cache.py, lfu_cache.py
   ```

3. Follow the instructions in each script to understand how the cache replacement policy works.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy caching!

---

Feel free to customize this README file according to your specific needs and project details. If you have any questions or need further assistance, don't hesitate to reach out.