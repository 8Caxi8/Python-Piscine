import sys

try:
    import pandas as pd
    import requests as rq
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError as e:
    print(f"[ERROR]: {e.name} not installed.\n"
          "Install with: pip install -r requirements.txt")
    raise sys.exit(1)


def check_dependencies() -> None:
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    print(f"[OK] requests ({rq.__version__}) - Network access ready")
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    print(f"[OK] numpy ({np.__version__}) - Data generation ready\n")


def generate_data() -> pd.DataFrame:
    no = list(np.random.rand(1000))

    df = pd.DataFrame(no, columns=["matrix_data"])

    return df


def get_nasaapi_data(longitude: float, latitude: float,
                     start: int, end: int) -> pd.DataFrame:
    url = ("https://power.larc.nasa.gov/api/temporal/daily/point"
           "?parameters=ALLSKY_SFC_SW_DWN"
           "&community=RE"
           f"&longitude={longitude}"
           f"&latitude={latitude}"
           f"&start={start}"
           f"&end={end}"
           "&format=JSON")

    response = rq.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    values = data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]

    df = pd.DataFrame(list(values.items()),
                      columns=["date", "solar_radiation"])

    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")

    return df


def analyze_data(df: pd.DataFrame, data_type: str
                 ) -> tuple[pd.DataFrame, float, float, float]:
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} data points...")

    mean = df[data_type].mean()
    std = df[data_type].std()
    median = df[data_type].median()

    return df, mean, std, median


def create_solar_visualization(statistics:
                               tuple[pd.DataFrame, float, float, float],
                               longitude: float,
                               latitude: float
                               ) -> None:
    FILE_NAME = "solar_radiation_analysis.png"

    df, mean, std, median = statistics

    print("Generating visualization...")

    start_date = df["date"].min().date()
    end_date = df["date"].max().date()

    plt.figure(figsize=(12, 6))

    plt.scatter(
        df["date"],
        df["solar_radiation"],
        color="orange",
        s=30,
        label="Daily Solar Radiation"
    )

    plt.plot(
        df["date"],
        df["solar_radiation"],
        color="orange",
        linewidth=0.5,
        alpha=0.5,
        )

    plt.axhline(
        mean,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Mean ({mean:.2f})"
    )

    plt.axhline(
        median,
        color="blue",
        linestyle="-.",
        linewidth=2,
        label=f"Median ({median:.2f})"
    )

    plt.axhline(
        mean + std,
        color="green",
        linestyle=":",
        linewidth=2,
        label=f"Mean + Std ({(mean + std):.2f})"
    )

    plt.axhline(
        mean - std,
        color="green",
        linestyle=":",
        linewidth=2,
        label=f"Mean - Std ({(mean - std):.2f})"
    )

    plt.xlabel("Date")
    plt.ylabel("Solar Radiation (kWh/m²/day)")
    plt.title("Daily Solar Radiation - NASA POWER Data\n"
              f"{latitude:.4f}°, {longitude:.4f}° | "
              f"{start_date} to {end_date}")

    plt.grid(alpha=0.3)
    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(FILE_NAME)

    print("\nAnalysis complete!")
    print(f"Results saved to: {FILE_NAME}")


def create_matrix_visualization(statistics:
                                tuple[pd.DataFrame, float, float, float]
                                ) -> None:
    FILE_NAME = "matrix_analysis.png"

    df, mean, std, median = statistics

    print("Generating visualization...")

    plt.figure()
    plt.title("Matrix Data Distribution")
    plt.hist(
        df["matrix_data"],
        bins=30,
        color="green",
        alpha=0.6,
        label="Data Distribution"
    )
    plt.axvline(
        mean,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Mean ({mean:.2f})"
    )
    plt.axvline(
        median,
        color="blue",
        linestyle="-.",
        linewidth=2,
        label=f"Median ({median:.2f})"
    )
    plt.axvline(
        mean - std,
        color="orange",
        linestyle=":",
        linewidth=2,
        label="Mean - Std"
    )
    plt.axvline(
        mean + std,
        color="orange",
        linestyle=":",
        linewidth=2,
        label="Mean + Std"
    )
    plt.savefig(FILE_NAME)
    print("\nAnalysis complete!")
    print(f"Results saved to: {FILE_NAME}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Check dependencies:")
    longitude = -9.1393
    latitude = 38.7223

    check_dependencies()
    try:
        data = get_nasaapi_data(longitude, latitude, 20250101, 20260101)
        data_type = "solar_radiation"

    except (rq.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"Requests Error: {e}")
        print("Generating backup data...\n")
        data = generate_data()
        data_type = "matrix_data"

    statistics = analyze_data(data, data_type)

    if data_type == "solar_radiation":
        create_solar_visualization(statistics, longitude, latitude)
    else:
        create_matrix_visualization(statistics)


if __name__ == "__main__":
    main()
