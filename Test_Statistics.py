import statistics_calc

# test_calc_average()

def test_calc_avg_empty_values():
    assert(statistics_calc.calc_average([])==False)

def test_calc_avg_positive_values():
    assert(statistics_calc.calc_average([1,2,3,4,5])==3)

def test_calc_avg_negative_values():
    assert(statistics_calc.calc_average([-1,-2,-3,-4,-5])==-3)

def test_calc_avg_mixed_values():
    assert(statistics_calc.calc_average([-1,2,-3,4,-5])==-0.6)

def test_calc_avg_same_values():
    assert(statistics_calc.calc_average([5,5,5,5,5])==5)

def test_calc_avg_float_values():
    assert(statistics_calc.calc_average([0.5,1.5,2.5,3.5,4.5])==2.5)

# test_calc_min_max()

def test_calc_min_max_empty_values():
    assert(statistics_calc.calc_min_max([])==False)

def test_calc_min_max_positive_values():
    assert(statistics_calc.calc_min_max([1,2,3,4,5])==[1,5])

def test_calc_min_max_negative_values():
    assert(statistics_calc.calc_min_max([-1,-2,-3,-4,-5])==[-5,-1])

def test_calc_min_max_mixed_values():
    assert(statistics_calc.calc_min_max([-1,2,-3,4,-5])==[-5,4])

def test_calc_min_max_same_values():
    assert(statistics_calc.calc_min_max([5,5,5,5,5])==[5,5])

def test_calc_min_max_float_values():
    assert(statistics_calc.calc_min_max([0.5,1.5,2.5,3.5,4.5])==[0.5,4.5])

# test_calc_median()

def test_calc_median_empty_values():
    assert(statistics_calc.calc_median([])==False)

def test_calc_median_positive_values():
    assert(statistics_calc.calc_median([5,2,7,55,21,16])==11.5)

def test_calc_median_negative_values():
    assert(statistics_calc.calc_median([-5,-2,-7,-55,-21,-16])==-11.5)

def test_calc_median_mixed_values():
    assert(statistics_calc.calc_median([-5,2,-7,55,-21,16])==-1,5)

def test_calc_median_same_values():
    assert(statistics_calc.calc_median([5,5,5,5,5])==5)

def test_calc_median_float_values():
    assert(statistics_calc.calc_median([0.5,1.5,2.5,3.5,4.5,5.5])==3)
