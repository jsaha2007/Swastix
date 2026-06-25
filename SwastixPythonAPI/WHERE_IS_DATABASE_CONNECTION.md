# ?? Where to See Your PostgreSQL Connection - Visual Guide

## ?? THE ANSWER: Your `.env` File!

```
Your Project Directory:
C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\

                              ?

                           .env file  ? HERE! ??

```

---

## ?? Quick View

### **Open This File:**
```
C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.env
```

### **Look for This Line:**
```
DATABASE_URL=postgresql://username:password@localhost:5432/swastix_db
```

---

## ?? Your Current Configuration

After updating, your `.env` file now contains:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/swastix_db

# Application Configuration
DEBUG=True
SECRET_KEY=your-secret-key-change-in-production

# OTP Configuration
OTP_EXPIRY_MINUTES=10
OTP_LENGTH=6

# Email Configuration (for notifications)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# SMS Configuration (Twilio or similar)
SMS_API_KEY=your-sms-api-key
SMS_SENDER=Swastix

# Application Settings
APPOINTMENT_REMINDER_HOURS=24
```

---

## ?? How to Edit It

### **Step 1: Open File**
1. Open File Explorer
2. Navigate to: `C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\`
3. Find `.env` file
4. Right-click ? **Open with** ? **Notepad** (or your editor)

### **Step 2: Find the Database Connection**
Look for the line starting with:
```
DATABASE_URL=
```

### **Step 3: Update with Your Credentials**

**Before:**
```
DATABASE_URL=postgresql://username:password@localhost:5432/swastix_db
```

**After (Example):**
```
DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/swastix_db
```

### **Step 4: Save**
Press `Ctrl + S` to save

---

## ?? What Each Part Means

```
DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/swastix_db
              ?              ?         ?           ?        ?   ?
         Database Type   Username  Password    Server    Port  Database Name
         (PostgreSQL)
```

### **Breakdown:**
- **postgresql://** - This is a PostgreSQL database
- **postgres** - Your database username
- **mypassword** - Your database password
- **localhost** - Your computer (or server address)
- **5432** - PostgreSQL's default port
- **swastix_db** - The database name

---

## ??? How to Find Your PostgreSQL Credentials

### **If You Just Installed PostgreSQL:**

Your default credentials are usually:
```
Username: postgres
Password: (whatever you set during installation)
Server: localhost
Port: 5432
Database: swastix_db (we'll create this)
```

### **Example .env Entry:**
```
DATABASE_URL=postgresql://postgres:your_password_here@localhost:5432/swastix_db
```

---

## ? Step-by-Step to Get Your Connection Working

### **1. Create the Database**
Open Command Prompt or PowerShell and run:
```bash
createdb swastix_db
```

### **2. Edit .env File**
Open: `C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.env`

Replace:
```
DATABASE_URL=postgresql://postgres:your_actual_password@localhost:5432/swastix_db
```

### **3. Test Connection**
```bash
python -c "
from database import engine
try:
    conn = engine.connect()
    print('? Connection works!')
    conn.close()
except Exception as e:
    print(f'? Error: {e}')
"
```

### **4. Initialize Database**
```bash
python init_db.py
```

---

## ?? File Location Diagram

```
SwastixPythonAPI/  (Your Project)
?
??? main.py                      ? FastAPI app
??? config.py                    ? Reads .env
??? database.py                  ? Uses DATABASE_URL
?
??? .env                         ? YOUR CONNECTION HERE! ??
?   DATABASE_URL=postgresql://...
?
??? .env.example                 ? Template (don't edit)
?   DATABASE_URL=postgresql://...
?
??? models/
?   ??? __init__.py
?   ??? patient.py
?   ??? ... (11 model files)
?
??? ... (other files)
```

---

## ?? In Code: How It's Used

### **Step 1: config.py Reads It**
```python
import os
from dotenv import load_dotenv

load_dotenv()  # ? Reads your .env file

DATABASE_URL = os.getenv("DATABASE_URL")
# Now DATABASE_URL = "postgresql://postgres:password@localhost:5432/swastix_db"
```

### **Step 2: database.py Uses It**
```python
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)  # ? Connects to your database
```

### **Step 3: Models Use the Engine**
```python
from database import Base, engine

Base.metadata.create_all(bind=engine)  # ? Creates your tables
```

---

## ?? Common Values

### **Windows (PostgreSQL Default)**
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/swastix_db
```

### **Mac (Homebrew Default)**
```
DATABASE_URL=postgresql://postgres:@localhost:5432/swastix_db
```

### **Linux (Package Manager Default)**
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/swastix_db
```

### **Remote Server**
```
DATABASE_URL=postgresql://dbuser:dbpass@192.168.1.100:5432/swastix_db
```

---

## ?? Quick Commands

```bash
# View your .env file
cat .env

# Test connection
python -c "from config import DATABASE_URL; print(DATABASE_URL)"

# Create database
createdb swastix_db

# List all databases
psql -l

# Connect to your database
psql -U postgres -d swastix_db
```

---

## ? Summary

| Question | Answer |
|----------|--------|
| **Where is the connection?** | `.env` file in your project |
| **What's the line called?** | `DATABASE_URL` |
| **Where do I edit it?** | Open `.env` with any text editor |
| **What format?** | `postgresql://user:password@host:port/dbname` |
| **How to test?** | Run `python init_db.py` |

---

## ?? You're All Set!

Now you know exactly where your PostgreSQL connection is configured:

**File**: `.env`  
**Line**: `DATABASE_URL=postgresql://...`  
**Location**: `C:\Drive D\Code\Own\Swastix\Swastrix_API\SwastixPythonAPI\SwastixPythonAPI\.env`

Just update it with your actual PostgreSQL credentials and you're ready to go! ??
