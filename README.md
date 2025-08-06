# AES-DFA
[!codecov](https://codecov.io/github/thomasperrot/aes-dfa/graph/badge.svg?token=UL6MZ6UIXQ)](https://codecov.io/github/thomasperrot/aes-dfa)
![test working](https://github.com/thomasperrot/aes-dfa/actions/workflows/testing.yml/badge.svg)

An optimized distributed architecture to crack AES using a single fault.

## Overview

This repository contains:
* Rust code containing the main cracking algorithm, based on [this research paper](https://eprint.iacr.org/2009/575.pdf)
* A Python backend running:
  * a REST API using FastAPI
  * a task queue in Redis
  * workers in Celery
* An awful frontend to submit the data to crack

## Usage

You will need [Docker compose](https://docs.docker.com/compose/) to run the project. Then:
```
docker compose up
```
Then you can access the frontend at http://localhost:8080

## Contributing

TODO