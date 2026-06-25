#!/usr/bin/env python
"""
Swastix Build & Verification Script
Verifies all components and builds the application
"""

import os
import sys
import subprocess
from pathlib import Path

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text):
    """Print header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{Colors.ENDC}\n")


def print_success(text):
    """Print success message"""
    print(f"{Colors.OKGREEN}? {text}{Colors.ENDC}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.FAIL}? {text}{Colors.ENDC}")


def print_warning(text):
    """Print warning message"""
    print(f"{Colors.WARNING}??  {text}{Colors.ENDC}")


def print_info(text):
    """Print info message"""
    print(f"{Colors.OKCYAN}??  {text}{Colors.ENDC}")


def check_python():
    """Check Python version"""
    print_header("Checking Python Version")

    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"

    if version.major >= 3 and version.minor >= 8:
        print_success(f"Python {version_str} installed")
        return True
    else:
        print_error(f"Python 3.8+ required. Found {version_str}")
        return False


def check_files():
    """Check if all required files exist"""
    print_header("Checking Required Files")

    required_files = [
        "config.py",
        "database.py",
        "init_db.py",
        "main.py",
        "requirements.txt",
        ".env.example",
        "models/__init__.py",
        "models/otp.py",
        "models/patient.py",
        "models/doctor.py",
        "models/timeslot.py",
        "models/appointment.py",
        "models/prescription.py",
        "models/medical_document.py",
        "models/rating.py",
        "models/admin.py",
        "models/notification.py",
    ]

    all_exist = True
    for file in required_files:
        file_path = Path(file)
        if file_path.exists():
            print_success(f"Found: {file}")
        else:
            print_error(f"Missing: {file}")
            all_exist = False

    return all_exist


def check_imports():
    """Check if all modules can be imported"""
    print_header("Checking Module Imports")

    modules = [
        ("config", "Configuration module"),
        ("database", "Database module"),
        ("models", "Models module"),
    ]

    all_ok = True
    for module, description in modules:
        try:
            __import__(module)
            print_success(f"{description} ({module}) - OK")
        except ImportError as e:
            print_error(f"{description} ({module}) - FAILED: {e}")
            all_ok = False

    return all_ok


def check_dependencies():
    """Check if all dependencies are installed"""
    print_header("Checking Dependencies")

    dependencies = [
        "sqlalchemy",
        "psycopg2",
        "pydantic",
        "python_dotenv",
        "uvicorn",
        "fastapi",
    ]

    all_ok = True
    for dep in dependencies:
        try:
            __import__(dep)
            print_success(f"{dep} - installed")
        except ImportError:
            print_warning(f"{dep} - not installed")
            all_ok = False

    return all_ok


def compile_python_files():
    """Compile all Python files"""
    print_header("Compiling Python Files")

    py_files = [
        "config.py",
        "database.py",
        "init_db.py",
        "main.py",
        "models/__init__.py",
        "models/otp.py",
        "models/patient.py",
        "models/doctor.py",
        "models/timeslot.py",
        "models/appointment.py",
        "models/prescription.py",
        "models/medical_document.py",
        "models/rating.py",
        "models/admin.py",
        "models/notification.py",
    ]

    all_ok = True
    for py_file in py_files:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", py_file],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print_success(f"Compiled: {py_file}")
        else:
            print_error(f"Failed to compile: {py_file}")
            print(f"  Error: {result.stderr}")
            all_ok = False

    return all_ok


def verify_database_schema():
    """Verify database schema"""
    print_header("Verifying Database Schema")

    try:
        from models import (
            User, RoleEnum,
            OTP,
            Patient,
            Doctor, DoctorSpecialty,
            Timeslot, TimeslotStatus,
            Appointment, AppointmentStatus, ConsultationType,
            Prescription,
            MedicalDocument, DocumentType,
            Rating,
            Admin,
            Notification, NotificationType
        )

        print_success("All 11 database models loaded successfully")

        # Count columns
        models_info = [
            ("User", User),
            ("Patient", Patient),
            ("Doctor", Doctor),
            ("Timeslot", Timeslot),
            ("Appointment", Appointment),
            ("Prescription", Prescription),
            ("MedicalDocument", MedicalDocument),
            ("Rating", Rating),
            ("Admin", Admin),
            ("OTP", OTP),
            ("Notification", Notification),
        ]

        total_columns = 0
        for model_name, model_class in models_info:
            columns = len(model_class.__table__.columns)
            total_columns += columns
            print_info(f"{model_name}: {columns} columns")

        print_success(f"Total: {total_columns} columns across all models")
        return True

    except Exception as e:
        print_error(f"Failed to verify schema: {e}")
        return False


def print_build_summary(results):
    """Print build summary"""
    print_header("Build Summary")

    checks = [
        ("Python Version", results.get("python", False)),
        ("Required Files", results.get("files", False)),
        ("Module Imports", results.get("imports", False)),
        ("Dependencies", results.get("dependencies", False)),
        ("Python Compilation", results.get("compile", False)),
        ("Database Schema", results.get("schema", False)),
    ]

    passed = sum(1 for _, result in checks if result)
    total = len(checks)

    print(f"\nTotal: {passed}/{total} checks passed\n")

    for check_name, result in checks:
        status = "? PASS" if result else "? FAIL"
        print(f"  {check_name}: {status}")

    if passed == total:
        print(f"\n{Colors.OKGREEN}{Colors.BOLD}?? Build Successful!{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Ready to run: python main.py{Colors.ENDC}\n")
        return True
    else:
        print(f"\n{Colors.FAIL}{Colors.BOLD}??  Build has issues{Colors.ENDC}")
        print(f"{Colors.WARNING}Fix the above errors and run build again{Colors.ENDC}\n")
        return False


def main():
    """Main build function"""
    print_header("?? Swastix Doctor Booking System - Build")

    results = {}

    # Run all checks
    results["python"] = check_python()
    results["files"] = check_files()
    results["imports"] = check_imports()
    results["dependencies"] = check_dependencies()
    results["compile"] = compile_python_files()
    results["schema"] = verify_database_schema()

    # Print summary
    success = print_build_summary(results)

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
