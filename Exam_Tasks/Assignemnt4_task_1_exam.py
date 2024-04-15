import numpy as np
import matplotlib.pyplot as plt
import pulp

# Create a LP Maximize problem
lp_prob = pulp.LpProblem('Problem', pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable("x", lowBound=0, cat='Continuous')
y = pulp.LpVariable("y", lowBound=0, cat='Continuous')

# Objective function
lp_prob += 200*x + 300*y

# Constraints
lp_prob += 15*x + 20*y <= 2400  # Machine time constraint
lp_prob += 20*x + 30*y <= 2100  # Craftsman time constraint
lp_prob += x >= 10              # Demand constraint for Product X

# Solve the problem
lp_prob.solve()

# Print the results
print("Production of Product X per week:", pulp.value(x))
print("Production of Product Y per week:", pulp.value(y))
print("Total profit per week: £", pulp.value(lp_prob.objective))

# Define the constraints
def machine_constraint(x):
    return (2400 - 15*x) / 20

def craftsman_constraint(x):
    return (2100 - 20*x) / 30

def demand_constraint():
    return 10

# Define the objective function
def objective_function(x):
    return (200/300)*x

# Create x values for plotting
x_values = np.linspace(0, 150, 400)

# Plot the constraints
plt.plot(x_values, machine_constraint(x_values), label='Machine Time Constraint: 15x + 20y ≤ 2400')
plt.plot(x_values, craftsman_constraint(x_values), label='Craftsman Time Constraint: 20x + 30y ≤ 2100')
plt.axvline(x=demand_constraint(), color='red', linestyle='--', label='Demand Constraint: x ≥ 10')

# Plot the objective function
plt.plot(x_values, objective_function(x_values), label='Profit: 200x + 300y', color='green')

# Add labels and legend
plt.xlabel('Units of X')
plt.ylabel('Units of Y')
plt.title('Optimization Problem')
plt.legend()
plt.grid(True)


# Show plot
plt.xlim(0, 150)
plt.ylim(0, 150)
plt.show()