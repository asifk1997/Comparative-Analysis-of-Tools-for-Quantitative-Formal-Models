import subprocess
import glob as glob
from pathlib import Path
import os
import os.path
from os import path
ePMC_path = "/home/asif/ePMC/"
modes_path = "/home/asif/Downloads/Compressed/Modest/"
prism_path = "/home/asif/Downloads/Compressed/prism-4.6-linux64/bin/"

def run_jani_on_storm(file_path):
    nf = file_path.replace("jani", "storm.txt")
    # print(file_path, nf)
    f = open(nf, "w")
    p = subprocess.run(["storm", "--jani", file_path, "--timemem", "--janiproperty"], stdout=f)
    print(p)


def run_prism_on_storm(file_path):
    # if file_path.count("cluster.v1.prism") !=1:
    #     return
    pathh = Path(file_path)
    parent_path  = pathh.parent.absolute()
    print(file_path)
    nf = file_path.replace("prism", "pm.storm.txt")
    prop_file_paths = glob.glob(str(parent_path)+"/*.props")
    prop_file_name = prop_file_paths[-1]
    print("prop",prop_file_paths,prop_file_name)
    constants_file_path =  os.path.join(pathh.parent.absolute(),"constants.txt")#str(path.parent.absolute())+"/"+ "constants.txt"
    f = open(nf, "w")
    if path.exists(constants_file_path):
        constants_file = open(constants_file_path, "r")
        constants = constants_file.read()
        constants.replace("\n","")
        p = subprocess.run(["storm", "--prism", file_path, "--timemem", "--prop",prop_file_name,"-pc","--constants",constants], stdout=f, timeout=600)
    else:
        p = subprocess.run(["storm", "--prism", file_path, "--timemem", "--prop", prop_file_name, "-pc"],stdout=f, timeout=600)
    print(p)


def run_jani_on_epmc(file_path):
    nf = file_path.replace("jani", "empc.txt")
    print(file_path, nf)
    f = open(nf, "w")
    p = subprocess.run(
        ["java", "-jar", "epmc-standard.jar", "check", "--model-input-files", file_path, "--model-input-type", "jani",
         "--time-stamps", "milliseconds-absolute"], stdout=f, cwd=ePMC_path, stderr=f)
    print(p)

def run_prism_on_epmc(file_path):
    pathh = Path(file_path)
    parent_path = pathh.parent.absolute()
    nf = file_path.replace("prism", "pm.epmc.txt")
    prop_file_paths = glob.glob(str(parent_path) + "/*.props")
    prop_file_name = prop_file_paths[-1]
    print("prop", prop_file_paths, prop_file_name)
    constants_file_path = os.path.join(pathh.parent.absolute(), "constants.txt")
    f = open(nf, "w")
    if path.exists(constants_file_path):
        constants_file = open(constants_file_path, "r")
        constants = constants_file.read()
        constants = constants.replace("\n", "")
        constants = constants.replace(" ", "")
        p = subprocess.run(["java", "-jar", "epmc-standard.jar", "check", "--model-input-files", file_path, "--model-input-type", "prism","--property-input-files",prop_file_name, "--const",constants,"--time-stamps", "milliseconds-absolute"], stdout=f, cwd=ePMC_path, stderr=f)
    else:
        p = subprocess.run(["java", "-jar", "epmc-standard.jar", "check", "--model-input-files", file_path, "--model-input-type", "prism","--property-input-files",prop_file_name,"--time-stamps", "milliseconds-absolute"], stdout=f, cwd=ePMC_path, stderr=f)
    print(p)

def run_jani_on_mcsta(file_path):
    print(file_path)
    if file_path.count("cluster")==0:
        return
    # pathh = Path(file_path)
    # constants_file_path = os.path.join(pathh.parent.absolute(), "constants.txt")
    # constants_file = open(constants_file_path, "r")
    # constants = constants_file.read()
    # constants = constants.replace("\n", "")
    # constants = constants.replace(" ", "")
    nf = file_path.replace("jani", "mcsta.txt")
    print(file_path, nf)
    f = open(nf, "w")
    try:
        p = subprocess.run(["./modest", "mcsta", file_path], stdout=f, cwd=modes_path, stderr=f, timeout=600)
    except subprocess.TimeoutExpired as e:
        f.write(str(e))
        p = e
    print(p)

