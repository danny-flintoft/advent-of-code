dir_ = "2025/day_08/"
input_data = open(dir_+'input_1.txt', 'r').read().split('\n')
test_data = open(dir_+'test_input.txt', 'r').read().split('\n')

import pandas as pd

######################### part 1 #########################
data = input_data


def get_distance(a,b):
    dist = ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5
    return dist

positions = [[int(y) for y in x.split(',')] for x in data]

# build data frame of all position pairs + distance

positions_df = pd.DataFrame()
positions_df['pos'] = positions
positions_df['key'] = 0
positions_df = positions_df.merge(positions_df, on ='key', how = 'outer')
positions_df = positions_df[['pos_x','pos_y']]
positions_df = positions_df.query("pos_x != pos_y").copy()   
positions_df['distance'] = \
    positions_df.apply(lambda x: get_distance(x.pos_x, x.pos_y), axis=1)
positions_df = positions_df.sort_values('distance')


# process pairs
connected_boxes = []
circuits = []

run = 0
while len(connected_boxes) < len(positions):
  run += 1 
  
  box_a = positions_df.iloc[0,0]
  box_b = positions_df.iloc[0,1]
  positions_df = positions_df.iloc[2:] # remove two because everything is duplicated as a result of the cross join

  if box_a in connected_boxes and box_b in connected_boxes:
      
      for i, circuit_1 in enumerate(circuits):
          if box_a in circuit_1:
              break
          
      for j, circuit_2 in enumerate(circuits):
          if box_b in circuit_2:
              break   
      
      if i != j:
        new_circuit = circuit_1 + circuit_2
        circuits = circuits + [new_circuit]
        
        if i > j:
            del circuits[i]
            del circuits[j]
        else:
            del circuits[j]
            del circuits[i]
  
  elif box_a in connected_boxes:
      for i, circuit in enumerate(circuits):
          if box_a in circuit:
              new_circuit = circuit + [box_b]
              del circuits[i]
              circuits = circuits + [new_circuit]
              connected_boxes.append(box_b)
              break
          
  elif box_b in connected_boxes:
      for i, circuit in enumerate(circuits):
          if box_b in circuit:
              new_circuit = circuit + [box_a]
              del circuits[i]
              circuits = circuits + [new_circuit]
              connected_boxes.append(box_a)
              break
   
  else:
      circuits.append([box_a, box_b])
      connected_boxes.append(box_a)
      connected_boxes.append(box_b)  
      
  if run == 1000:
      circuit_lengths = [len(circuit) for circuit in circuits]
      circuit_lengths.sort(reverse = True)
      p1_ans = circuit_lengths[0]*circuit_lengths[1]*circuit_lengths[2]
 
p2_ans = box_a[0] * box_b[0]

print(f"part 1 answer: {p1_ans}")
print(f"part 2 answer: {p2_ans}")
