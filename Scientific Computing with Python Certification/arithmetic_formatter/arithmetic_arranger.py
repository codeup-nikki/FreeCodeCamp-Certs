def arithmetic_arranger(problems, display = False):
  row1 = ""
  row2 = ""
  row3 = ""

  #if problems.len() > 5:
  #  output = "Error: Too Many problems."
  
  for i, ele in enumerate(problems):
    sub = ele.split()
    row1 += f"{str(sub[0]) :>10}"
    hold = f"{str(sub[1]) + ' ' + str(sub[2]) :>10}"
    row2 += f"{str(sub[1]) + ' ' + str(sub[2]) :>10}"
    row3 += f"{ '_'*(len(hold)-5) :>10}"

  output = row1 + '\n'+ row2 + '\n' + row3

  return output