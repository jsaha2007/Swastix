#!/bin/bash
# Setup script for Swastix database (Linux/Mac)

echo ""
echo "========================================"
echo "Swastix - Database Setup"
echo "========================================"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Initialize database
echo "Initializing database..."
python init_db.py

echo ""
echo "========================================"
echo "? Setup complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Update .env file with your database credentials"
echo "2. Run: python init_db.py (to create tables)"
echo "3. Start development with: uvicorn main:app --reload"
echo ""
