# Import the pygame library for multimedia applications
import pygame
# Import the time library for sleep function
import time

# Initialize pygame, which is necessary before using its modules
pygame.init()

# Load the swap sound effect from a given file path
swap_sound = pygame.mixer.Sound("C:\\Users\\Owner\\Downloads\\PingSoundEffect.wav")

# Define a function to play a given sound
def play_sound(sound):
    sound.play()  # Play the given sound
    time.sleep(1)  # Pause the program for 1 second to let the sound play

# Define the merge sort function with an array and a step counter as parameters
def merge_sort(arr, step=[0]):
    if len(arr) > 1:  # If the array has more than one element, proceed with sorting
        mid = len(arr) // 2  # Find the middle of the array
        L = arr[:mid]  # Divide the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L, step)  # Recursively sort the first half
        merge_sort(R, step)  # Recursively sort the second half

        i = j = k = 0  # Initialize counters for L, R, and the main array

        # Merge the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:  # If the element in L is smaller, add it to the main array
                arr[k] = L[i]
                i += 1
            else:  # Otherwise, add the element from R
                arr[k] = R[j]
                j += 1
            k += 1
            step[0] += 1  # Increment the step counter
            print(f"Step {step[0]}:", arr)  # Print the current step and array
            play_sound(swap_sound)  # Play sound on each merge action

        # Copy the remaining elements of L[], if there are any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            step[0] += 1
            print(f"Step {step[0]}:", arr)
            play_sound(swap_sound)

        # Copy the remaining elements of R[], if there are any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            step[0] += 1
            print(f"Step {step[0]}:", arr)
            play_sound(swap_sound)

# Initialize an array with unsorted numbers
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Given array is:", arr)  # Print the unsorted array
merge_sort(arr)  # Call the merge_sort function on the array
print("Sorted array is:", arr)  # Print the sorted array

# Quit pygame
pygame.quit()
