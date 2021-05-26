We used Ubuntu 20.04 for running the tools.
For running the software you need to install all the tools:
ePMC - https://github.com/ISCAS-PMC/ePMC
STORM - https://www.prismmodelchecker.org/
Modes - https://www.modestchecker.net/
Mcsta - https://www.modestchecker.net/
Prism - https://www.prismmodelchecker.org/

1. Setup the path of the folders where you have downloaded the softwares in main.py file like this:

ePMC_path = "/home/asif/ePMC/"
modes_path = "/home/asif/Downloads/Compressed/Modest/"
prism_path = "/home/asif/Downloads/Compressed/prism-4.6-linux64/bin/"

2. Also change dataset folder path in main.py like this:

dataset_folder = "/home/asif/PycharmProjects/PECSS/dataset/*"

3. Run main.py like : python main.py
It will run all the files and along with generate the output report for all the tools in the dataset folder as well.


4. Look at the dataset report.


5. Make CSV from those reports.
We have made report in csvs folder.

6. Run "draw_graphs_peak_memory.py" and "draw_graph_properties.py" to generate the graphs from the CSV's.




