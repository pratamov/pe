total_lychrel = 0
for i in range(0, 10_000):
    is_lychrel = False
    iter_, prev_, next_ = 0, i, int(str(i)[::-1])

    while str(prev_ + next_)[::-1] != str(prev_ + next_) and iter_ < 51:
        temp_ = next_
        next_ = prev_ + next_
        prev_ = temp_
        iter_ += 1

    total_lychrel += 1 if iter_ > 50 else 0

print(total_lychrel)