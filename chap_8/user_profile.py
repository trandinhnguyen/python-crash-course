def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last

    return kwargs


my_profile = build_profile(
    'nguyen', 'tran', dob='9-12-2000', age='23', gender='male')

print(my_profile)
