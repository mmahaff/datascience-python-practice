print 'Hello World'

x = 'This is a string'
print(x[0])
print(x[0:1])
print(x[0:2])
print(x[-1])
print(x[-4:-2])
print(x[:3])
print(x[3:])

firstname='Christopher'
lastname='Brooks'

print(firstname + ' ' + lastname)
print(firstname * 3)
print('Chris' in firstname)

print('Chris' + str(2))

sales_record = {'price': 3.24,
                'num_items': 4,
                'person': 'Chris'}
sales_statement = '{} bought {} items at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))
                             
