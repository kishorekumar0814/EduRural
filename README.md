# 🌱 EduRural – Digital Learning Platform for Rural School Students  

EduRural is a **web-based learning platform** designed to make quality education accessible to **rural students**.  
It provides an easy-to-use interface for interactive courses such as **Mathematics, Science, and English**, with a vision to bridge the educational gap using modern web technologies and cloud deployment.  

---

## 🚀 Project Overview  

This project demonstrates a **complete cloud deployment pipeline** for a Flask web application using **Docker** and **Kubernetes** on **AWS EC2**.  

**Workflow Overview:**  
1. Developed a web application using **HTML, CSS, JavaScript, and Flask (Python)**.  
2. Pushed the project source code to **GitHub**.  
3. Created an **AWS EC2 instance (Ubuntu)** and connected via **SSH** using a `.pem` key.  
4. Cloned the project from GitHub and **built a Docker image** locally on EC2.  
5. **Deployed the containerized app** using **Docker** and **Kubernetes**.  
6. Accessed the running application using **Public IP, Public DNS, and Private IP** of the EC2 instance.  

---

## 🏧️ Architecture  

```
WebApp (HTML, CSS, JS, Flask)
        ↓
GitHub Repository
        ↓
AWS EC2 (Ubuntu Instance)
        ↓
Docker (Containerized EduRural App)
        ↓
Kubernetes (Deployment & Management)
        ↓
WebApp accessible via Public IP / Public DNS / Private IP
```

---

## ⚙️ Technologies Used  

| Category | Technology |
|-----------|-------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Cloud Platform | AWS EC2 (Ubuntu) |
| Version Control | Git & GitHub |
| Firewall | UFW (Uncomplicated Firewall) |
| Package Manager | pip |
| Others | Gunicorn (optional), Flask-SQLAlchemy |

---

## 🧩 Project Structure  

```
EduRural/
│
├── static/                   # CSS, JS, and image files
├── templates/                # HTML templates
├── app.py                    # Flask main application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker build instructions
├── kubernetes-deployment.yaml # Kubernetes deployment configuration
├── README.md                 # Project documentation
└── .gitignore                # Ignored files
```

---

## 🛣️ Docker Setup  

### Step 1: Build Docker Image  
```bash
docker build -t edurural:latest .
```

### Step 2: Run Docker Container  
```bash
docker run -d -p 5000:5000 edurural:latest
```

### Step 3: Check Running Containers  
```bash
docker ps
```

---

## ☸️ Kubernetes Deployment  

### Step 1: Create Deployment & Service  
```bash
kubectl apply -f kubernetes-deployment.yaml
```

### Step 2: Check Pods & Services  
```bash
kubectl get pods
kubectl get svc
```

### Step 3: Access Application  
Use the **Public IP / DNS** of your EC2 instance on port `5000`:  
```
http://<EC2-PUBLIC-IP>:5000/
```

---

## 🔑 AWS EC2 Setup  

1. Launch an **EC2 Instance** (Ubuntu).  
2. Configure **Security Group**:  
   - Allow inbound traffic for ports `22 (SSH)` and `5000 (Flask/Docker app)`.  
3. Connect via SSH:  
   ```bash
   ssh -i "your-key.pem" ubuntu@<public-dns>
   ```
4. Install required packages:  
   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo apt install python3-pip -y
   sudo apt install kubectl -y
   ```

---

## 🧠 Future Enhancements  

- Add **student authentication & profiles**.  
- Integrate **AI-based personalized learning** modules.  
- Deploy a **managed Kubernetes cluster (EKS)**.  
- Enable **CI/CD pipeline** with GitHub Actions.  
- Include **analytics dashboard** for tracking progress.  

---

## 💡 Key Learnings  

- Hands-on experience with **Docker & Kubernetes** on AWS.  
- Understanding of **Flask backend integration** with cloud infrastructure.  
- Building a **scalable and containerized web application**.  
- Deploying a project from **local development to cloud production**.

---

## 📸 Architecture Diagram  

![EduRural Architecture]<img width="817" height="262" alt="image" src="https://github.com/user-attachments/assets/88aacd44-05e6-4089-b6c9-bcd3de0dda22" />


---

## 🧑‍💻 Author  

**Kishore Kumar S**  
🎓 M.Tech in Computer Science & Engineering  
📍 Vellore Institute of Technology  
💼 Aspiring Machine Learning & Cloud Engineer  
📧 Email: kishorekumarofficial1409@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/kishorekumars) | [GitHub](https://github.com/kishore1409)  

---

## 💚 License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

