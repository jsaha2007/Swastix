from agents.orchestrators.admin_orchestrator import AdminOrchestrator

admin_orchestrator = AdminOrchestrator()
result = admin_orchestrator.run("View reporting dashboard with daily booking and cancellation volume")

print(f"Story saved at: {result['story']}")
print(f"Code saved at: {result['code']}")
print(f"Review saved at: {result['review']}")
print(f"Data saved at: {result['data']}")
print(f"Tests saved at: {result['tests']}")
