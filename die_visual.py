from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results =[]

for roll_num in range(10000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides

for value in range(2,max_result+1):
	frequence = results.count(value)
	frequencies.append(frequence)

print(frequencies)

hist = pygal.Bar()
hist.title = "结果"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "结果"
hist.y_title = "频率结果"
hist.add('d6',frequencies)
hist.render_to_file('die_visual.svg')