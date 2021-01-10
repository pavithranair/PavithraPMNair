import step_4

start = time.time()#stores the number of seconds passed since epoch
verified_elements = step_4.np_intersection(subset_elements, all_elements)#stores the intersection of subset_elements and all_elements
print(len(verified_elements))#prints length of intersection of subset_elements and all_elements
print('Duration: {} seconds'.format(time.time() - start))#prints time passed since start

start = time.time()#stores the number of seconds passed since epoch
verified_elements = step_4.set_intersection(subset_elements, all_elements)#stores the intersection of subset_elements and all_elements
print(len(verified_elements))#prints length of intersection of subset_elements and all_elements
print('Duration: {} seconds'.format(time.time() - start))#prints time passed since start