def run_modest_on_mcsta(file_path):
    nf = file_path.replace("modest", "md.mcsta.txt")
    print(file_path, nf)
    f = open(nf, "w")
    pathh = Path(file_path)
    constants_file_path = os.path.join(pathh.parent.absolute(), "constants.txt")
    constants_file = open(constants_file_path, "r")
    constants = constants_file.read()
    constants = constants.replace("\n", "")
    constants = constants.replace(" ", "")
    try:
        p = subprocess.run(["./modest", "mcsta", file_path,"-E",constants], stdout=f, cwd=modes_path, stderr=f, timeout=600)
    except subprocess.TimeoutExpired as e:
        f.write(str(e))
        p = e
    print(p)

def run_jani_on_modes(file_path):
    nf = file_path.replace("jani", "modes.txt")
    print(file_path, nf)
    f = open(nf, "w")
    try:
        p = subprocess.run(["./modest", "modes", file_path], stdout=f, cwd=modes_path, stderr=f, timeout=600)
    except subprocess.TimeoutExpired as e:
        f.write(str(e))
        p = e
    print(p)

def run_modest_on_modes(file_path):

    nf = file_path.replace("modest", "md.modes.txt")
    print(file_path, nf)
    f = open(nf, "w")
    pathh = Path(file_path)
    constants_file_path = os.path.join(pathh.parent.absolute(), "constants.txt")
    constants_file = open(constants_file_path, "r")
    constants = constants_file.read()
    constants = constants.replace("\n", "")
    constants = constants.replace(" ", "")
    try:
        p = subprocess.run(["./modest", "modes", file_path, "-E", constants], stdout=f, cwd=modes_path, stderr=f,
                           timeout=600)
    except subprocess.TimeoutExpired as e:
        f.write(str(e))
        p = e
    print(p)

def run_prism_on_prism_tool(file_path):
    pathh = Path(file_path)
    parent_path = pathh.parent.absolute()
    nf = file_path.replace("prism", "pm.pmtool.txt")
    prop_file_paths = glob.glob(str(parent_path) + "/*.props")
    prop_file_name = prop_file_paths[-1]
    print("prop", prop_file_paths, prop_file_name)
    constants_file_path = os.path.join(pathh.parent.absolute(), "constants.txt")
    f = open(nf, "w")
    if path.exists(constants_file_path):
        constants_file = open(constants_file_path, "r")
        constants = constants_file.read()
        constants = constants.replace("\n", "")
        constants = constants.replace(" ","")
        p = subprocess.run(["./prism", file_path, prop_file_name, "-const", constants,"-extrareachinfo"],stdout=f,stderr=f, timeout=600,cwd=prism_path)
    else:
        p = subprocess.run(["./prism", file_path, prop_file_name, "-extrareachinfo"], stdout=f,stderr=f,timeout=600,cwd=prism_path)
    print(p)


def run_tools(file_path):
    if "jani" in file_path:
        # run_jani_on_storm(file_path)
        # run_jani_on_epmc(file_path)
        run_jani_on_mcsta(file_path)
        # run_jani_on_modes(file_path)
        pass
    elif "prism" in file_path:
        # run_prism_on_storm(file_path)
        # run_prism_on_prism_tool(file_path)
        # run_prism_on_epmc(file_path)
        pass
    elif "modest" in file_path:
        # run_modest_on_mcsta(file_path)
        # run_modest_on_modes(file_path)
        pass


dataset_folder = "/home/asif/PycharmProjects/PECSS/dataset/*"
folders = glob.glob(dataset_folder)
for ff in folders:
    automata_type_folders = glob.glob(ff + "/*")
    for g in automata_type_folders:
        automata_folders = glob.glob(g + "/*")
        for h in automata_folders:
            print(h)
            # run_jani_on_storm(h)
            run_tools(h)
        print()
    print()
