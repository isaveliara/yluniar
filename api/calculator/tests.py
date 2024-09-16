from image import render_steps_to_image, replace_chars_for_render_in_image

from eqt_solver import process_equation_with_steps, solve_equation
def test_equation_processing():
    test_cases = [
        "2x² + 3x + 1 = 0",      # standard quadratic equation
        "x² - 5x = 0",           # quadratic without constant
        "x² - 16 = 0",           # quadratic without linear term
        "3x + 9 = 0",            # linear equation
        "x² + 4x + 4 = 0",       # perfect square trinomial
        "x² + 0x - 25 = 0",      # equation with zero linear term
        "x² = 0",                # simple quadratic (roots at zero)
        "0x² + 5x + 10 = 0",     # linear disguised as quadratic (a=0)
        "x² + 1 = 0",            # complex roots (disrciminant < 0)
        "4 = 0"                  # invalid (no x terms, no support for non-X terms)
    ]
    
    i= 0
    for equation in test_cases:
        i+=1
        print(f"Testing equation: {equation}")
        try:
            #calling the main function of process equation
            steps = process_equation_with_steps(equation)

            
            
            steps_for_renderImage = list(map(replace_chars_for_render_in_image, steps)) #part of image

            for step in steps:
                print(step) #logging all steps of the expression
            render_steps_to_image(steps_for_renderImage, f"expression_{i}.png")
        except Exception as e:
            print(f"Error processing equation {equation}: {e}")
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    #run the test
    test_equation_processing()
