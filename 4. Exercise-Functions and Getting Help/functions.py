#%%
#Question 1
def round_to_two_places(num):
    num = round(num, 2)
    print(num)
    return num

round_to_two_places(12.323456)

#%%
# Question 2
round(234, -1)

#%%
# Question 3
def to_smash(total_candies, friends=3):
    return total_candies % friends

to_smash(32, 1)

#%%
# Question 4
round_to_two_places(9.9999)
#%%
x = -10
y = 5
# # Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))
print(smallest_abs)
#%%
def f(x):
    y = abs(x)
    return y

print(f(5))