# This program scrapes source code from an HTML web page.
import urllib.request

cities = ['Seattle', 'Atlanta', 'Dallas', 'New York']

print('Your weather report')
print('Current observations are available for:')
for i in range(0, len(cities)):
    print('-',cities[i])
print()
city = input('Enter the city you would like a weather report for: ')

while city not in cities:
    city = input('No data available. Please try another city: ')

if city in cities:
    print('Accessing weather data . . .')
    print()
    print('The current weather has been accessed for', city)


# Access web page
try:
    if city == 'Seattle':
        page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KSEA.xml')
        data = page.read().decode('utf-8')
    elif city == 'Atlanta':
        page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KPDK.xml')
        data = page.read().decode('utf-8')
    elif city == 'Dallas':
        page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KDFW.xml')
        data = page.read().decode('utf-8')
    elif city == 'New York':
        page = urllib.request.urlopen('https://w1.weather.gov/xml/current_obs/KNYC.xml')
        data = page.read().decode('utf-8')
except:
    print('Failed to access webpage.')
    
else:
    
    # dictionary
    info = {'location': None,
                  'weather': None,
                  'temperature': None,
                  'humidity': None,
                  'wind': None,
                  'observation': None}

    # split data at line break
    split_data = data.split('\n')

    for line in split_data:
        if "<location>" in line:
            info['location'] = line[11:-11] # store in dictionary
              
        if "<weather>" in line:
            info['weather'] = line[10:-10]
            
        if "<temp_f>" in line:
            info['temperature'] = line[9:-10] + ' degrees F'
            
        if "<relative_humidity>" in line:
            info['humidity'] = line[20:-20] + '%'
            
        if "<wind_string>" in line:
            info['wind'] = line[14:-14]
            
        if "<observation_time>" in line:
            info['observation'] = line[19:-20]


        
        

    # ask user which data they want
    print()
    print('Information available:')
    for key in info:
        print('-', key)
        
    
    def prompt(request):
        if request == 'location': # make this a def
            print('The exact location is', info['location'])
            print()

        elif request == 'temperature':
            print('The temperature in', city,'is', info['temperature'])
            print()

        elif request == 'observation':
            print(info['observation'])
            print()

        elif request=='weather':
            print('The',request, 'in', city, 'is', info['weather'])
            print()

        elif request=='humidity':
            print('The',request, 'in', city, 'is', info['humidity'])
            print()

        elif request=='wind':
            print('The',request, 'in', city, 'is', info['wind'])
            print()

    print()
    request = input('What weather information would you like? ').lower()
    if request not in info:
        print('That data is not available.')
        print()
    else:
        prompt(request)

    while True:
        request = input('What weather information would you like? Or, to end, enter "done". ')
        if request == 'done':
            break
        prompt(request)

        while request not in info:
            print('That data is not available.')
            print()
            request = input('What weather information would you like? Or, to end, enter "done". ')
            prompt(request)

            if request == 'done':
                break

        


    
