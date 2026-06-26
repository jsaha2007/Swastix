# Swastix Database Schema Documentation

## Overview
This document describes the database schema for the Swastix doctor booking system.

## Tables

### 1. Users (`users`)
Base table for all users (Patient, Doctor, Admin)
- `id`: Primary key
- `email`: Unique email address
- `phone`: Unique phone number
- `role`: PATIENT, DOCTOR, or ADMIN
- `is_active`: Whether user is active
- `is_verified`: Whether email/phone is verified via OTP
- `created_at`, `updated_at`: Timestamps

### 2. OTP (`otps`)
One-Time Password for email and phone verification
- `id`: Primary key
- `email`: Email to verify (optional)
- `phone`: Phone to verify (optional)
- `otp_code`: The OTP code
- `is_used`: Whether OTP has been used
- `expires_at`: When OTP expires
- `verified_at`: When OTP was verified

### 3. Patients (`patients`)
Patient profile information
- `id`: Primary key
- `user_id`: Foreign key to users
- `first_name`, `last_name`: Patient name
- `date_of_birth`: DOB
- `gender`: Gender
- `address`, `city`, `state`, `postal_code`: Address
- `medical_history`: Medical history (text/JSON)
- `allergies`: Allergies info
- `blood_group`: Blood group
- `consent_sms`, `consent_email`: Communication preferences
- `profile_picture_url`: Profile picture

### 4. Doctors (`doctors`)
Doctor profile and professional information
- `id`: Primary key
- `user_id`: Foreign key to users
- `first_name`, `last_name`: Doctor name
- `specialization`: Medical specialty (enum)
- `qualification`: Degrees and certifications
- `license_number`: Medical license
- `years_of_experience`: Years in practice
- `bio`: Doctor bio
- `address`, `city`, `state`, `postal_code`: Address
- `consultation_fee`: Fee in INR
- `consultation_duration_minutes`: Duration of consultation
- `profile_picture_url`: Profile picture
- `resume_url`: Resume/CV
- `is_approved`: Admin approval status
- `is_active`: Whether doctor is active
- `average_rating`: Average rating (1-5)
- `total_ratings`: Total number of ratings

### 5. Timeslots (`timeslots`)
Doctor availability timeslots
- `id`: Primary key
- `doctor_id`: Foreign key to doctors
- `slot_date`: Date of the slot
- `start_time`, `end_time`: Time range
- `status`: AVAILABLE, BOOKED, or BLOCKED
- `day_of_week`: Day for recurring slots
- `is_recurring`: Whether slot is recurring
- `notes`: For blocked slots (holidays, time-offs)

### 6. Appointments (`appointments`)
Patient appointments with doctors
- `id`: Primary key
- `patient_id`: Foreign key to patients
- `doctor_id`: Foreign key to doctors
- `timeslot_id`: Foreign key to timeslots
- `appointment_date`: Date of appointment
- `start_time`, `end_time`: Time range
- `consultation_type`: ONLINE or IN_PERSON
- `reason_for_visit`: Reason for appointment
- `status`: PENDING, CONFIRMED, COMPLETED, CANCELLED, NO_SHOW, RESCHEDULED
- `cancellation_reason`: Reason if cancelled
- `cancelled_by`: WHO cancelled (patient, doctor, admin)

### 7. Medical Documents (`medical_documents`)
Patient medical documents (prescriptions, reports, etc.)
- `id`: Primary key
- `patient_id`: Foreign key to patients
- `appointment_id`: Related appointment (optional)
- `doctor_id`: Doctor who uploaded (optional)
- `document_type`: PRESCRIPTION, DIAGNOSIS_REPORT, EXAM_REPORT, etc.
- `document_url`: URL to document file
- `file_name`: Original filename
- `description`: Document description
- `uploaded_by_id`: User who uploaded

### 8. Prescriptions (`prescriptions`)
Prescriptions created by doctors
- `id`: Primary key
- `appointment_id`: Related appointment
- `patient_id`: Foreign key to patients
- `doctor_id`: Foreign key to doctors
- `medicine_name`: Name of medicine
- `dosage`: Dosage (e.g., 500mg)
- `frequency`: Frequency (e.g., twice daily)
- `duration`: Duration (e.g., 7 days)
- `instructions`: Special instructions
- `is_active`: Whether prescription is active
- `notes`: Additional notes

### 9. Ratings (`ratings`)
Doctor and visit ratings/reviews
- `id`: Primary key
- `appointment_id`: Related appointment (unique)
- `patient_id`: Foreign key to patients
- `doctor_id`: Foreign key to doctors
- `rating_score`: Overall rating (1-5)
- `rate_doctor`: Rating for doctor (1-5)
- `rate_visit`: Rating for visit experience (1-5)
- `review_text`: Review text

### 10. Admins (`admins`)
Admin users and their permissions
- `id`: Primary key
- `user_id`: Foreign key to users
- `first_name`, `last_name`: Admin name
- `can_manage_doctors`: Permission to manage doctors
- `can_manage_patients`: Permission to manage patients
- `can_view_appointments`: Permission to view appointments
- `can_view_reports`: Permission to view reports
- `can_manage_admins`: Permission to manage other admins
- `is_active`: Whether admin is active

### 11. Notifications (`notifications`)
Notifications sent to users
- `id`: Primary key
- `user_id`: Foreign key to users
- `notification_type`: Type of notification
- `channel`: EMAIL, SMS, or IN_APP
- `subject`: Notification subject
- `message`: Notification message
- `appointment_id`: Related appointment (optional)
- `is_sent`: Whether notification was sent
- `is_read`: Whether user read it
- `sent_at`: When it was sent
- `retry_count`: Number of send retries

## Relationships

- **User ? Patient**: One-to-One
- **User ? Doctor**: One-to-One
- **User ? Admin**: One-to-One
- **Doctor ? Timeslots**: One-to-Many
- **Doctor ? Appointments**: One-to-Many
- **Patient ? Appointments**: One-to-Many
- **Appointment ? Timeslot**: Many-to-One
- **Appointment ? MedicalDocuments**: One-to-Many
- **Appointment ? Prescriptions**: One-to-Many
- **Appointment ? Ratings**: One-to-One
- **Patient ? MedicalDocuments**: One-to-Many
- **Patient ? Ratings**: One-to-Many
- **Doctor ? Ratings**: One-to-Many
- **User ? Notifications**: One-to-Many
- **Appointment ? Notifications**: One-to-Many

## Enums

### RoleEnum
- PATIENT
- DOCTOR
- ADMIN

### DoctorSpecialty
- GENERAL
- CARDIOLOGY
- DERMATOLOGY
- ORTHOPEDICS
- PEDIATRICS
- NEUROLOGY
- PSYCHIATRY
- ENT
- OPHTHALMOLOGY
- GYNECOLOGY
- OTHER

### ConsultationType
- ONLINE
- IN_PERSON

### AppointmentStatus
- PENDING
- CONFIRMED
- COMPLETED
- CANCELLED
- NO_SHOW
- RESCHEDULED

### TimeslotStatus
- AVAILABLE
- BOOKED
- BLOCKED

### DocumentType
- PRESCRIPTION
- DIAGNOSIS_REPORT
- EXAM_REPORT
- LAB_REPORT
- MEDICAL_CERTIFICATE
- OTHER

### NotificationType
- APPOINTMENT_CONFIRMATION
- APPOINTMENT_REMINDER
- APPOINTMENT_CANCELLED
- APPOINTMENT_RESCHEDULED
- OTP_VERIFICATION
- RATING_REQUEST
- OTHER

### NotificationChannel
- EMAIL
- SMS
- IN_APP
