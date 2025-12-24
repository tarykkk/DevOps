from string_utils import print_string, analyze_string_case, uppercase_list
from generator_utils import even_odd_generator

print_string("Hello")
analyze_string_case("HELLO")
print(uppercase_list("smogtether"))

gen = even_odd_generator()
for _ in range(4):
    print(next(gen))