from collections import deque
from datetime import datetime
import time

# ---------- STACK CLASS ----------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# ---------- QUEUE CLASS ----------
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# ---------- CAR CLASS ----------
class Car:
    def __init__(self, number):
        self.number = number
        self.entry_time = datetime.now()

    def __str__(self):
        return f"Car[{self.number}]"


# ---------- PARKING LOT CLASS ----------
class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_stack = Stack()
        self.waiting_queue = Queue()

    def park_car(self, car_number):
        car = Car(car_number)
        if self.parking_stack.size() < self.capacity:
            self.parking_stack.push(car)
            print(f"{car} parked at {car.entry_time.strftime('%H:%M:%S')}")
        else:
            self.waiting_queue.enqueue(car)
            print(f"Parking full! {car} added to waiting queue.")

    def remove_car(self):
        if self.parking_stack.is_empty():
            print("No cars to remove.")
            return

        car = self.parking_stack.pop()
        exit_time = datetime.now()
        parked_duration = (exit_time - car.entry_time).seconds
        fee = parked_duration * 0.5  # ₹0.5 per second (demo logic)
        print(f"{car} left the parking at {exit_time.strftime('%H:%M:%S')}. Fee: ₹{fee:.2f}")

        if not self.waiting_queue.is_empty():
            next_car = self.waiting_queue.dequeue()
            self.parking_stack.push(next_car)
            print(f"{next_car} moved from queue to parking.")

    def display_status(self):
        print("\n--- Parking Lot Status ---")
        print(f"Cars Parked: {self.parking_stack.size()}/{self.capacity}")
        print(f"Waiting Queue: {self.waiting_queue.size()} cars\n")


# ---------- DEMO ----------
if __name__ == "__main__":
    parking = ParkingLot(capacity=3)

    parking.park_car("KA-01-AA-1234")
    parking.park_car("KA-02-BB-5678")
    parking.park_car("KA-03-CC-9999")
    parking.park_car("KA-04-DD-4321")  # Goes to queue

    time.sleep(2)
    parking.display_status()

    parking.remove_car()
    time.sleep(1)
    parking.display_status()

    parking.remove_car()
    parking.display_status()
