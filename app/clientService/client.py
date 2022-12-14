from threading import Thread
import time
import random
from components.tables import *
from components.foods import menu
from components.orders import *

time_unit = 1

# Customized Clients class extending the Thread class
class Client(Thread):
    def __init__(self, *args, **kwargs):
        # Access methods of the base class
        super(Client, self).__init__(*args, **kwargs)

    # Represent the thread's activity
    def run(self):
        # Continuous threading of creating objects
        while True:
            # Delay the execution of the function for 5 seconds
            time.sleep(5)
            # Execute the function to create an order
            self.generate_order()

    # Method to generate an order
    def generate_order(self):
        # Return the next free table from the list of tables
        (table_id, table) = next(((id, table) for id, table in enumerate(tables) if table['state'] == table_state1), (None, None))
        # Check if there is a free table
        if table_id is not None:
            # Random order id
            order_id = int(random.random() * random.random() / random.random() * 1000)
            # Create an array to store the chosen foods id's
            # The client can order up to 10 foods
            chosen_foods = random.sample(range(1, len(menu) + 1), random.randint(1, 5))
            # Random order priority
            order_priority = random.randint(1, 5)
            # Calculate the maximum wait time
            max_wait_time = 0
            for i in chosen_foods:
                food = menu[i - 1]
                if max_wait_time < food['preparation-time']:
                    max_wait_time = food['preparation-time']
            max_wait_time = max_wait_time * 1.3
            # Create the order
            order = {'table_id': table['id'], 'id': order_id, 'items': chosen_foods, 'priority': order_priority, 'max_wait': max_wait_time}
            # Put the order in the orders queue
            order_queue.put(order)
            # Add the order to the table
            tables[table_id]['order_id'] = order_id
            # Change the table state
            tables[table_id]['state'] = table_state2
            # Verify the order after receiving it from the kitchen
            orders.append(order)
        else:
            # Random time for clints to free the table
            time.sleep(random.randint(2, 10) * time_unit)
            # Free a random table
            (table_id, table) = next(((id, table) for id, table in enumerate(tables) if table['state'] == table_state4), (None, None))
            if table_id is not None:
                # Change the status of the table
                tables[table_id]['state'] = table_state1