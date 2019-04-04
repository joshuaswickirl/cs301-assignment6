import sys
import os

# append project root directory to sys.path
sys.path.append(
    os.path.dirname(  # project root
        os.path.dirname(  # tests dir
            os.path.abspath(__file__)  # tests/env.py
        )
    )
)