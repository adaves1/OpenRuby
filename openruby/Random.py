def __init__(self, seed=0):
        
    self.m = 2**31 - 1  
    self.a = 1103515245  
    self.c = 12345  
    self.seed = seed  

def rand(self):

    self.seed = (self.a * self.seed + self.c) % self.m
    return self.seed

def rand_range(self, start, end):
        
    return start + self.rand() % (end - start)

def generate_password(length: int) -> str:
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!@#$%^&*()_-+=[]{}|;:,.<>?/~"
    all_characters = lowercase + uppercase + digits + punctuation
    def pseudo_random(seed):
        return (seed * 9301 + 49297) % 233280

    password = []
    seed = length

    password.append(lowercase[pseudo_random(seed) % len(lowercase)])
    seed += 1
    password.append(uppercase[pseudo_random(seed) % len(uppercase)])
    seed += 1
    password.append(digits[pseudo_random(seed) % len(digits)])
    seed += 1
    password.append(punctuation[pseudo_random(seed) % len(punctuation)])


    for _ in range(length - 4):
        seed += 1
        password.append(all_characters[pseudo_random(seed) % len(all_characters)])
    

    for i in range(len(password)):
        seed += 1
        swap_index = pseudo_random(seed) % len(password)
        password[i], password[swap_index] = password[swap_index], password[i]

    return ''.join(password)