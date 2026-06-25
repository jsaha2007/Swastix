# ??? PostgreSQL Database Connection Guide

## Where to See Your Database Connection

### **File Location**
```
C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.env
```

---

## ?? Database URL Format

Your PostgreSQL connection string looks like this:

```
DATABASE_URL=postgresql://username:password@localhost:5432/swastix_db
```

### Breaking it down:
```
postgresql://  ? Database type
username       ? Your PostgreSQL username
:              ? Separator
password       ? Your PostgreSQL password
@              ? Separator
localhost      ? Server address (local machine)
:              ? Port separator
5432           ? PostgreSQL default port
/              ? Separator
swastix_db     ? Database name
```

---

## ?? How to Configure Your Connection

### **Step 1: Open `.env` file**
```
C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.env
```

### **Step 2: Update DATABASE_URL**

Replace with your actual PostgreSQL credentials:

```
# If your PostgreSQL username is 'postgres' and password is 'mypassword':
DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/swastix_db

# If no password (local development):
DATABASE_URL=postgresql://postgres@localhost:5432/swastix_db

# If different port (e.g., 5433):
DATABASE_URL=postgresql://postgres:password@localhost:5433/swastix_db

# If remote server:
DATABASE_URL=postgresql://user:password@192.168.1.100:5432/swastix_db
```

### **Step 3: Save the file**

---

## ?? How to Find Your PostgreSQL Credentials

### **On Windows:**

#### Method 1: Using psql Command
```powershell
# Open PowerShell or Command Prompt and type:
psql -U postgres

# If this works, your username is 'postgres'
# It will ask for password - that's your PostgreSQL password
```

#### Method 2: Check PostgreSQL Installation
1. Open **Services** (services.msc)
2. Look for "postgresql-*" service
3. Right-click ? Properties
4. Note the user running the service

#### Method 3: Using pgAdmin (GUI Tool)
1. Open **pgAdmin** (comes with PostgreSQL)
2. Right-click **Servers** ? **Create** ? **Server**
3. Check the connection details

---

## ?? Example Configurations

### **Local Development (No Password)**
```
DATABASE_URL=postgresql://postgres@localhost:5432/swastix_db
```

### **Local Development (With Password)**
```
DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/swastix_db
```

### **Windows Default**
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/swastix_db
```

### **Remote Server**
```
DATABASE_URL=postgresql://username:password@192.168.1.50:5432/swastix_db
```

---

## ? How to Test Your Connection

### **Method 1: Using psql**
```bash
# Test connection
psql -U postgres -h localhost -d swastix_db

# If successful, you'll see the psql prompt: postgres=#
```

### **Method 2: Using Python**
```bash
python -c "
from database import engine
try:
    connection = engine.connect()
    print('? Database connection successful!')
    connection.close()
except Exception as e:
    print(f'? Connection failed: {e}')
"
```

### **Method 3: When Running the App**
```bash
python main.py

# If connection is good, you'll see startup messages
# If connection fails, you'll see an error in the console
```

---

## ?? Common Connection Issues

### **Issue: "Could not connect to database"**
```
? postgresql://postgres:wrong_password@localhost:5432/swastix_db

? Solution: Check your password in .env
```

### **Issue: "Database does not exist"**
```
? postgresql://postgres:password@localhost:5432/wrong_db_name

? Solution: Create database first:
   createdb swastix_db
```

### **Issue: "Connection refused"**
```
? PostgreSQL not running

? Solution: Start PostgreSQL:
   # Windows: Services ? Start PostgreSQL
   # Mac: brew services start postgresql
   # Linux: sudo systemctl start postgresql
```

### **Issue: "Port 5432 is not open"**
```
? Different port configured

? Solution: Update port in .env:
   DATABASE_URL=postgresql://user:pass@localhost:5433/swastix_db
```

---

## ?? Where Each Component Uses This

### **In Python Code**

**File**: `config.py`
```python
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/swastix_db")
```

**File**: `database.py`
```python
from config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_size=10,
    max_overflow=20,
)
```

---

## ?? Quick Reference

| Component | Location | Example |
|-----------|----------|---------|
| **Config File** | `.env` | `DATABASE_URL=postgresql://...` |
| **Config Reader** | `config.py` | `os.getenv("DATABASE_URL")` |
| **Engine Setup** | `database.py` | `create_engine(DATABASE_URL)` |
| **Models** | `models/` | Uses SQLAlchemy Base |

---

## ?? Security Tips

### **DO:**
? Use strong passwords  
? Keep `.env` out of version control  
? Use environment variables for production  
? Create separate DB users for different environments  

### **DON'T:**
? Hardcode passwords in code  
? Share `.env` files  
? Use same password everywhere  
? Store passwords in git  

---

## ?? Step-by-Step Setup

### **1. Check PostgreSQL is Running**
```bash
# Windows
net start postgresql-x64-15  # or your version

# Mac
brew services start postgresql

# Linux
sudo systemctl start postgresql
```

### **2. Create Database**
```bash
createdb swastix_db
```

### **3. Update .env**
```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/swastix_db
```

### **4. Test Connection**
```bash
python -c "from database import engine; engine.connect()"
```

### **5. Initialize Database**
```bash
python init_db.py
```

### **6. Run Application**
```bash
python main.py
```

---

## ?? Need Help?

### Check These Files
- **Setup Guide**: `PHASE1_README.md`
- **Schema Info**: `DATABASE_SCHEMA.md`
- **Troubleshooting**: `BUILD_REPORT.md`

### Quick Commands
```bash
# Verify connection
python -c "from models import User; print('? Connected')"

# Check database exists
psql -l | grep swastix_db

# List all tables
psql -U postgres -d swastix_db -c "\dt"

# Check .env is loaded
python -c "from config import DATABASE_URL; print(DATABASE_URL)"
```

---

**Now you know exactly where your PostgreSQL connection is configured!** ??

**File**: `C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.env`
