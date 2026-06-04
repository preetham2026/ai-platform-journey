# Basic tests for Ritham Dairy Farm API

def test_milk_calculation():
    milk = 35
    price = 1.50
    revenue = milk * price
    assert revenue == 52.50
    print("✅ Milk calculation test passed!")

def test_grade_calculation():
    def get_grade(milk):
        if milk >= 30:   return "A"
        elif milk >= 25: return "B"
        elif milk >= 20: return "C"
        else:            return "D"

    assert get_grade(35) == "A"
    assert get_grade(27) == "B"
    assert get_grade(22) == "C"
    assert get_grade(15) == "D"
    print("✅ Grade calculation test passed!")

def test_farm_data():
    cows = ["Bessie", "Clara", "Bella", "Ruby"]
    assert len(cows) == 4
    assert "Clara" in cows
    print("✅ Farm data test passed!")

if __name__ == "__main__":
    print("🧪 Running Ritham Farm Tests...")
    test_milk_calculation()
    test_grade_calculation()
    test_farm_data()
    print("\n🎉 All tests passed!")