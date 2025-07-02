# Programming exercise:
# The next leap year

year = int(input("Year: "))

candidate_year = year + 1

while True:
    is_divisible_by_400 = (candidate_year % 400 == 0)
    is_divisible_by_4_but_not_100 = (candidate_year % 4 == 0 and candidate_year % 100 !=0)

    if is_divisible_by_400 or is_divisible_by_4_but_not_100:
        print(f"The next leap year after {year} is {candidate_year}")
        break

    candidate_year += 1

# Mantido parênteses nas expressões para melhorar legibilidade

