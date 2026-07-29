class LocalGapGenerator:

    def generate(self, analysis_text):

        text = analysis_text.lower()

        # 5G + IoT
        if "5g" in text or "iot" in text:

            return """
TOP 5 RESEARCH GAPS

1. Limited Integration of 5G and Edge AI
Most studies discuss 5G connectivity but ignore intelligent edge processing.

2. Scalability Challenges
Large-scale IoT deployments still face performance bottlenecks.

3. Energy Efficiency Issues
5G-enabled IoT devices consume significant power.

4. Security and Privacy Concerns
Many solutions lack strong cybersecurity mechanisms.

5. Real-World Deployment Validation
Most approaches are evaluated only in simulations.

RESEARCH OPPORTUNITIES

• AI-Powered Edge IoT Systems
• Secure 5G IoT Frameworks
• Energy-Efficient Smart Devices
• Digital Twin IoT Architectures
• Autonomous IoT Networks
"""

        # Quantum Security
        elif "quantum" in text:

            return """
TOP 5 RESEARCH GAPS

1. Quantum Hardware Limitations
2. Lack of Large-Scale Evaluation
3. Poor Explainability
4. Hybrid Quantum-Classical Optimization
5. Real-Time Deployment Challenges

RESEARCH OPPORTUNITIES

• Quantum Federated Learning
• Explainable Quantum AI
• Hybrid Quantum IDS
• Quantum Edge Computing
• Quantum Cybersecurity
"""

        # Intrusion Detection
        elif (
            "intrusion" in text
            or "cyber" in text
            or "security" in text
        ):

            return """
TOP 5 RESEARCH GAPS

1. Lack of Real-Time Deployment
2. Limited Explainability
3. Poor Adaptation to Zero-Day Attacks
4. High Computational Cost
5. Limited Edge/IoT Optimization

RESEARCH OPPORTUNITIES

• Explainable Intrusion Detection Systems
• Quantum-enhanced IDS
• Federated Learning IDS
• Edge AI Security Frameworks
• Autonomous Self-Learning Cybersecurity Systems
"""

        # Generic fallback
        else:

            return """
TOP 5 RESEARCH GAPS

1. Limited Real-World Validation
2. Scalability Issues
3. Lack of Explainability
4. High Resource Consumption
5. Dataset Limitations

RESEARCH OPPORTUNITIES

• Explainable AI
• Edge Computing
• Federated Learning
• Green AI
• Autonomous Systems
""" 