# Predictive Maintenance for Cold Chain Logistics

This repository implements a predictive maintenance solution for **10 reefer trucks** using a **hybrid LSTM + Random Forest** model. The system simulates real-time sensor data via **Kafka**, processes it with a **Flask** backend connected to a **free-tier AWS database**, and displays a user-friendly **React** dashboard.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Project Structure](#project-structure)  
3. [Set Up a Free AWS Database](#set-up-a-free-aws-database)  
4. [Configuration Placeholders](#configuration-placeholders)  
5. [Step-by-Step Setup in PyCharm (Windows)](#step-by-step-setup-in-pycharm-windows)  
6. [How to Run](#how-to-run)  
7. [Troubleshooting](#troubleshooting)  

---

## Prerequisites

- **Windows OS**  
- **Python 3.8+** installed  
- **PyCharm** (Community or Professional)  
- **Node.js** (for the frontend, if you plan to run the React app locally)  
- **Docker** (optional, if you want to run Kafka and services in containers)  
- **Git** (optional, to clone the repository directly)  
- **AWS Account** with access to the free-tier RDS (PostgreSQL or MySQL)

---

## Project Structure

```
predictive_maintenance_project/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── kafka/
│   └── data_simulator.py
├── model/
│   ├── hybrid_model.py
│   ├── train_model.py
│   └── utils.py
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       └── components/
│           ├── Dashboard.js
│           └── TruckCard.js
└── docs/
    └── project_plan.md
```

- **kafka/** – Contains a data simulator script for generating reefer truck sensor data.  
- **model/** – Hybrid LSTM + Random Forest model training scripts.  
- **backend/** – Flask API connecting to AWS database and hosting prediction endpoints.  
- **frontend/** – React dashboard for real-time monitoring and alerts.  
- **docker-compose.yml** – Docker Compose file to spin up Kafka, Zookeeper, backend, and optionally the frontend.

---

## Set Up a Free AWS Database

Below is a high-level guide to creating a **PostgreSQL** database on AWS RDS (you can also choose MySQL if you prefer, as long as you update your connection details accordingly).

1. **Create an AWS Account**  
   - Go to [aws.amazon.com](https://aws.amazon.com/) and follow the steps to create an account. You may need a credit card, but the free tier will not charge you if you stay within limits.

2. **Open the RDS Console**  
   - Once logged in, search for **“RDS”** in the AWS Console.

3. **Create a Database**  
   - Click **Create database**.  
   - Choose **Standard create**.  
   - Engine options: **PostgreSQL** (or MySQL).  
   - **Templates**: Select **Free tier**.  
   - Give your database an **Identifier** (e.g., `predictive_db`).  
   - **Master username** and **password**: Choose something you’ll remember.

4. **Instance Configuration**  
   - Choose the free-tier-eligible instance size (e.g., `db.t2.micro` or `db.t3.micro`).  
   - Storage: 20GB (default free-tier).  
   - Public access: **Yes** (to connect from your local machine).  
   - VPC security group: **Create or select** a security group that allows inbound traffic from your IP address on the DB port (default: 5432 for PostgreSQL).

5. **Wait for the DB to Launch**  
   - AWS will provision your RDS instance. This can take a few minutes.  
   - Once available, note the **Endpoint** (something like `predictive_db.abc123.us-east-1.rds.amazonaws.com`).

6. **Test Connection** (Optional)  
   - Use a client like **pgAdmin** (for PostgreSQL) or MySQL Workbench (for MySQL).  
   - Confirm you can connect with the endpoint, username, and password.

7. **Add a Table (Optional)**  
   - If your application requires specific tables, run the relevant SQL scripts or connect from the Python code to create tables automatically.

**Important:** The free tier has monthly usage limits. Monitor your usage in the AWS Billing Dashboard to avoid charges.

---

## Configuration Placeholders

1. **`backend/config.py`**  
   ```python
   class Config:
       DEBUG = True
       # AWS Database configuration (replace with your free-tier AWS DB settings)
       DB_HOST = os.environ.get("AWS_DB_HOST", "your-db-host.amazonaws.com")
       DB_PORT = os.environ.get("AWS_DB_PORT", "5432")
       DB_NAME = os.environ.get("AWS_DB_NAME", "predictive_db")
       DB_USER = os.environ.get("AWS_DB_USER", "dbuser")
       DB_PASSWORD = os.environ.get("AWS_DB_PASSWORD", "dbpassword")
   ```
   - **`DB_HOST`**: Replace `"your-db-host.amazonaws.com"` with your **RDS endpoint** (e.g., `predictive_db.abc123.us-east-1.rds.amazonaws.com`).  
   - **`DB_NAME`**: Replace `"predictive_db"` with the database name you set in RDS.  
   - **`DB_USER`**: Replace `"dbuser"` with the username you created.  
   - **`DB_PASSWORD`**: Replace `"dbpassword"` with your actual password.

2. **`docker-compose.yml`** (If using Docker)  
   - Ensure ports like `9092`, `5000`, `3000` are free on your machine.  
   - Update service definitions if you need to change container names or images.

3. **Kafka Broker Configuration**  
   - In `kafka/data_simulator.py`, confirm `KAFKA_BROKER = 'localhost:9092'` (if you are running Kafka locally).  
   - If you use Docker, ensure the Kafka container is accessible at `localhost:9092`.

4. **Model Save Paths**  
   - The LSTM and Random Forest models are saved to `model_lstm.h5` and `model_rf.pkl`. Make sure the file paths in `backend/app.py` and `model/train_model.py` match your environment.

---

## Step-by-Step Setup in PyCharm (Windows)

1. **Download/Clone the Project**  
   - If you have Git, open a terminal and run:  
     ```bash
     git clone <repository-url>
     ```  
     Otherwise, download the ZIP file from your repository, unzip it, and note the folder location.

2. **Open in PyCharm**  
   - Launch PyCharm.  
   - Click **File** > **Open** and select the `predictive_maintenance_project` folder.

3. **Create a Python Interpreter**  
   - In PyCharm, go to **File** > **Settings** > **Project: [Project Name]** > **Python Interpreter**.  
   - Click the gear icon, then **Add**.  
   - Choose **Virtualenv** or **Conda**, select Python 3.8+ as the base.  
   - Confirm to create a new virtual environment.

4. **Install Python Dependencies**  
   - In the PyCharm terminal (bottom pane), run:  
     ```bash
     pip install -r requirements.txt
     ```  
   - Then navigate to `backend` and install the backend requirements as well:  
     ```bash
     cd backend
     pip install -r requirements.txt
     cd ..
     ```

5. **Adjust Configuration Placeholders**  
   - Open **`backend/config.py`** and replace the placeholder AWS credentials (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`) with your real RDS endpoint, database name, username, and password.

6. **Node.js (for the Frontend)**  
   - If you want to run the React app, install **Node.js** (version 14+ recommended).  
   - In a separate terminal, navigate to the `frontend` folder:  
     ```bash
     cd frontend
     npm install
     ```

7. **Optional: Docker Setup**  
   - If you prefer to run Kafka and the entire stack via Docker, install **Docker Desktop** for Windows.  
   - In PyCharm’s terminal (or any terminal), run:  
     ```bash
     docker-compose up
     ```  
   - This should start Zookeeper, Kafka, the backend, and the frontend if configured.

---

## How to Run

### 1. Train the Model

1. In PyCharm’s **Project** panel, right-click on `model/train_model.py` and select **Run**.  
2. This script creates two files: `model_lstm.h5` and `model_rf.pkl` in the `model` folder.

### 2. Run the Flask Backend

1. Right-click on `backend/app.py` and choose **Run**.  
2. The Flask server should start at `http://localhost:5000`.

### 3. Start the Kafka Data Simulator

1. Right-click on `kafka/data_simulator.py` and choose **Run**.  
2. It will continuously generate random sensor data for 10 reefer trucks and send them to Kafka (at `localhost:9092` by default).

### 4. Launch the Frontend (React)

1. Open a new terminal in PyCharm or Windows.  
2. Navigate to the `frontend` folder:  
   ```bash
   cd frontend
   npm start
   ```  
3. The React app typically starts on `http://localhost:3000`.  
4. You should see a dashboard displaying reefer trucks’ data. For the exact UI style from your reference images, further customize the components in `frontend/src/components`.

---

## Troubleshooting

1. **Port Conflicts**  
   - If you get errors that a port is in use, change the port in `docker-compose.yml` or in the code. For example, set `port=5001` in `backend/app.py` if `5000` is unavailable.

2. **AWS DB Connection Fails**  
   - Double-check your AWS DB credentials in `backend/config.py`.  
   - Ensure your local machine’s IP is allowed in the RDS security group. (In the RDS console, go to **Databases** > **YourDB** > **Connectivity & security** and edit the inbound rules for the associated security group.)

3. **Kafka Broker Unreachable**  
   - If `kafka/data_simulator.py` can’t connect to `localhost:9092`, confirm Kafka is running (either via Docker Compose or a local Kafka installation).  
   - Update `KAFKA_BROKER` in `data_simulator.py` if using a different host/port.

4. **Node.js or NPM Errors**  
   - Make sure you installed Node.js properly.  
   - If you see missing modules, run `npm install` again in the `frontend` folder.

5. **PyCharm Interpreter Issues**  
   - Verify you selected the correct Python interpreter under **File** > **Settings** > **Project** > **Python Interpreter**.

---

**That’s it!** Once you’ve configured everything, you can run the project end-to-end in PyCharm on Windows, using your **free-tier AWS database** to store reefer truck data. If you’re new to Python, Kafka, or Docker, don’t hesitate to look for additional tutorials on how to manage these tools in more detail.

For further questions or help, feel free to reach out or open an issue in the repository.  

**Enjoy your Predictive Maintenance project for Cold Chain Logistics!**
