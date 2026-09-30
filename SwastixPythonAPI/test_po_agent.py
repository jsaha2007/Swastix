from agents.po_agent import PoAgent

po = PoAgent()
result_path = po.execute("Search doctors by name and address")
print(f"Story saved at: {result_path}")
