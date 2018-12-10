import sys
def analyze_text(text):
    # Your code here
    """ Count the alphabetical characters; also, the letters 'e'. Return a ratio. """
    
def answer(nums_alpha, nums_e, quotient):
    print("The text contains " + nums_alpha + " alphabetic characters, of which " + 
            nums_e + " (" + quotient + "%) are 'e'.")

def main():
    nums = ["squat", "bench", "deadlift"]
    for lift in lifts:
        keep_lifting = "yes"
        weight = 0
        input_prompt = "Keep doing the " + lift + "? Enter yes for the next set."
        while keep_lifting == "yes":
            weight = weight + 10
            if lift == "bench" and weight > 200:
                break
            else:
                workout_coach(lift, weight)
            keep_lifting = input(input_prompt)

if __name__ == "__main__":
    main()
