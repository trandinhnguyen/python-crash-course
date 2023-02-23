from population import city_country_population

def test_city_country():
    result = city_country_population('ha noi', 'viet nam')
    assert result == 'Ha Noi, Viet Nam'

def test_city_country_population():
    result = city_country_population('ha noi', 'viet nam', 500_000)
    assert result == 'Ha Noi, Viet Nam - population 500000'