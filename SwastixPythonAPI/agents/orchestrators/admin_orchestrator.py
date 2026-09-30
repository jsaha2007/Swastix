from agents.orchestrators.base_orchestrator import BaseOrchestrator

class AdminOrchestrator(BaseOrchestrator):
    def __init__(self):
        super().__init__(
            domain_context="""Swastix Doctor Booking System. 
            Admin can manage doctor and their schedule, manage patients and their appointments.
            Moreover, admin can get a reporting dashboard to view which contains daily volume, 
            booking volume, cancellation volume, successfull visit volume"""
        )