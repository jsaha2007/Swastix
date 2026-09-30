from agents.orchestrators.base_orchestrator import BaseOrchestrator

class DoctorOrchestrator(BaseOrchestrator):
   def __init__(self):
       super().__init__(
           domain_context = """Swastix Doctor Booking System. 
           Doctors manage availability, appointments, prescriptions, view patient's medical history.
           Moreover, Rate the patient"""
       )

