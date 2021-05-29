  <h3 align="center">Crypto Price Tracker</h3>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#technologies">Technologies</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


## About

I wanted to start logging various crypto prices on a regular cadence. This tool was created specificaly for me, but could be customized easily for your own use case.

It currently tracks the prices for:
* Ethereum
* Polygon

### Technologies

* Python
* MySQL
* [SqlAlchemy ORM](https://docs.sqlalchemy.org/en/14/)
* [Kraken Public API](https://docs.kraken.com/rest/)

## Getting Started

To get this running for your own use you'll need to set up a few things. 
* You'll need to know how to set up a database and access to it.
* Have a modern version of Python installed

### Prerequisites

* MySQL
  * Create a mysql database if you don't want to modify the code.

```sh
sudo mysql -p
```
  ```sql
  create database some_database;
  create 'some_user'@'%' identified by 'some_password';
  grant all privileges on some_database.* TO 'some_user'@'%';
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/zackoch/crypto_tracker.git
   ```
2. Create a virtual environment
   ```sh
   cd crypto_tracker && python3 -m venv venv
   ```
3. Install required packages via pip
   ```sh
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Modify environment variables 
    ```sh
    mv sample.env .env
    nano .env
    ```
    replace `some_user`, `some_password`, `host`, and `some_database` to match the database and user you created in the prerequisites

    ```sh
    DB_CON_STRING='mysql+pymysql://some_user:some_password@host/some_database'
    ```
5. Create the tables
    ```sh
    python
    ```
    ```python
    from models import *
    Base.metadata.create_all()
    ```

## Usage
 
* You can call the script directly which will insert the data into your db one time (useful to test)
    ```sh
    source venv/bin/activate
    python main.py
    ```
OR

* You can schedule it as a cronjob to run at a specific time / cadence
    ```sh

    ```
