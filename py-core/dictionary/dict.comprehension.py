rates = ['UYU_39.6', 'EUR_0.8']
op = {rate.split('_')[0]: rate.split('_')[1]
      for rate in rates}  # defined by curly brackets
print(op)

# Output: {'UYU': '39.6', 'EUR': '0.8'}
