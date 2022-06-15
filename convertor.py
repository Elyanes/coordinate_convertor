# -*- coding: utf-8 -*-
import re


def convertor(input_file, output_file):
    with open(input_file, "r") as read_file, open(output_file, "w") as write_file:
        write_file.write("%N001 M63\nN002 D01 T01 S01 P01 G43\n")
        line_number = 3
        g_value = "G01"
        for line in read_file:
            line = line.rstrip()
            if ("X" in line and line.startswith("N")) or ("Y" in line and line.startswith("N")) :
                line = line.split(" ")
                line[0] = f"N{line_number:03d}"
                if line[1] == "G00":
                    line[1] = g_value
                elif not line[1].startswith("G"):
                    line.insert(1, g_value)
                elif not line[1] == "G00" and line[1].startswith("G") and not line[1] == g_value:
                    g_value = line[1]
                for i in range (1, len(line)):
                    if line[i].startswith("Y") or line[i].startswith("X") or line[i].startswith("Z") or line[i].startswith("I") or line[i].startswith("J") or line[i].startswith("F"):
                        coordinate_string = line[i]
                        negative = False
                        if "-" in coordinate_string :
                            negative = True
                        if not coordinate_string.endswith("."):
                            temp = re.findall(r'\d+', coordinate_string)
                            m_value = float(".".join(temp))
                            mm_value = round(m_value*1000)
                            dec_number = f"{mm_value:06d}"
                            if negative is True:
                                line[i] = f"{line[i][0]}-{dec_number}" 
                            else:
                                line[i] = f"{line[i][0]}+{dec_number}" 
                        elif coordinate_string.endswith("."):
                            temp = re.findall(r'\d+', coordinate_string)
                            m_value = float(".".join(temp))
                            mm_value = round(m_value*100)
                            dec_number = f"{mm_value:06d}"
                            if negative is True and line[i][0] != "F":
                                line[i] = f"{line[i][0]}-{dec_number}" 
                            elif negative is False and line[i][0] != "F":
                                line[i] = f"{line[i][0]}+{dec_number}" 
                            elif negative is True and line[i][0] == "F":
                                line[i] = f"{line[i][0]}{dec_number}" 
                            elif negative is False and line[i][0] == "F":
                                line[i] = f"{line[i][0]}{dec_number}"
                converted_line = " ".join(line)
                if not "000000" in converted_line:
                    write_file.write(converted_line + "\n")
                else:
                    continue
            line_number = line_number + 1
        write_file.write(f"N{line_number} G45\nN{line_number+1} M02\n")

        

            
        

if __name__ == '__main__':
    pass