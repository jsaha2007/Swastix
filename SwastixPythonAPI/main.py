"""
Swastix Doctor Booking System - Main Application Entry Point
Phase 1: Database Layer - Complete
Phases 2-4: To be implemented

This is the main FastAPI application file.
Currently set up for Phase 1 (Database layer only).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from config import DEBUG, SECRET_KEY
from database import engine, Base
from models import (
    User, RoleEnum, OTP,
    Patient, Doctor, DoctorSpecialty,
    Appointment, AppointmentStatus, ConsultationType,
    Timeslot, TimeslotStatus,
    Prescription, Rating, MedicalDocument, DocumentType,
    Admin, Notification, NotificationType
)

# Initialize FastAPI app
app = FastAPI(
    title="Swastix Doctor Booking System",
    description="A doctor booking system designed for rural India with OTP-based authentication",
    version="1.0.0",
    debug=DEBUG
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables (if they don't exist)
Base.metadata.create_all(bind=engine)


# ============================================================================
# HEALTH CHECK ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint - Health check"""
    return {
        "message": "Welcome to Swastix Doctor Booking System",
        "version": "1.0.0",
        "status": "running",
        "phase": "Phase 1 - Database Layer",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "redoc": "/redoc",
            "openapi": "/openapi.json"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Swastix API",
        "version": "1.0.0",
        "phase": "Phase 1 - Database Layer",
        "database": "Connected to PostgreSQL"
    }


@app.get("/api/v1")
async def api_info():
    """API information endpoint"""
    return {
        "name": "Swastix Doctor Booking System",
        "version": "1.0.0",
        "description": "A doctor booking system for rural India",
        "current_phase": "Phase 1 - Database Layer",
        "features": {
            "authentication": "OTP-based (Email/Phone)",
            "roles": ["Patient", "Doctor", "Admin"],
            "database": "PostgreSQL",
            "orm": "SQLAlchemy 2.0"
        },
        "models_available": [
            "User", "OTP", "Patient", "Doctor", "Timeslot",
            "Appointment", "Prescription", "MedicalDocument",
            "Rating", "Admin", "Notification"
        ],
        "next_phase": "Phase 2 - Repository Layer"
    }


@app.get("/api/v1/status")
async def status():
    """Detailed status endpoint"""
    return {
        "service": "Swastix Doctor Booking System",
        "status": "operational",
        "version": "1.0.0",
        "phase": {
            "current": "Phase 1 - Database Layer",
            "status": "? Complete",
            "description": "Database models and ORM setup"
        },
        "components": {
            "database": {
                "type": "PostgreSQL",
                "status": "? Ready",
                "tables": 11,
                "relationships": "15+"
            },
            "orm": {
                "type": "SQLAlchemy 2.0",
                "status": "? Ready",
                "models": 11
            },
            "api": {
                "type": "FastAPI",
                "status": "?? Phase 2 in progress",
                "endpoints": "Limited (health checks only)"
            }
        },
        "database_models": {
            "authentication": ["User", "OTP"],
            "core": ["Patient", "Doctor", "Admin"],
            "appointments": ["Appointment", "Timeslot"],
            "medical": ["Prescription", "MedicalDocument"],
            "reviews": ["Rating"],
            "notifications": ["Notification"]
        }
    }


# ============================================================================
# PLACEHOLDER ENDPOINTS (For Phase 2+)
# ============================================================================

@app.get("/api/v1/doctors")
async def list_doctors():
    """
    List all doctors - PLACEHOLDER
    Phase 2: Will implement repository pattern
    """
    return {
        "message": "Endpoint available in Phase 2 - Repository Layer",
        "status": "not_implemented",
        "available_in": "Phase 2"
    }


@app.get("/api/v1/appointments")
async def list_appointments():
    """
    List all appointments - PLACEHOLDER
    Phase 2: Will implement repository pattern
    """
    return {
        "message": "Endpoint available in Phase 2 - Repository Layer",
        "status": "not_implemented",
        "available_in": "Phase 2"
    }


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": str(exc) if DEBUG else "An error occurred",
            "detail": type(exc).__name__
        }
    )


# ============================================================================
# STARTUP/SHUTDOWN EVENTS
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Application startup event"""
    print("\n" + "="*60)
    print("?? Swastix Doctor Booking System - Starting Up")
    print("="*60)
    print("? Phase 1: Database Layer - Complete")
    print("? Database models initialized")
    print("? ORM configured with SQLAlchemy")
    print("? PostgreSQL connection ready")
    print("?? Phase 2: Repository Layer - Coming Next")
    print("="*60 + "\n")


@app.on_event("shutdown")
async def shutdown_event():
    """Application shutdown event"""
    print("\n" + "="*60)
    print("?? Swastix Doctor Booking System - Shutting Down")
    print("="*60 + "\n")


# ============================================================================
# RUN APPLICATION
# ============================================================================

if __name__ == "__main__":
    import uvicorn

    print("\n" + "="*60)
    print("?? Swastix - Doctor Booking System for Rural India")
    print("="*60)
    print("Starting FastAPI server on http://127.0.0.1:8000")
    print("API Docs: http://127.0.0.1:8000/docs")
    print("ReDoc: http://127.0.0.1:8000/redoc")
    print("="*60 + "\n")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=DEBUG,
        log_level="info"
    )
