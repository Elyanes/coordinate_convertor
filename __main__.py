# -*- coding: utf-8 -*-
import convertor
import os
from os.path import join as osj

def main():
    input_file = "C:\\Projets\\coordinate_convertor\\examples\\testfilé.nc"
    input_file_name = os.path.basename(input_file).split(".")[0]
    output_folder = "C:\\Projets\\coordinate_convertor\\examples"
    output_file = osj(output_folder, input_file_name + "_output.geo")
    convertor.convertor(input_file, output_file)


if __name__ == "__main__":
    main()