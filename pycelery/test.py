from tasks import some_task

# to run celery tasks.py
''' celery -A tasks worker --pool=solo --loglevel=info '''

number = input('Enter a number:')

if int(number) > 2:
    result = some_task.delay()
    print('valid data')
else:
    print('invalid')

print('success')