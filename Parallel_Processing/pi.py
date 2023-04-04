import multiprocessing
import random
import cProfile

# Define the number of samples to use for the Monte Carlo simulation
samples = 1000000

# Define a function to calculate pi using a serial approach
def pi_serial():

    # Initialize the number of hits within the unit circle to 0
    hits = 0

    # Loop over the number of samples and generate a random point in the unit square
    for i in range(samples):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        # If the point is within the unit circle, increment the number of hits
        if x**2 + y**2 <= 1:
            hits += 1

    # Calculate pi using the number of hits and return the result
    pi = 4.0 * hits/samples
    return pi

# Define a function to generate a single sample and return 1 if the sample is 
# within the unit circle and 0 otherwise
def sample():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0
    

# Define a function to calculate pi using a parallel approach with the apply_async() method
def pi_apply_async():
    # Create a multiprocessing Pool object
    pool = multiprocessing.Pool()

    # Generate a list of async results by calling the sample function in parallel for each sample
    results_async = [pool.apply_async(sample) for i in range(samples)]

    # Compute the number of hits by summing the results of the async calls
    hits = sum(r.get() for r in results_async)

    # Calculate pi using the number of hits and return the result
    pi = 4.0 * hits/samples
    return pi


# Define a function to generate multiple samples and return the sum of the results
def sample_multiple(samples_partial):
    return sum(sample() for i in range(samples_partial))


# Define a function to calculate pi using a parallel approach with the apply_async() method and chunked inputs
def pi_apply_async_chunked():
    # Define the number of tasks to use and the size of each chunk
    ntasks = 10
    chunk_size = int(samples / ntasks)

    # Create a multiprocessing Pool object
    pool = multiprocessing.Pool()

    # Generate a list of async results by calling the sample_multiple function in parallel for each task
    results_async = [pool.apply_async(sample_multiple, [chunk_size]) for i in range(ntasks)]

    # Compute the number of hits by summing the results of the async calls
    hits = sum(r.get() for r in results_async)

    # Calculate pi using the number of hits and return the result
    pi = 4.0 * hits / samples
    return pi

# Calculate the compute time for each function
if __name__ == "__main__":

    cProfile.run("pi_serial()")

    cProfile.run("pi_apply_async()")

    cProfile.run("pi_apply_async_chunked()")