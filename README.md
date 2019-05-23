# Thesis
Literature mining for cancer-marker databasing

1. Use NER to annotate abstracts
2. Use Kindred to find relations
3. Collate relations into database

Install Kindred in a virtual environment:
`python3 -m venv env`
`source ./env/bin/activate`
`pip install kindred`
`python -m spacy download en`