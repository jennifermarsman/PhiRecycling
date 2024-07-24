import argparse
from cpu_recycling import run

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_path", type=str, required=True, help="Path to the model")
    args = parser.parse_args()
    image_path = 'triangular-arrows-sign-for-recycle.png'

    # Call the run function from cpu_recycling.py
    run(args, image_path)

    
if __name__ == "__main__":
    main()
