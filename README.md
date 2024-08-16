# semantic_search

## To download the model Google News pre-trained word embeddings go to the corresponding link, download it and set it in the program path.
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g


# Semantic Search

This repository provides a tool for semantic search utilizing word embeddings to measure the similarity between text content. It includes scripts and resources to implement semantic similarity calculations in Python.

## Features

- **Word Embedding Similarity**: Uses pre-trained Google News word embeddings to calculate semantic similarity between text.
- **Content Similarity Calculation**: Provides functionality to compute similarity scores between different pieces of content.
- **Efficient Search**: Enables semantic search across a corpus of text data to find the most similar content.

## Files in the Repository

- **`application.py`**: The main application script for running the semantic search and similarity calculations.
- **`content_similarity.py`**: Script to calculate the similarity between content using word embeddings.
- **`wmd_similarity.py`**: Implementation of the Word Mover's Distance (WMD) for measuring the semantic distance between documents.
- **`testing.xlsx`**: Excel file containing sample data for testing the semantic search functionality.
- **`icon.png`**: Icon or logo associated with the project.
- **`requirements.txt`**: A list of Python dependencies required to run the project.
- **`pyvenv.cfg`**: Configuration file for the virtual environment.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`LICENSE`**: License file for the project.
- **`content_similarity.cpython-310.pyc`**: Compiled Python bytecode file.
- **`Breadcrumbssemantic_search/README.md`**: Detailed instructions and explanations about the semantic search implementation.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/semantic_search.git
    cd semantic_search
    ```

2. **Set up the virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the pre-trained word embeddings**:
   - Download the Google News pre-trained word embeddings from the following link: [Google News Word Embeddings](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g)
   - Place the downloaded embeddings in the appropriate directory as specified in the scripts.

5. **Run the application**:
    ```bash
    python application.py
    ```

## Usage

- Use the `application.py` script to perform semantic searches across your text corpus.
- Customize the `content_similarity.py` and `wmd_similarity.py` scripts to suit your specific needs for content similarity calculations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

