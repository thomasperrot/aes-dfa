# AES-DFA

![license](https://img.shields.io/github/license/thomasperrot/aes-dfa)
![Rust](https://img.shields.io/badge/rust-%23000000.svg?logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?&logo=python&logoColor=ffdd54)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?logo=vuedotjs)
![test working](https://github.com/thomasperrot/aes-dfa/actions/workflows/testing.yml/badge.svg)
[![codecov](https://codecov.io/github/thomasperrot/aes-dfa/graph/badge.svg?token=UL6MZ6UIXQ)](https://codecov.io/github/thomasperrot/aes-dfa)

An optimized distributed architecture to crack AES using a single fault.

## Overview

This repository contains:
* Rust code containing the main cracking algorithm, based on [this research paper](https://eprint.iacr.org/2009/575.pdf). More information in [rust/README.md](https://github.com/thomasperrot/aes-dfa/blob/master/rust/README.md)
* A Python backend running:
  * a REST API using FastAPI
  * a task queue in Redis
  * workers in Celery, which use the Rust code for maximum efficiency
* An awful frontend to submit the data to crack

![A screenshot of the app](https://raw.githubusercontent.com/thomasperrot/aes-dfa/refs/heads/master/img/img.png "Successful computation")

## Usage

You will need [Docker compose](https://docs.docker.com/compose/) to run the project. Then:
```
docker compose up
```
Then you can access the frontend at http://localhost:8080

## Contributing

### Rust

You can find more information in the rust/README.md

To run the unittests
```
cargo test
```
By default, long tests are skipped. If you want to run all tests, then run:
```
cargo test -- --include-ignored
```
To build and publish the Python package, you must run:
```
MATURIN_PYPI_TOKEN=<TOKEN> maturin publish --target release
```

### Backend

You need to have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. Then to run the unittests
```
cd backend
docker compose up redis
uv run pytest
```

### Frontend

To develop the frontend, you need to install [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm). Then you can run
```
npm run dev
```

