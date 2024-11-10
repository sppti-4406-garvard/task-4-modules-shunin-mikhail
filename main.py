import matplotlib

from geometry import rect_s, circle_s, triangle_s
from math_operations import div_, sub_
from temperature_conversion import to_celc, to_fareng
from validation import is_valid
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print(sub_(5, 2))
    print(div_(666, 0))

    print(to_fareng(-10))    # 14
    print(to_celc(14))

    print(is_valid(9), is_valid(666))

    print(rect_s(2, 5), circle_s(3), triangle_s(2, 5))


    # TASK 2:

    print(*np.array([i + 1 for i in range(10)]), sep=' ')
    print(*np.arange(1, 11))

    print(np.random.randint(-10, 10, size=(3, 3)))

    f = np.array([0] * 10)
    f[2] = 5
    print(f)

    print(np.arange(1, 12 + 1).reshape((3, 4)))

    a1 = np.array([np.random.randint(-10, 10) for _ in range(25)]).reshape((5, 5))
    a2 = np.random.randint(-10, 10, (5, 5))
    print(
        a2,
        a2.sum()
    )

    y = np.random.randint(1, 10+1, (4, 4))
    print(y)
    print([int(max(i)) for i in y])

    f = np.random.randint(-10, 10+1, (3, 3))
    print(f, f * 2)

    z1 = np.random.randint(0, 8+1, (3, 3))
    z2 = np.random.randint(0, 8+1, (3, 3))
    print(z1 * z2)

    h = np.random.randint(-10, 10, (3, 3))
    print(np.linalg.det(h))

    # TASK 3
    matplotlib.use('Qt5Agg')

    # 3.1
    time = np.linspace(0, 23, 100)  # time from 0 to 24 hours
    temperature = 10 + 10 * np.sin(time / 24 * 2 * np.pi)  # example temperature variation

    plt.figure(figsize=(10, 6))
    plt.plot(time, temperature, label="Temperature")
    plt.xlabel("Time (hours)")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 3.2
    categories = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']
    sales = np.random.randint(20, 100, size=len(categories))  # random sales data

    plt.figure()
    plt.bar(categories, sales, color='skyblue')
    plt.xlabel("Product Category")
    plt.ylabel("Sales Quantity")
    plt.title("Sales by Product Category")
    plt.show()

    #3.3
    height = np.random.normal(170, 10, 100)
    weight = np.random.normal(70, 15, 100)

    plt.figure()
    plt.scatter(height, weight, alpha=0.6, color='purple')
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Height vs. Weight Scatter Plot")
    plt.grid(True)
    plt.show()

    #3.4
    scores = np.random.randint(50, 100, 200)  # scores between 50 and 100

    plt.figure()
    plt.hist(scores, bins=10, color='orange', edgecolor='black')
    plt.xlabel("Scores")
    plt.ylabel("Number of Students")
    plt.title("Distribution of Math Scores")
    plt.show()

    #3.5
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap="viridis")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title("3D Surface Plot")
    plt.show()

    #4

    def f(x, y):
        return (x ** 2 + y ** 2 - 1) ** 3 - (x ** 2) * (y ** 3)


    # Generate x and y values
    x = np.linspace(-2, 2, 1000)
    y = np.linspace(-2, 2, 1000)

    # Create a meshgrid for x and y values
    X, Y = np.meshgrid(x, y)

    # Calculate Z values using the function
    Z = f(X, Y)

    # Plot the contour
    plt.figure(figsize=(8, 8))
    plt.contour(X, Y, Z, levels=[0], colors='red')  # Only plotting the zero level for the equation
    plt.title("Contour Plot for ((x^2 + y^2 - 1)^3) - (x^2)(y^3) = 0")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()
