def median(samples:list, rounded:int=2) -> float:
    if len(samples) % 2 == 0:
        median_samples = (samples[len(samples)//2 - 1] + samples[len(samples)//2]) / 2
    else:
        median_samples = samples[len(samples)//2]
    return round(median_samples, rounded)


def standardization_samples(samples:list, sort=False) -> list:
    '''Standartization by median'''
    if sort == True:
        samples.sort()

    median_samples = median(samples)
    
    variance = (sum([(i-median_samples)**2 for i in samples]) / len(samples)-1)**0.5
    variance = round(variance, 2)

    z_scores = [(i-median_samples)/variance for i in samples]

    return z_scores

def normalisation_samples(samples:list, min_range:int=-1, max_range:int=1, rounded:int=0, sort:bool=False) -> list:
    '''Normalisation in range min-max'''

    if sort == True:
        samples.sort()

    range_samples = max(samples) - min(samples)
    if range_samples == 0.0:
        return [0.0]
    first = min(samples)
    normalized = [round(min_range + (((i - first)*(max_range-min_range)) / range_samples), rounded) for i in samples]

    return normalized

def adjusted_boxplot(samples:list, rounded=2, interval:float=1.96, sort:bool=False) -> list:
    '''Using confidence intervals to standardize data'''
    if sort == True:
        samples.sort()

    median_samples = median(samples)

    variance = (sum([(i-median_samples)**2 for i in samples]) / len(samples)-1)**0.5
    variance = round(variance, rounded)

    se = variance / len(samples)**0.5
    se = round(se, rounded)

    boxplot_left = median_samples - interval * se
    boxplot_right = median_samples + interval * se

    for i in range(len(samples)):
        if samples[i] < boxplot_left:
            samples[i] = boxplot_left
        if samples[i] > boxplot_right:
            samples[i] = boxplot_right

    return samples