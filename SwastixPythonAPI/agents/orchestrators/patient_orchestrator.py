from agents.orchestrators.base_orchestrator import BaseOrchestrator

class PatientOrchestrator(BaseOrchestrator):
    def __init__(self):
        super().__init__(
            domain_context="""Swastix Doctor Booking System. 
            Patient can search for doctors, view doctor's details, manage own appointments only.
            Moreover, Get notified via SMS/Email about appointment
            Rate doctor and the visit"""
        )