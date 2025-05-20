# WordCloud Generator

This repository contains a Python-based WordCloud wrapper that creates visually appealing word clouds from text data.

## Features

- Generate word clouds from csv file string columns 
- Customize font, color schemes, and shapes.
- Save word clouds as image files.
- Supports stopword filtering for cleaner results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/wordcloud.git
    cd wordcloud
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your text data (e.g., a `.csv` file or a string `.txt`).
2. Set configs.py 
2. Run the script:
    ```bash
    python main.py
    ```
3. Customize options using additional arguments:
    - `--shape`: Specify a custom shape for the word cloud.
    - `--stopwords`: Provide a list of stopwords to exclude.
    - `--color`: Choose a color palette.

## Examples

Here is an example generated using this tool:

![Example 1](output/wordcloud_DCP_blended.png)

## Acknowledgments

- Built using the [wordcloud](https://github.com/amueller/word_cloud) library.
- Inspired by creative data visualization techniques.
