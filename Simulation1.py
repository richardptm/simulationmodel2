import numpy as np
import matplotlib.pyplot as plt
# Define the number of patients
num_patients = 1000  
# Define the number of simulations
num_simulations = 500  
# Define baseline waiting time parameters
baseline_mean = 60  # Average waiting time in minutes
baseline_std = 15   # Standard deviation of waiting times in minutes
# Generate synthetic baseline waiting times for all patients
baseline_waiting_times = np.random.normal(baseline_mean, baseline_std, num_patients)
# Define parameters
np.random.seed(45)  # Ensures reproducibility of random values
# Simulate symptom severity and categorize into urgent/non-urgent
symptom_severity = np.random.uniform(0, 1, num_patients)
urgent_patients = symptom_severity > 0.7
non_urgent_patients = ~urgent_patients

# Define percentage reduction in waiting time due to triage
urgent_reduction = 0.60  # 60% reduction for urgent
non_urgent_reduction = 0.30  # 30% reduction for non-urgent

# Apply reductions based on classification
waiting_times_after_triage = np.copy(baseline_waiting_times)
waiting_times_after_triage[urgent_patients] *= (1 - urgent_reduction)
waiting_times_after_triage[non_urgent_patients] *= (1 - non_urgent_reduction)

# Monte Carlo simulation to assess uncertainty
simulated_waiting_times = []

for _ in range(num_simulations):
    # Simulate variability in triage effectiveness (±5%)
    urgent_variation = urgent_reduction + np.random.uniform(-0.05, 0.05)
    non_urgent_variation = non_urgent_reduction + np.random.uniform(-0.05, 0.05)
    
    simulated_times = np.copy(baseline_waiting_times)
    simulated_times[urgent_patients] *= (1 - urgent_variation)
    simulated_times[non_urgent_patients] *= (1 - non_urgent_variation)
    
    simulated_waiting_times.append(simulated_times.mean())
# Visualize results
plt.figure(figsize=(12, 6))

# Baseline vs Improved Waiting Times
plt.hist(baseline_waiting_times, bins=30, alpha=0.6, label="Baseline Waiting Times", color='blue')
plt.hist(waiting_times_after_triage, bins=30, alpha=0.6, label="After Triage (Urgent/Non-Urgent)", color='green')
plt.title("Baseline vs Waiting Times After Triage")
plt.xlabel("Waiting Time (minutes)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Monte Carlo Simulation Results
plt.figure(figsize=(12, 6))
plt.hist(simulated_waiting_times, bins=30, color='purple', alpha=0.7)
plt.title("Monte Carlo Simulation: Average Waiting Times (Urgent/Non-Urgent)")
plt.xlabel("Average Waiting Time (minutes)")
plt.ylabel("Frequency")
plt.axvline(np.mean(simulated_waiting_times), color='red', linestyle='dashed', linewidth=1, label="Mean Simulated Time")
plt.legend()
plt.show()

# Print summary statistics
baseline_mean_wait = np.mean(baseline_waiting_times)
improved_mean_wait = np.mean(waiting_times_after_triage)
simulated_mean_wait = np.mean(simulated_waiting_times)
simulated_std_wait = np.std(simulated_waiting_times)

(baseline_mean_wait, improved_mean_wait, simulated_mean_wait, simulated_std_wait)

