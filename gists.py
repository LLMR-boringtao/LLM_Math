# APE (Automatic Prompt Engineer)
method = """
    Take a deep breath. \
    Following the two examples below, solve the problem by proposing as many different methods as possible and finding the most logically consistent one as the final answer.
    Hints: ”algebra”;”optimization”,”equation”,”logical reasoning”

    Example 1:
    ###Problem:
    Classes A and B start from the school at the same time to go to a park that is 51 km away. Class A walks at a speed of 4 km/h, and Class B walks at a speed of 5 km/h. The school has a car that can travel at 60 km/h and can carry one class of students at a time. To ensure that both classes arrive at the park in the shortest time possible, how many kilometres do Classes A and B need to walk?
    ###Answer:
    1. Let Class A walk X km. Then the time Class A takes to walk is X/4 hours. In this time, the car travels 15X km.
    2. The car takes Class B to the point where they should start walking and then returns to meet Class A. The distance the car travels to take Class B is (15X+X)=8X. Therefore, Class B walks 51−8X km, and the time Class B takes to walk is 51−8X hours. 
    3. In this time, the car travels (51−8X)×12 km. At this point, the car needs to pick up Class A and return to the park.
    ###Solution:
    By solving the equation (51−8X)×12+(51−8X) +X=51, we get X=5.5 and 51−8X=7. Therefore, Class A walks 5.5 km, and Class B walks 7 km.

    Example 2:
    ###Problem:
    A company organises a social event. 50% of the sales department participates, and 60% of the IT department participates. The number of people from the IT department who participate is 6 more than the number from the sales department. Later, due to urgent work, 60% of the remaining people in the sales department and 50% of the remaining people in the IT department are selected to form a 30-person work team. How many employees does the company have?
    ###Answer:
    1. Let the sales department have X people and the IT department have Y people. Then the number of people participating from the sales department is 0.5X and from the IT department is 0.6Y. The IT department has 6 more people participating than the sales department, so 0.6Y−0.5X=6.
    2. The number of people participating from the sales department is 0.5X, so the remaining number is also 0.5X. 60% of the remaining people are selected, which is 0.3X. The number of people participating from the IT department is 0.6Y, so the remaining number is 0.4Y. 50% of the remaining people are selected, which is 0.2Y. Therefore, 0.3X+0.2Y=30.
    ###Solution:
    By solving the equation 0.6Y−0.5X=6 and 0.3X+0.2Y=30 to find X=60 and Y=60. Therefore, the total number of employees in the company is 120.
"""

_prompt_solution = _prompt_template_solution.format_messages(
    problem=problem,
    role=role,
    method=method
)