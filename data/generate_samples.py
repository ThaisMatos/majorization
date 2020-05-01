# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Generate samples and check if it respect the rule R

# %%
import csv
import numpy as np

dim = 3 # space dimension
total_pairs = 100 #total of pairs of vectors to be generated

# %% [markdown]
# ## Generating random samples

# %%
def generate_random_vector():
    vec_samples = list()
    for i in range(total_pairs):
        vec = np.random.uniform(size=dim) #sorting
        vec /= np.sum(vec) #normalizing
        vec_samples.append(vec)
        
    return vec_samples


# %%
def get_sorted_random_samples():
    return [np.sort(vec)[::-1] for vec in generate_random_vector()]


# %%
vec1_samples = get_sorted_random_samples()
vec2_samples = get_sorted_random_samples()

# %% [markdown]
# # Check if respect the rule

# %%
def is_less_than(v1,v2):
    return np.sum(v1) < np.sum(v2)

def is_equal(v1,v2):
    return np.isclose(np.sum(v1),np.sum(v2))

def check_rule(v1,v2):
    return is_less_than(v1,v2) or is_equal(v1,v2)


# %%
def is_a_valid_pair(v1,v2):
    for idx in range(1,len(v1)): #ignoring last sum because all vectors sum 1
        if not check_rule(v1[:idx], v2[:idx]):
            return False

    return True


# %%
def validate_samples(first_vec,second_vec):
    validation_first_vs_second = list()
    for sample1 in first_vec:
        validation_sample = list()
        for sample2 in second_vec:
            validation_sample.append(is_a_valid_pair(sample1,sample2))
        validation_first_vs_second.append(validation_sample)

    return validation_first_vs_second


# %%
validation_vec1_vs_vec2 = validate_samples(vec1_samples,vec2_samples)
validation_vec2_vs_vec1 = validate_samples(vec2_samples,vec1_samples)

# %% [markdown]
# # Writing outputs in a file
# > Format: vector1;vector2;vector1xvector2;vector2xvector1

# %%
filename = 'output_d'+str(dim)+'_s'+str(total_pairs**2)+'.csv'
with open(filename, mode='w') as output_file:
    output_writer = csv.writer(output_file,delimiter=';')

    for vec1_idx in range(total_pairs):
        for vec2_idx in range(total_pairs):
            output_writer.writerow([np.array2string(vec1_samples[vec1_idx], separator=', '),np.array2string(vec2_samples[vec2_idx], separator=', '),validation_vec1_vs_vec2[vec1_idx][vec2_idx],validation_vec2_vs_vec1[vec2_idx][vec1_idx]])

