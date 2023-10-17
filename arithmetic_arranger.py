def arithmetic_arranger(problems, answers=False):

  if len(problems) > 5:
    return "Error: Too many problems"

  line_1 = ""
  line_2 = ""
  line_3 = ""
  line_4 = ""
  counter = 0
  for problem in problems:
    counter += 1

    if "+" in problem:
      operator = "+"
    elif "-" in problem:
      operator = "-"
    else:
      return "Error: Operator must be '+' or '-'."

    items = problem.split(operator)
    items[0] = items[0].strip()
    items[1] = items[1].strip()

    if items[0].isnumeric() is False or items[1].isnumeric() is False:
      return "Error: Numbers must only contain digits."
    if len(items[0]) > 4 or len(items[1]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if answers:
      if operator == "+":
        items.append(str(int(items[0]) + int(items[1])))
      else:
        items.append(str(int(items[0]) - int(items[1])))

    if len(items[0]) <= len(items[1]):
      items[0] = items[0].rjust(len(items[1]) + 2)
      items[1] = operator + items[1].rjust(len(items[0]) - 1)
    else:
      items[0] = items[0].rjust(len(items[0]) + 2)
      items[1] = operator + items[1].rjust(len(items[0]) - 1)

    line_1 += items[0]
    line_2 += items[1]
    line_3 += "-" * len(items[0])
    if answers:
      items[2] = items[2].rjust(len(items[1]))
      line_4 += items[2]

    if counter < len(problems):
      line_1 += "    "
      line_2 += "    "
      line_3 += "    "
      if answers:
        line_4 += "    "

  arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3
  if answers:
    arranged_problems += "\n" + line_4

  return arranged_problems
