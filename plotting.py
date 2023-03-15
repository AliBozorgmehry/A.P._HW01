#########################################
# LINE CHART AND SCATTER PLOT

import matplotlib.pylab as plt

plt.plot()
plt.show()


year = [1800, 1850, 1900, 1930, 1950, 1970, 1990, 2010]
pop = [1, 1.3, 1.6, 2, 2.5, 3.7, 5.3, 7.0]


# scatter plot
plt.scatter(year, pop)
plt.show()

# line chart
plt.plot(year, pop)
plt.show()

# line chart & scatter plot
plt.plot(year, pop)
plt.scatter(year, pop)
plt.show()


plt.clf()
# more customizations
plt.plot(year, pop, c = 'darkred')
plt.scatter(year, pop, c = 'darkred')
plt.xlabel('year')
plt.ylabel('population')
plt.title('World Population Over Time')
# plt.yticks([x for x in range(9)])
plt.yticks([x for x in range(9)], 
            [str(x)+' B  ' for x in range(9)])

plt.show()


# future projections
year = year + [2027, 2046]
pop = pop + [8, 9]

plt.clf()

plt.plot(year[:8], pop[:8], c = 'darkred')
plt.plot(year[7:], pop[7:], c = 'darkred', 
         linestyle = '--') # some other linetsyles: '-.', ':'
plt.scatter(year[8:], pop[8:], c = 'darkred', 
            alpha = .3)
plt.scatter(year[:8], pop[:8], c = 'darkred')

plt.xlabel('year')
plt.ylabel('population')
plt.title('World Population Over Time')
plt.yticks([x for x in range(11)], [str(x)+'B' for x in range(11)])

plt.show()

# different linestyles, legend, size, font and save
import numpy as np

x = np.linspace(0,2,100)

plt.clf() # to clear the figure
plt.figure(figsize = (15, 13))

import matplotlib

font = {'family' : 'Garamond',
        'size' : 20}
matplotlib.rc('font', **font)


plt.plot(x, x*0, alpha = .4, linestyle = '-', c = 'black')
plt.plot(x, x, linestyle = '-', label = 'linear')
plt.plot(x, x**2, linestyle = '--', label = 'squar')
plt.plot(x, x**3, linestyle = ':', label = 'cube')
plt.plot(x, np.sqrt(x), linestyle = '-.', label = 'sqrt')
plt.plot(x, np.log(x), linestyle = '-.', label = 'ln')
plt.plot(x, 2**x, linestyle = '-.', label = '2**x')
plt.legend()


plt.savefig('D:/SMCloud/mycourses/Computer Programming With Python - 99/img/plt4.png')
plt.close() # to close the figure


################
# BAR PLOT
Cities = ['Lahore', 'Paris', 'Seoul', 'London', 
          'Sao Paulo', 'Karachi', 'Istanbul', 
          'Moscow', 'Tehran', 'New York', 'Baghdad', 
          'Riyadh', 'Madrid', 'Toronto', 'Tokyo', 
          'Delhi', 'Shanghai']
Pop = [12, 11, 10, 9, 21, 16, 15, 12, 9, 
       9, 7, 7, 6, 6, 37, 29, 26]

plt.bar(Cities, Pop) # vertical barplot
plt.show()

plt.barh(Cities, Pop) # horizental barplot
plt.show()



# better to SORT them first and then plot

font = {'family' : 'normal',
        'size' : 14}
matplotlib.rc('font', **font)


Cities = np.array(Cities)
Pop = np.array(Pop)

Pop
np.sort(Pop)
np.argsort(Pop)

Cities[np.argsort(Pop)]

plt.clf()
plt.barh(Cities[np.argsort(Pop)], np.sort(Pop))
plt.barh(Cities[Cities == 'Tehran'], 
         Pop[Cities == 'Tehran']) # to distinguish Tehran, new color is automatically set

plt.show()




#############################################
#  Histograms

x = np.array([1, 2, 3, 4, 2, 11, 13, 3, 4, 5, 5, 4, 5, 6, 7, 5, 4,
              5, 6, 7, 6, 7, 5, 7, 8, 9, 0, 7, 6, 8, 9, 10])

plt.hist(x)
plt.show()

plt.hist(x, bins=5)
plt.show()


# another example
# rural and urban populations in some provinces in Iran
provs = {'Province' : ['Azarbayejan Sh', 'Azarbayejan Gh', 'Ardabil', 'Isfahan', 'Alborz'],
         'pop_rural' : [1100220, 1129000, 404236, 613073, 199559],
         'pop_urban' : [2809432, 2136219, 866184, 4507777, 2512841]}

# take a look at their histogram
plt.hist(provs['pop_rural'])
plt.show()
plt.hist(provs['pop_urban'])
plt.show()


# what about their ratio?
provs['pop_rural'] / provs['pop_urban'] # does it work ??!

# use numpy array for values in dictionary
provs = {'Province' : ['Azarbayejan Sh', 'Azarbayejan Gh', 'Ardabil', 'Isfahan', 'Alborz'],
         'pop_rural' : np.array([1100220, 1129000, 404236, 613073, 199559]),
         'pop_urban' : np.array([2809432, 2136219, 866184, 4507777, 2512841])}

plt.hist(provs['pop_rural'] / provs['pop_urban'])


plt.hist(provs['pop_rural']/1000000)
plt.show()

plt.hist(provs['pop_urban']/1000000)
plt.show()



