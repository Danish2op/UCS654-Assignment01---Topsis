import pandas as pd
import numpy as np
import sys

def normalize_matrix(data, weights):
    norm_data = data / np.sqrt((data**2).sum(axis=0))
    return norm_data * weights

def calculate_ideal_solutions(norm_data, impacts):
    ideal_best = []
    ideal_worst = []
    for i, impact in enumerate(impacts):
        if impact == '+':
            ideal_best.append(np.max(norm_data[:, i]))
            ideal_worst.append(np.min(norm_data[:, i]))
        elif impact == '-':
            ideal_best.append(np.min(norm_data[:, i]))
            ideal_worst.append(np.max(norm_data[:, i]))
    return np.array(ideal_best), np.array(ideal_worst)

def calculate_topsis_score(norm_data, ideal_best, ideal_worst):
    distances_best = np.sqrt(((norm_data - ideal_best)**2).sum(axis=1))
    distances_worst = np.sqrt(((norm_data - ideal_worst)**2).sum(axis=1))
    scores = distances_worst / (distances_best + distances_worst)
    return scores

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        return

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    result_file = sys.argv[4]

    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    if len(data.columns) < 3:
        print("Error: Input file must have at least three columns.")
        return

    if len(weights) != len(data.columns) - 1 or len(impacts) != len(data.columns) - 1:
        print("Error: The number of weights and impacts must match the number of criteria (columns).")
        return

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be either '+' or '-'.")
        return

    try:
        matrix = data.iloc[:, 1:].to_numpy(dtype=float)
    except ValueError:
        print("Error: All criteria values must be numeric.")
        return

    norm_data = normalize_matrix(matrix, weights)
    ideal_best, ideal_worst = calculate_ideal_solutions(norm_data, impacts)
    topsis_scores = calculate_topsis_score(norm_data, ideal_best, ideal_worst)

    rankings = topsis_scores.argsort()[::-1] + 1

    # Add Topsis Score and Rank to the original DataFrame
    data['Topsis Score'] = topsis_scores
    data['Rank'] = rankings

    # Save the updated DataFrame to the result file
    data.to_csv(result_file, index=False)

    print(f"Result file successfully saved to: {result_file}")

if __name__ == "__main__":
    main()
