# Candidate Elimination Algorithm

import csv

def candidate_elimination(data):
    # Initialize S and G
    num_attributes = len(data[0]) - 1

    S = ['0'] * num_attributes
    G = [['?'] * num_attributes]

    print("Initial S:", S)
    print("Initial G:", G)
    print("-" * 50)

    for i, example in enumerate(data):
        x = example[:-1]
        label = example[-1]

        print(f"Training Example {i + 1}: {example}")

        if label == 'Yes':  # Positive example
            for j in range(num_attributes):
                if S[j] == '0':
                    S[j] = x[j]
                elif S[j] != x[j]:
                    S[j] = '?'

            # Remove inconsistent hypotheses from G
            G = [g for g in G if all(g[j] == '?' or g[j] == S[j] for j in range(num_attributes))]

        else:  # Negative example
            new_G = []
            for g in G:
                if all(g[j] == '?' or g[j] == x[j] for j in range(num_attributes)):
                    for j in range(num_attributes):
                        if g[j] == '?':
                            if S[j] != '?' and S[j] != x[j]:
                                new_hypothesis = g.copy()
                                new_hypothesis[j] = S[j]
                                new_G.append(new_hypothesis)
                else:
                    new_G.append(g)

            G = new_G

        print("S:", S)
        print("G:", G)
        print("-" * 50)

    return S, G


# 🔹 Sample training data
# Format: [Sky, AirTemp, Humidity, Wind, Water, Forecast, Target]
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
  
]

# Run algorithm
S_final, G_final = candidate_elimination(training_data)

print("\nFinal Specific Hypothesis (S):", S_final)
print("Final General Hypotheses (G):", G_final)
