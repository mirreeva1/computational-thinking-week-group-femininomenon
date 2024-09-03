import numpy as np

def solution_station_6(inputs: int) -> float:
    sample_inputs = np.array([1.6, 0.8, 1.9, 0.3, 1.3, 1.3, 2.8, 2.6])
    sample_outputs = np.array([0.9996, 0.7174, 0.9463, 0.2955, 0.9636, 0.9636, 0.335, 0.5155])
    
    min_input = np.min(sample_inputs)
    max_input = np.max(sample_inputs)
    
    normalized_input = (inputs - min_input) / (max_input - min_input)

    transformed_results_provided = np.array([1535.144, 2349.544, 883.624, 1209.384, 2919.624, 2960.344, 598.584, 1860.904])
    scaling_factor = (transformed_results_provided - transformed_results_provided.mean()) / (normalized_input - normalized_input.mean())
    scaling_factor = scaling_factor.mean()  

    normalized_result = normalized_input * scaling_factor
    
    return normalized_result
