from matplotlib import pyplot as plt

def func(x: list[float], N:int) -> list[float]:
    """
    Calculate function values for passed array of arguments
    """
    return [ 1-((t-N/2)/(N/2)**2) if 0 <= t <= N else None for t in x ]

def tabulate(N: int, n: int) -> tuple [list[float], list[float]]:
    x = [t for t in range(n+1) ]
    y = func(x, N)
    return (x, y)

def main():
    N=11
    n=1000
    res = tabulate(N, n)

    plt.plot(res[0], res[1])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()