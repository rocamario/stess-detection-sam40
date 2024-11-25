
def divide_signal_into_trials(signal):
    """
    Divides the input signal into 3 trials, each 3199 points long.

    Parameters:
    signal (numpy.ndarray): The input signal array.

    Returns:
    tuple: A tuple containing 3 trials, each of length 3199 points.
    """
    
    # Define the length of each trial
    trial_length = 3200
    
    # Divide the signal into 3 trials
    trial1 = signal[0:trial_length]
    trial2 = signal[trial_length:2*trial_length]
    trial3 = signal[2*trial_length:3*trial_length]
    
    return trial1, trial2, trial3
