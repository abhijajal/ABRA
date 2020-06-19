After installing the required dependencies, 
Task 1 program can be run as follows:
python "Task 1.py"
Where Task 1.py should be in the same folder as of "WikipediaArticles" folder.
This program will open each file in WikipediaArticles and performs all the operations.

Task 2 program can be run as follows:
python "Task 2.py" Amazon_com.txt
Where Task 2.py should be in the same folder as of "WikipediaArticles" folder,jobTitle.txt and worldcities.csv.
It also generates the Templates.json after the information extraction.
It also generates corefResolved verisons of the txt file it just  processed.

Steps to install NeuralCoref:
pip uninstall spacy 
pip uninstall neuralcoref
pip install spacy==2.1.0 
pip install neuralcoref --no-binary neuralcoref
python -m spacy download en_core_web_sm
