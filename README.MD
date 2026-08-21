e_commerce3
![Preview](screen.jpg)


## ✨ Key Features

This GitHub repository is a **PyCharm** project developed to practice full-stack development.
Unlike e_commerce3, this project can be run normally or **containerized via Docker**.

<font color="#5f7824">More importantly, once you confirm this project working as anticipated, the codes of this repository can serve you a sound working code that can be changed as any one wishes.</font>

The core technologies and APIs used include:

* **Python**-based backend
* **FastAPI** framework
* **PostgreSQL** database
* **RESTful API** communication between Frontend and Backend
* **Docker**

While it is not a commercial-grade application, it is highly complete and allows you to test the project using your own database consisting of 5 tables (See `e_commerce3_models.pptx` for a full description).

You can explore the detailed structures of the tables, columns, and relationships in the project files (see below to clone and set up the project).

## ⚙️ Installation and Configuration

If you need help cloning the repository into PyCharm, please refer to this guide:
[How to create a project folder in PyCharm with a GitHub repository](https://www.google.com/search?q=how+to+create+project+folder+in+pycharm+with+a+github+repository)

If you encounter any issues, feel free to contact me at smlee@inha.ac.kr.

### Prerequisites
Before proceeding, make sure you have **PyCharm** and **PostgreSQL** installed on your PC. Then, follow these two steps:

1. Open the Terminal in PyCharm and run the following command to install all required libraries:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a file named `.env` in the project root folder and paste the following line:

   ```env
   DATABASE_URL=postgresql+psycopg2://postgres:{your_password}@localhost:5432/e_commerce_db
   ```
   *Note: This file is required for the project to run. Replace `{your_password}` with the password you set during PostgreSQL installation.*

## 🧩 Running the Cloned Project: #1 Normal way

With Docker installed in your PC, you can run one of two ways: the normal way and another way in containers.

To start the backend server, open the Terminal and run:

```bash
uvicorn app.main:app --reload
```

Once you see `"Application startup complete."` at the end of the log, your backend server is ready. The server runs on the default port `8000`.

### Accessing the Project
You can access the project in your browser using two different URLs:

1. **Frontend / Main Interface**

```
http://127.0.0.1:8000
```

*The page will display the main dashboard screen, likely showing all 0s initially.*

2. **FastAPI Interactive Docs (API Endpoints)**

```
http://127.0.0.1:8000/docs
```

*This page displays the interactive FastAPI endpoints. Below you will find the way to generate and add data to database.*


## 🧩 Running the Cloned Project: #2 Another way in containers

Comment the content of the file named `.env` mentioned above and paste the following lines:

```env
DATABASE_URL=postgresql+psycopg2://postgres:{your_password}@db:5432/db_docker
POSTGRES_USER=postgres
POSTGRES_PASSWORD={your_password}
POSTGRES_DB=db_docker
```
*Note: This file is required for the project to be dockerized. Replace `{your_password}` with the password you set during PostgreSQL installation.*

*Note: Although the same POSTGRES_DB name is used, the actual DB inside dockerized project is totally separated from the one in your local PC. Ask your favorite AI for the details.*

To start the backend server, open the Terminal and run AFTER running Docker Desktop:

```bash
docker compose up --build
```

Once you see `"Application startup complete."` at the end of the log, your backend server is ready. The server runs on the default port `8000` like the normal way.


## 🗄️ How to Generate Initial Data

1. Open the swagger UI for the FastAPI endpoints with the address below: 

```
http://127.0.0.1:8000/docs
```

2. You will find 2 administrative POST endpoints, POST /admin/recreate_tables and POST /admin/generate_add_data, as well as others.
3. If you click the button of the first endpoint, the button "Try it out", and the button "Execute", it drops all existing tables and creates them fresh from the metadata.
4. If you click the button of the second endpoint and the button "Try it out", a box of Edit Value will be waiting for your input. You need to provide the integer values of customer_count, product_count, order_count, and city_count at the designated areas. The product_count is a tuple of 2 integers; the first one is for the categories, and the second one is for the products of each category.
5. If you click the button of "Execute" after editing the integer values, it generate data and add them to the tables.
6. Use another tab to open frontend webpage with the address below:

```
http://127.0.0.1:8000
```

7. You will see the key performance indicators and 3 different graphs for the data you have generated a moment ago.


## 📄 License
MIT License - free for personal and commercial use.
---
Made to be cloned and run instantly. If you get the same screen as `screen.jpg`, setup succeeded.
